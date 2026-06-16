from __future__ import annotations

from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).parent
PDF_ROOT = ROOT / "Reading Literature" / "files"
TEXT_ROOT = ROOT / "Reading Literature" / "text"


def slug_for(path: Path) -> str:
    stem = path.stem.lower()
    keep = []
    previous_dash = False
    for char in stem:
        if char.isalnum():
            keep.append(char)
            previous_dash = False
        elif not previous_dash:
            keep.append("-")
            previous_dash = True
    return "".join(keep).strip("-")[:120]


def extract_pdf(path: Path) -> str:
    reader = PdfReader(path)
    chunks = [f"# Source PDF: {path.relative_to(ROOT)}", ""]
    for index, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ""
        chunks.append(f"\n\n--- Page {index} ---\n")
        chunks.append(text)
    return "\n".join(chunks)


def main() -> None:
    TEXT_ROOT.mkdir(parents=True, exist_ok=True)
    pdfs = sorted(PDF_ROOT.glob("*/*.pdf"))
    if not pdfs:
        raise SystemExit(f"No PDFs found under {PDF_ROOT}")

    for pdf in pdfs:
        output = TEXT_ROOT / f"{slug_for(pdf)}.txt"
        output.write_text(extract_pdf(pdf), encoding="utf-8")
        print(f"{pdf.name} -> {output.relative_to(ROOT)}")

    print(f"\nExtracted {len(pdfs)} PDFs to {TEXT_ROOT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
