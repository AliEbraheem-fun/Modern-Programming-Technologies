# -*- coding: utf-8 -*-
"""
Собирает приложение с ключами к тестовым заданиям из файлов keys/chNN.json.

    python genkeys.py

Формат keys/chNN.json:
    {"chapter": 4, "keys": [{"n": 1, "answer": "б"}, ...]}
"""
import glob
import io
import json
import os
import sys

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
KEYS_DIR = os.path.join(HERE, 'keys')
OUT = os.path.join(HERE, 'back', 'app_keys.tex')

HEAD = r"""% ============================================================
%  СГЕНЕРИРОВАНО скриптом genkeys.py — не править вручную.
%  Источник: posobie/keys/chNN.json
% ============================================================
\chapter{Ответы на тестовые задания}
\label{app:keys}

Проверяйте себя только после того, как ответили на все вопросы главы.
Если ответ не совпал, вернитесь к соответствующему разделу~--- номер вопроса
обычно подсказывает, о каком именно разделе идёт речь.

"""

TAIL = ""


def main():
    files = sorted(glob.glob(os.path.join(KEYS_DIR, 'ch*.json')))
    if not files:
        print('НЕТ ФАЙЛОВ КЛЮЧЕЙ в %s' % KEYS_DIR)
        # всё равно создаём заглушку, чтобы документ собирался
        io.open(OUT, 'w', encoding='utf-8', newline='\n').write(
            HEAD + '\n\\textit{Ключи будут добавлены после готовности глав.}\n')
        return 1

    parts = [HEAD]
    total = 0
    for f in files:
        data = json.load(io.open(f, encoding='utf-8'))
        ch = data['chapter']
        keys = data['keys']
        total += len(keys)
        parts.append('\\section*{Глава %d}\n' % ch)
        parts.append('\\addcontentsline{toc}{section}{Глава %d}\n\n' % ch)
        # компактная таблица: номер вопроса -> буква ответа
        parts.append('\\noindent\n\\begin{tabular}{')
        parts.append('c' * len(keys))
        parts.append('}\n\\toprule\n')
        parts.append(' & '.join(str(k['n']) for k in keys) + r' \\' + '\n')
        parts.append('\\midrule\n')
        parts.append(' & '.join(k['answer'] for k in keys) + r' \\' + '\n')
        parts.append('\\bottomrule\n\\end{tabular}\n\n\\vspace{4mm}\n\n')

    parts.append(TAIL)
    io.open(OUT, 'w', encoding='utf-8', newline='\n').write(''.join(parts))
    print('OK: %s' % OUT)
    print('глав: %d, ключей всего: %d' % (len(files), total))
    for f in files:
        d = json.load(io.open(f, encoding='utf-8'))
        print('   глава %2d: %d ключей' % (d['chapter'], len(d['keys'])))
    return 0


if __name__ == '__main__':
    sys.exit(main())
