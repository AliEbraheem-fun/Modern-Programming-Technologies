# -*- coding: utf-8 -*-
"""
Проверяет одну главу учебного пособия: компилирует её изолированно
и сообщает об ошибках LaTeX, переполнениях полосы набора и объёме.

    python checkchapter.py 04
"""
import io
import os
import re
import subprocess
import sys

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))

WRAPPER = r"""\documentclass[14pt,a4paper,oneside]{extbook}
\input{preamble}
\begin{document}
\input{chapters/ch%s}
\end{document}
"""


def main():
    if len(sys.argv) != 2:
        raise SystemExit('usage: python checkchapter.py NN   (e.g. 04)')
    nn = sys.argv[1].zfill(2)
    chapter = os.path.join(HERE, 'chapters', 'ch%s.tex' % nn)
    if not os.path.exists(chapter):
        raise SystemExit('NOT FOUND: %s' % chapter)

    # объём главы
    src = io.open(chapter, encoding='utf-8').read()
    chars = len(src)

    wrapper_name = '_check_ch%s' % nn
    wrapper_path = os.path.join(HERE, wrapper_name + '.tex')
    io.open(wrapper_path, 'w', encoding='utf-8', newline='\n').write(WRAPPER % nn)

    build_dir = os.path.join(HERE, 'build')
    # minted не работает с -output-directory, поэтому собираем в текущем
    # каталоге, а временные файлы убираем в конце
    cmd = ['xelatex', '-shell-escape', '-interaction=nonstopmode', wrapper_path]
    # два прохода — для ссылок
    for _ in range(2):
        subprocess.run(cmd, cwd=HERE, stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)

    log_path = os.path.join(HERE, wrapper_name + '.log')
    pdf_path = os.path.join(HERE, wrapper_name + '.pdf')

    errors, overfull, undefined = [], [], []
    if os.path.exists(log_path):
        log = io.open(log_path, encoding='utf-8', errors='replace').read()
        errors = re.findall(r'^! .*$', log, re.M)
        overfull = re.findall(r'^Overfull \\hbox \(([\d.]+)pt', log, re.M)
        undefined = re.findall(r'Reference `([^\']+)\' on page', log)

    print('=' * 60)
    print('ГЛАВА %s' % nn)
    print('=' * 60)
    print('объём:        %d знаков' % chars)
    print('PDF собран:   %s' % ('да' if os.path.exists(pdf_path) else 'НЕТ'))
    print('ошибок LaTeX: %d' % len(errors))
    for e in errors[:15]:
        print('   ' + e.strip())
    big = [o for o in overfull if float(o) > 5.0]
    print('вылетов за поля (>5pt): %d' % len(big))
    if big[:5]:
        print('   величины: ' + ', '.join(big[:5]) + ' pt')
    if undefined:
        print('битых ссылок: %d -> %s' % (len(undefined), sorted(set(undefined))[:8]))
    else:
        print('битых ссылок: 0')

    try:
        os.remove(wrapper_path)
    except OSError:
        pass

    ok = os.path.exists(pdf_path) and not errors and not big
    print()
    print('ИТОГ: ' + ('ОК' if ok else 'ТРЕБУЕТ ИСПРАВЛЕНИЙ'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
