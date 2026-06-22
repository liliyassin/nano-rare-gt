"""
Regenerate all match PDFs in output/pdfs/ from the current output/match_*.md files.
- Strips emoji from markdown before conversion (xelatex can't render them)
- Uses pandoc + xelatex
"""

import re
import subprocess
import tempfile
from pathlib import Path

OUTPUT_MD  = Path("output")
OUTPUT_PDF = Path("output/pdfs")
OUTPUT_PDF.mkdir(parents=True, exist_ok=True)

# Remove emoji and other non-Latin characters pandoc/xelatex chokes on
EMOJI_RE = re.compile(
    "["
    "\U0001F300-\U0001F9FF"   # misc symbols and pictographs
    "\U00002600-\U000027BF"   # misc symbols
    "\U0001F7C0-\U0001F7FF"   # geometric shapes extended
    "]+",
    flags=re.UNICODE,
)

def strip_emoji(text: str) -> str:
    return EMOJI_RE.sub("", text)

PANDOC_OPTS = [
    "--pdf-engine=xelatex",
    "-V", "geometry:margin=2cm",
    "-V", "fontsize=10pt",
    "-V", "mainfont=DejaVu Serif",
    "-V", "colorlinks=true",
    "--highlight-style=kate",
]

md_files = sorted(OUTPUT_MD.glob("match_*.md"))
print(f"Found {len(md_files)} match files.\n")

ok = 0
fail = 0
for md in md_files:
    out_pdf = OUTPUT_PDF / md.with_suffix(".pdf").name
    # Strip emoji and write to a temp file
    clean = strip_emoji(md.read_text())
    with tempfile.NamedTemporaryFile(suffix=".md", mode="w", delete=False) as tmp:
        tmp.write(clean)
        tmp_path = tmp.name

    result = subprocess.run(
        ["pandoc", tmp_path, "-o", str(out_pdf)] + PANDOC_OPTS,
        capture_output=True, text=True
    )
    Path(tmp_path).unlink(missing_ok=True)

    if result.returncode == 0:
        print(f"  ✓ {out_pdf.name}")
        ok += 1
    else:
        print(f"  ✗ {md.name}")
        print(result.stderr[-300:] if result.stderr else "  (no stderr)")
        fail += 1

print(f"\nDone: {ok} OK, {fail} failed.")
