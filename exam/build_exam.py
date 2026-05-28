"""Build standalone exam.html and docsify-friendly exam.md from template + encrypted blob.

Reads:
    exam/template.html
    exam/pool.enc.txt

Writes:
    exam.html                (standalone, project root)
    exam.md                  (docsify-friendly, project root)
"""
from __future__ import annotations
import io
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "exam" / "template.html"
BLOB = ROOT / "exam" / "pool.enc.txt"
OUT_HTML = ROOT / "exam.html"
OUT_MD = ROOT / "exam.md"

PLACEHOLDER = "{{ENCRYPTED_POOL}}"


def build() -> None:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

    if not TEMPLATE.exists():
        sys.stderr.write(f"Missing {TEMPLATE}\n")
        sys.exit(1)
    if not BLOB.exists():
        sys.stderr.write(
            f"Missing {BLOB}. Run `python exam/encrypt_pool.py` first.\n"
        )
        sys.exit(1)

    template = TEMPLATE.read_text(encoding="utf-8")
    blob = BLOB.read_text(encoding="ascii").strip()

    if PLACEHOLDER not in template:
        sys.stderr.write(f"Placeholder {PLACEHOLDER!r} not found in template\n")
        sys.exit(1)

    html = template.replace(PLACEHOLDER, blob)
    OUT_HTML.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT_HTML} ({len(html):,} bytes)")

    # ----- docsify version -----
    # Embed the standalone exam.html via <iframe src="..."> for isolation.
    # Docsify serves static files alongside markdown, so a relative src works.
    md = """# Итоговый тест: лекции 1–6

> 60 вопросов, 40 минут. Перед началом подготовьте имя, фамилию и пароль доступа (выдаёт преподаватель).

<p style="text-align:center;margin:16px 0;">
  <a href="exam.html" target="_blank" rel="noopener"
     style="display:inline-block;padding:10px 20px;background:#3F51B5;color:#fff;
            text-decoration:none;border-radius:6px;font-weight:500;">
    Открыть тест в отдельной вкладке
  </a>
</p>

<iframe src="exam.html"
        style="width:100%;height:80vh;border:1px solid #e5e7eb;border-radius:8px;"
        title="Итоговый тест">
</iframe>
"""
    OUT_MD.write_text(md, encoding="utf-8")
    print(f"Wrote {OUT_MD} ({len(md):,} bytes)")


if __name__ == "__main__":
    build()
