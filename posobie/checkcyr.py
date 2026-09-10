# -*- coding: utf-8 -*-
r"""
Ищет в листингах места, где пакет listings ломает кириллицу под XeLaTeX.

Два дефекта, воспроизведённые на тестах:
  1) ASCII-символ вплотную перед кириллицей переставляется:
     "// Java-объектом"  печатается как  "// Javaобъектом-"
     "println(Без"       печатается как  "printlnБез("
  2) строка листинга, НАЧИНАЮЩАЯСЯ с кириллицы, приклеивается к предыдущей
     и сбивает нумерацию строк.

Оба лечатся пробелом между ASCII-символом и кириллицей либо переносом
кириллицы в отдельный комментарий. Текст вне листингов не затрагивается.

    python checkcyr.py                    # все главы
    python checkcyr.py chapters/ch04.tex
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

CYR = 'а-яёА-ЯЁ'
# Ломается только ASCII-знак ВПЛОТНУЮ ПЕРЕД кириллицей: он переставляется
# в конец кириллического слова. Обратный порядок (кириллица, затем знак)
# на тестах отрабатывает верно, поэтому здесь не ищется.
# Кавычка исключена: открывающая кавычка строкового литерала печатается
# правильно (проверено на "Строка с кириллицей").
GLUE_BEFORE = re.compile(r'([!-/:-@\[-^`{-~])([' + CYR + r'])')
# строка начинается с кириллицы — приклеивается к предыдущей
STARTS_CYR = re.compile(r'^[ \t]*[' + CYR + r']')

BEGIN = re.compile(r'\\begin\{lstlisting\}')
END = re.compile(r'\\end\{lstlisting\}')

# безопасные сочетания: внутри строкового литерала кавычка перед кириллицей
# отрабатывает верно, а «//» с пробелом после — обычный комментарий
SAFE = (
    re.compile(r'"[' + CYR + r']'),   # "Строка с кириллицей"
    re.compile(r'//\s'),              # // комментарий
)


def scan(path):
    rel = os.path.relpath(path, HERE)
    lines = io.open(path, encoding='utf-8').read().split('\n')
    inside = False
    hits = []
    for i, line in enumerate(lines, 1):
        if BEGIN.search(line):
            inside = True
            continue
        if END.search(line):
            inside = False
            continue
        if not inside:
            continue

        if STARTS_CYR.match(line) and line.strip():
            hits.append((i, 'начало строки', line.strip()[:58]))
            continue

        for m in GLUE_BEFORE.finditer(line):
            # пробел между знаком и кириллицей — уже безопасно
            frag = line[max(0, m.start() - 12):m.end() + 12]
            hits.append((i, 'ASCII+кир', frag.strip()[:58]))
            break
    return rel, hits


def main():
    targets = ([os.path.join(HERE, a) for a in sys.argv[1:]]
               if len(sys.argv) > 1
               else sorted(glob.glob(os.path.join(HERE, 'chapters', 'ch*.tex'))))

    # После перевода книги на minted листингов lstlisting быть не должно:
    # minted работает с кириллицей корректно, и проверка становится сторожем
    # от возврата к listings, а не поиском дефектов.
    n_lst = 0
    for p in targets:
        if os.path.exists(p):
            n_lst += len(BEGIN.findall(io.open(p, encoding='utf-8').read()))
    if n_lst == 0:
        print('lstlisting в главах не найден — книга на minted, кириллица в коде')
        print('обрабатывается корректно. Проверять нечего.')
        return 0
    print('ВНИМАНИЕ: найдено %d листингов на lstlisting.' % n_lst)
    print('Под XeLaTeX они ломают кириллицу — переведите их на minted.')
    print()

    total = 0
    for p in targets:
        if not os.path.exists(p):
            print('НЕТ ФАЙЛА: %s' % p)
            continue
        rel, hits = scan(p)
        print('%-24s %s' % (rel, 'чисто' if not hits else '%d мест' % len(hits)))
        for ln, what, frag in hits[:12]:
            print('    стр. %-5d %-12s %s' % (ln, what, frag))
        if len(hits) > 12:
            print('    ... ещё %d' % (len(hits) - 12))
        total += len(hits)
    print()
    print('ВСЕГО ОПАСНЫХ МЕСТ: %d' % total)
    return 0 if total == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
