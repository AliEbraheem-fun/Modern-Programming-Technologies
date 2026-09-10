# -*- coding: utf-8 -*-
"""
Полная сборка учебного пособия.

    python build.py

Порядок: генерация приложения с ключами -> два прохода xelatex
(второй нужен для оглавления и перекрёстных ссылок) -> отчёт.
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
MAIN = 'posobie'


def run(cmd, **kw):
    return subprocess.run(cmd, cwd=HERE, stdout=subprocess.DEVNULL,
                          stderr=subprocess.DEVNULL, **kw)


def main():
    print('1. Генерация ключей к тестам...')
    run([sys.executable, 'genkeys.py'])

    print('2. Сборка PDF (проход 1 из 2)...')
    run(['xelatex', '-shell-escape', '-interaction=nonstopmode', MAIN + '.tex'])
    print('   Сборка PDF (проход 2 из 2)...')
    run(['xelatex', '-shell-escape', '-interaction=nonstopmode', MAIN + '.tex'])

    log_path = os.path.join(HERE, MAIN + '.log')
    pdf_path = os.path.join(HERE, MAIN + '.pdf')

    if not os.path.exists(log_path):
        print('ЛОГ НЕ СОЗДАН — сборка не запускалась')
        return 1

    log = io.open(log_path, encoding='utf-8', errors='replace').read()
    errors = re.findall(r'^! .*$', log, re.M)
    overfull = [float(x) for x in re.findall(r'^Overfull \\hbox \(([\d.]+)pt', log, re.M)]
    big = [o for o in overfull if o > 5.0]
    undef_ref = set(re.findall(r"Reference `([^']+)' on page", log))
    undef_cite = set(re.findall(r"Citation `([^']+)'", log))
    pages = re.findall(r'Output written on .*?\((\d+) pages', log)

    print()
    print('=' * 58)
    print('РЕЗУЛЬТАТ СБОРКИ')
    print('=' * 58)
    print('PDF:            %s' % ('собран' if os.path.exists(pdf_path) else 'НЕ СОБРАН'))
    if pages:
        print('страниц:        %s' % pages[0])
    if os.path.exists(pdf_path):
        print('размер:         %.1f МБ' % (os.path.getsize(pdf_path) / 1048576.0))
    print('ошибок LaTeX:   %d' % len(errors))
    for e in errors[:12]:
        print('    ' + e.strip())
    print('вылетов за поля (>5pt): %d' % len(big))
    if big:
        print('    максимум: %.1f pt' % max(big))
    print('битых ссылок:   %d' % len(undef_ref))
    for r in sorted(undef_ref)[:10]:
        print('    ' + r)
    if undef_cite:
        print('битых цитат:    %d' % len(undef_cite))

    # объём в печатных листах — по знакам исходников
    total = 0
    for sub in ('chapters', 'front', 'back'):
        d = os.path.join(HERE, sub)
        if not os.path.isdir(d):
            continue
        for f in os.listdir(d):
            if f.endswith('.tex'):
                total += len(io.open(os.path.join(d, f), encoding='utf-8').read())
    print('объём исходников: %d знаков = %.1f п.л.' % (total, total / 40000.0))

    ok = os.path.exists(pdf_path) and not errors and not undef_ref
    print()
    print('ИТОГ: ' + ('ГОТОВО' if ok else 'ЕСТЬ ЗАМЕЧАНИЯ'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
