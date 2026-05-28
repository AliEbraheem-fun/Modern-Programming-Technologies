"""Parse quiz1..quiz6 markdown files and produce a unified JSON pool of questions.

Filters out questions whose body mentions specific Java versions or release dates.
Run from project root: python exam/build_pool.py
"""
from __future__ import annotations
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent / "pool.json"

QUIZ_FILES = [
    "quiz1.md",
    "quiz2-1.md",
    "quiz2-2.md",
    "quiz3.md",
    "quiz4.md",
    "quiz5.md",
    "quiz6.md",
]

# A question is excluded if its full text (question + options) matches ANY of these.
EXCLUDE_PATTERNS = [
    re.compile(r"\bJava\s*\d+\b", re.IGNORECASE),
    re.compile(r"\b(JDK|JRE|JVM)\s*\d+\b", re.IGNORECASE),
    re.compile(r"когда\s+(был|была|были)\s+(выпущ|релиз|представл)", re.IGNORECASE),
    re.compile(r"\bв\s+каком\s+году\b", re.IGNORECASE),
    re.compile(r"\bв\s+какой\s+версии\b", re.IGNORECASE),
    re.compile(r"\b(год|года|году)\s+(выхода|релиза)\b", re.IGNORECASE),
    re.compile(r"\bLTS-?версия\b", re.IGNORECASE),
    re.compile(r"\bтекущ(ая|ей|их)\s+LTS\b", re.IGNORECASE),
    re.compile(r"\bкакая\s+версия\b", re.IGNORECASE),
    re.compile(r"\b(stable|релиз|выпуск)\s+\d{4}\b", re.IGNORECASE),
    re.compile(r"\b20[12]\d\b"),  # raw years 2010-2029 in question body
]

# Match each question block.
# The structure is:
# <div class="quiz-question" data-correct="N">
# <h4>Текст вопроса</h4>
# ...code blocks and other content...
# <div class="quiz-option" data-index="0">текст</div>
# <div class="quiz-option" data-index="1">текст</div>
# ...
# <div class="quiz-feedback"></div>
# </div>

QUESTION_RE = re.compile(
    r'<div class="quiz-question"\s+data-correct="(?P<correct>\d+)">\s*'
    r'(?P<body>.+?)'
    r'<div class="quiz-feedback">',
    re.DOTALL,
)

H4_RE = re.compile(r'<h4>(?P<text>.+?)</h4>', re.DOTALL)
OPTION_RE = re.compile(
    r'<div class="quiz-option"\s+data-index="(?P<idx>\d+)">(?P<text>.+?)</div>',
    re.DOTALL,
)
JSHELL_HINT_RE = re.compile(r'<span class="jshell-hint">.*?</span>', re.DOTALL)
TAG_RE = re.compile(r'<[^>]+>')
QUESTION_PREFIX_RE = re.compile(r'^Вопрос\s+\d+\.\s*', re.IGNORECASE)


def clean_text(s: str) -> str:
    s = JSHELL_HINT_RE.sub('', s)
    s = TAG_RE.sub('', s)
    s = s.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
    s = s.replace('&laquo;', '«').replace('&raquo;', '»').replace('&nbsp;', ' ')
    return s.strip()


def strip_question_prefix(s: str) -> str:
    return QUESTION_PREFIX_RE.sub('', s, count=1).strip()


def extract_code_blocks(body: str) -> str:
    """Extract fenced code blocks from question body (they sit between h4 and first option)."""
    # Pull text between </h4> and first <div class="quiz-option"
    m = re.search(r'</h4>(?P<between>.+?)<div class="quiz-option"', body, re.DOTALL)
    if not m:
        return ''
    between = m.group('between').strip()
    # Keep fenced code blocks verbatim
    code_blocks = re.findall(r'```\w*\n.*?\n```', between, re.DOTALL)
    return '\n\n'.join(cb.strip() for cb in code_blocks)


def parse_quiz(path: Path) -> list[dict]:
    text = path.read_text(encoding='utf-8')
    questions = []
    for m in QUESTION_RE.finditer(text):
        correct = int(m.group('correct'))
        body = m.group('body')

        h4 = H4_RE.search(body)
        if not h4:
            continue
        question_text = strip_question_prefix(clean_text(h4.group('text')))

        code = extract_code_blocks(body)

        options = []
        for om in OPTION_RE.finditer(body):
            options.append({
                'idx': int(om.group('idx')),
                'text': clean_text(om.group('text')),
            })
        options.sort(key=lambda x: x['idx'])
        option_texts = [o['text'] for o in options]

        if len(option_texts) < 2 or correct >= len(option_texts):
            continue

        questions.append({
            'source': path.name,
            'question': question_text,
            'code': code,
            'options': option_texts,
            'correct': correct,
        })
    return questions


def is_excluded(q: dict) -> tuple[bool, str]:
    haystack = q['question'] + '\n' + q['code'] + '\n' + '\n'.join(q['options'])
    for pat in EXCLUDE_PATTERNS:
        m = pat.search(haystack)
        if m:
            return True, f"matched /{pat.pattern}/ -> {m.group(0)!r}"
    return False, ''


def main() -> int:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    pool: list[dict] = []
    skipped: list[tuple[str, str, str]] = []  # (source, question, reason)
    per_source_kept: dict[str, int] = {}
    per_source_skipped: dict[str, int] = {}

    for name in QUIZ_FILES:
        path = ROOT / name
        if not path.exists():
            print(f"[warn] missing {name}", file=sys.stderr)
            continue
        qs = parse_quiz(path)
        for q in qs:
            excluded, reason = is_excluded(q)
            if excluded:
                skipped.append((name, q['question'][:80], reason))
                per_source_skipped[name] = per_source_skipped.get(name, 0) + 1
            else:
                pool.append(q)
                per_source_kept[name] = per_source_kept.get(name, 0) + 1

    # Strip the 'source' field before writing
    out_pool = [
        {
            'q': item['question'],
            'code': item['code'],
            'options': item['options'],
            'correct': item['correct'],
        }
        for item in pool
    ]
    OUT.write_text(json.dumps(out_pool, ensure_ascii=False, indent=2), encoding='utf-8')

    print(f"Wrote {len(out_pool)} questions to {OUT}")
    print("\nPer-source counts:")
    for name in QUIZ_FILES:
        kept = per_source_kept.get(name, 0)
        skip = per_source_skipped.get(name, 0)
        print(f"  {name}: kept {kept}, skipped {skip}")

    if skipped:
        print(f"\nSkipped {len(skipped)} questions (first 20):")
        for src, q, reason in skipped[:20]:
            print(f"  [{src}] {reason}")
            print(f"    {q!r}")

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
