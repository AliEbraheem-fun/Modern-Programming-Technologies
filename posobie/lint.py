# -*- coding: utf-8 -*-
r"""
Проверка .tex-файлов пособия на типичные дефекты машинной генерации.

    python lint.py              # все файлы
    python lint.py chapters/ch01.tex

Ловит:
  * иероглифы CJK и прочие посторонние алфавиты;
  * эмодзи;
  * остатки markdown (**, ##, ```, |---|, [текст](ссылка));
  * прямые кавычки вместо ёлочек;
  * дефис вместо длинного тире между словами;
  * рисунки/таблицы/листинги без \label или без ссылки в тексте;
  * ссылки на сайт, GitHub, «Лекция N», «Практика N»;
  * слишком длинные строки внутри lstlisting (вылезут за поля).
"""
import glob
import io
import os
import re
import sys

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
MAX_CODE_LINE = 72

CJK = re.compile(r'[\u3000-\u9fff\uac00-\ud7af\uff00-\uffef]')
EMOJI = re.compile(r'[\U0001F300-\U0001FAFF\u2600-\u27BF]')
MD_BOLD = re.compile(r'\*\*[^*]+\*\*')
MD_HEAD = re.compile(r'^#{1,6}\s')
MD_FENCE = re.compile(r'```')
MD_TABLE = re.compile(r'^\|[-\s|:]+\|\s*$')
# markdown-ссылка: скобки со ссылкой внутри. Требуем, чтобы в круглых скобках
# было похоже на адрес (.md, http, слэш или якорь), иначе под правило попадают
# узлы TikZ вида \node[boxw=23mm](a){...}
MD_LINK = re.compile(r'\[[^\]]+\]\([^)]*(?:\.md|https?://|/|\#)[^)]*\)')
STRAIGHT_Q = re.compile(r'"[А-Яа-яЁё]')
OLD_REF = re.compile(r'(Лекци[а-я]+\s+\d+|Практик[а-я]*\s+\d+|Практическое\s+занятие\s+\d+)')
WEB_REF = re.compile(r'(github\.com|quiz\d|exam\.html|_sidebar|docsify)')


def check_file(path):
    rel = os.path.relpath(path, HERE)
    text = io.open(path, encoding='utf-8').read()
    lines = text.split('\n')
    problems = []

    in_code = False
    for i, line in enumerate(lines, 1):
        if re.search(r'\\begin\{(lstlisting|minted|verbatim|Verbatim)\}', line):
            in_code = True
            continue
        if re.search(r'\\end\{(lstlisting|minted|verbatim|Verbatim)\}', line):
            in_code = False
            continue

        m = CJK.search(line)
        if m:
            problems.append((i, 'CJK', 'посторонний алфавит: %r' % m.group(0)))
        m = EMOJI.search(line)
        if m:
            problems.append((i, 'EMOJI', 'эмодзи: %r' % m.group(0)))

        if in_code:
            if len(line) > MAX_CODE_LINE:
                problems.append((i, 'LONGCODE',
                                 'строка кода %d симв. (>%d), вылезет за поля'
                                 % (len(line), MAX_CODE_LINE)))
            continue

        # вне кода
        if MD_BOLD.search(line):
            problems.append((i, 'MD', 'markdown-жирный ** вместо \\textbf'))
        if MD_HEAD.match(line):
            problems.append((i, 'MD', 'markdown-заголовок #'))
        if MD_FENCE.search(line):
            problems.append((i, 'MD', 'markdown-ограждение ```'))
        if MD_TABLE.match(line):
            problems.append((i, 'MD', 'markdown-таблица |---|'))
        if MD_LINK.search(line):
            problems.append((i, 'MD', 'markdown-ссылка [..](..)'))
        # прямые кавычки внутри \texttt{...} — это строковый литерал кода,
        # там они уместны; проверяем только обычную прозу
        prose_only = re.sub(r'\\texttt\{[^}]*\}', '', line)
        if STRAIGHT_Q.search(prose_only):
            problems.append((i, 'QUOTES', 'прямые кавычки вместо «ёлочек»'))
        m = OLD_REF.search(line)
        if m:
            problems.append((i, 'OLDREF',
                             'ссылка на структуру сайта: %r' % m.group(0)))
        m = WEB_REF.search(line)
        if m:
            problems.append((i, 'WEBREF', 'след сайта: %r' % m.group(0)))

    # ссылки на плавающие объекты
    labels = set(re.findall(r'\\label\{([^}]+)\}', text))
    refs = set(re.findall(r'\\ref\{([^}]+)\}', text))
    for kind, prefix in (('рисунок', 'fig:'), ('таблица', 'tab:'), ('листинг', 'lst:')):
        declared = {l for l in labels if l.startswith(prefix)}
        unref = declared - refs
        for l in sorted(unref):
            problems.append((0, 'NOREF',
                             'на %s %s нет ссылки \\ref в тексте' % (kind, l)))
    # ссылки между файлами проверяются глобально в main(), а не здесь

    # плавающие объекты без label вовсе
    n_fig = len(re.findall(r'\\begin\{figure\}', text))
    n_figlab = len([l for l in labels if l.startswith('fig:')])
    if n_fig > n_figlab:
        problems.append((0, 'NOLABEL',
                         'рисунков %d, а label только %d' % (n_fig, n_figlab)))

    return rel, problems, len(text), labels, refs


def main():
    if len(sys.argv) > 1:
        targets = [os.path.join(HERE, a) for a in sys.argv[1:]]
    else:
        targets = (sorted(glob.glob(os.path.join(HERE, 'chapters', '*.tex')))
                   + sorted(glob.glob(os.path.join(HERE, 'front', '*.tex')))
                   + sorted(glob.glob(os.path.join(HERE, 'back', '*.tex'))))
    if not targets:
        print('нет файлов для проверки')
        return 0

    total = 0
    all_labels = set()
    all_refs = {}
    for path in targets:
        if not os.path.exists(path):
            print('НЕТ ФАЙЛА: %s' % path)
            continue
        rel, problems, size, labels, refs = check_file(path)
        all_labels |= labels
        for r in refs:
            all_refs.setdefault(r, rel)
        status = 'OK' if not problems else '%d замечаний' % len(problems)
        print('%-28s %7d знаков  %s' % (rel, size, status))
        for ln, kind, msg in problems[:25]:
            loc = ('стр. %d' % ln) if ln else 'файл'
            print('    [%-8s] %-9s %s' % (kind, loc, msg))
        if len(problems) > 25:
            print('    ... ещё %d' % (len(problems) - 25))
        total += len(problems)

    # межфайловые ссылки: проверяем только когда просматриваем весь комплект
    if len(sys.argv) == 1:
        broken = sorted(set(all_refs) - all_labels)
        if broken:
            print()
            print('БИТЫЕ ССЫЛКИ МЕЖДУ ФАЙЛАМИ:')
            for r in broken:
                print('    \\ref{%s}  (в %s) — нет \\label' % (r, all_refs[r]))
            total += len(broken)

    print()
    print('ВСЕГО ЗАМЕЧАНИЙ: %d' % total)
    return 0 if total == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
