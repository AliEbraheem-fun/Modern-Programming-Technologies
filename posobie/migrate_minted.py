# -*- coding: utf-8 -*-
r"""
Переводит листинги глав с пакета listings на minted.

Причина: под XeLaTeX пакет listings ломает кириллицу внутри кода —
ASCII-знак перед русской буквой переставляется («// Java-объектом»
печатается как «// Javaобъектом-»), а строка, начинающаяся с кириллицы,
приклеивается к предыдущей и сбивает нумерацию. minted (через Pygments)
обрабатывает UTF-8 корректно. Проверено на test_minted.tex.

Преобразование:

    \begin{lstlisting}[language=Java,caption={Текст},label={lst:01-1}]
    КОД
    \end{lstlisting}

становится

    \begin{listing}[H]
    \begin{minted}{java}
    КОД
    \end{minted}
    \caption{Текст}
    \label{lst:01-1}
    \end{listing}

    python migrate_minted.py            # все главы
    python migrate_minted.py --dry-run  # только показать, что изменится
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

LANG_MAP = {
    'java': 'java',
    'xml': 'xml',
    'bash': 'bash',
    'sql': 'sql',
    'html': 'html',
    'c': 'c',
    'kotlinlang': 'kotlin',
    'kotlin': 'kotlin',
    'json': 'json',
    'yaml': 'yaml',
    'properties': 'properties',
}
# листинг без language= — консольная сессия, вывод программы, конфиг:
# подсветка там мешает, поэтому берём нейтральный лексер
DEFAULT_LANG = 'text'

BLOCK = re.compile(
    r'\\begin\{lstlisting\}(\[[^\]]*\])?\n(.*?)\n[ \t]*\\end\{lstlisting\}',
    re.S)


def parse_opts(raw):
    """Достаёт language/caption/label из необязательных параметров."""
    if not raw:
        return None, None, None
    body = raw[1:-1]
    lang = None
    m = re.search(r'language=([A-Za-z_]+)', body)
    if m:
        lang = m.group(1)
    caption = None
    m = re.search(r'caption=\{(.*?)\}(?=\s*,\s*label=|\s*$|\s*,)', body, re.S)
    if m:
        caption = m.group(1)
    else:
        m = re.search(r'caption=\{(.*)\}', body, re.S)
        if m:
            caption = m.group(1)
    label = None
    m = re.search(r'label=\{([^}]*)\}', body)
    if m:
        label = m.group(1)
    return lang, caption, label


def convert(text):
    n = [0]

    def repl(m):
        raw_opts, code = m.group(1), m.group(2)
        lang, caption, label = parse_opts(raw_opts)
        key = (lang or '').lower()
        minted_lang = LANG_MAP.get(key, DEFAULT_LANG)
        n[0] += 1

        out = []
        has_float = bool(caption or label)
        if has_float:
            out.append('\\begin{listing}[H]')
        out.append('\\begin{minted}{%s}' % minted_lang)
        out.append(code)
        out.append('\\end{minted}')
        if caption:
            out.append('\\caption{%s}' % caption)
        if label:
            out.append('\\label{%s}' % label)
        if has_float:
            out.append('\\end{listing}')
        return '\n'.join(out)

    return BLOCK.sub(repl, text), n[0]


def main():
    dry = '--dry-run' in sys.argv
    files = sorted(glob.glob(os.path.join(HERE, 'chapters', 'ch*.tex')))
    total = 0
    for f in files:
        src = io.open(f, encoding='utf-8').read()
        new, cnt = convert(src)
        left = len(re.findall(r'\\begin\{lstlisting\}', new))
        status = 'ok' if left == 0 else 'ОСТАЛОСЬ %d' % left
        print('%-24s листингов: %3d   %s' % (os.path.basename(f), cnt, status))
        total += cnt
        if not dry and new != src:
            io.open(f, 'w', encoding='utf-8', newline='\n').write(new)
    print()
    print('ВСЕГО ПЕРЕВЕДЕНО: %d%s' % (total, ' (пробный прогон)' if dry else ''))


if __name__ == '__main__':
    main()
