"""
Generate NanoGT_Dissertation_Draft.pdf from paper/ markdown sections.
Uses reportlab Platypus for structured layout.
"""

import re
from pathlib import Path
from datetime import date

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, HRFlowable
)

# ── Output path ───────────────────────────────────────────────────────────────
OUT = Path("NanoGT_Dissertation_Draft.pdf")
PAGE_W, PAGE_H = A4
MARGIN = 2.5 * cm

# ── Styles ────────────────────────────────────────────────────────────────────
styles = getSampleStyleSheet()

def make_style(name, parent="Normal", **kwargs):
    return ParagraphStyle(name, parent=styles[parent], **kwargs)

S = {
    "title":    make_style("NTitle",   "Title",   fontSize=20, leading=26, spaceAfter=6),
    "subtitle": make_style("NSub",     "Normal",  fontSize=11, textColor=colors.grey, spaceAfter=16),
    "h1":       make_style("NH1",      "Heading1",fontSize=14, leading=18, spaceBefore=14, spaceAfter=6),
    "h2":       make_style("NH2",      "Heading2",fontSize=11, leading=15, spaceBefore=10, spaceAfter=4),
    "body":     make_style("NBody",    "Normal",  fontSize=10, leading=14, spaceAfter=6),
    "bullet":   make_style("NBul",     "Normal",  fontSize=10, leading=13, leftIndent=16, spaceAfter=3),
    "code":     make_style("NCode",    "Code",    fontSize=8,  leading=11, leftIndent=12, fontName="Courier"),
    "caption":  make_style("NCap",     "Normal",  fontSize=9,  leading=12, textColor=colors.grey, spaceAfter=8),
    "ref":      make_style("NRef",     "Normal",  fontSize=9,  leading=12, leftIndent=12, spaceAfter=3),
}


def esc(text):
    """Escape XML special chars for ReportLab Paragraph."""
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return text


def md_inline(text):
    """Convert **bold**, *italic*, `code` to ReportLab XML."""
    text = esc(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\*(.+?)\*",     r"<i>\1</i>",  text)
    text = re.sub(r"`(.+?)`",       r"<font name='Courier'>\1</font>", text)
    return text


def parse_markdown(md_text, section_title=None):
    """Convert markdown to a list of reportlab flowables."""
    story = []
    if section_title:
        story.append(Paragraph(esc(section_title), S["h1"]))
        story.append(HRFlowable(width="100%", thickness=0.5, color=colors.lightgrey, spaceAfter=6))

    lines = md_text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()

        # Skip blank
        if not line.strip():
            i += 1
            continue

        # H1
        if line.startswith("# "):
            text = line[2:].strip()
            if not section_title:  # only if we haven't already added the section title
                story.append(Paragraph(esc(text), S["h1"]))
                story.append(HRFlowable(width="100%", thickness=0.5, color=colors.lightgrey, spaceAfter=6))
            i += 1
            continue

        # H2
        if line.startswith("## "):
            story.append(Paragraph(md_inline(line[3:].strip()), S["h2"]))
            i += 1
            continue

        # H3
        if line.startswith("### "):
            story.append(Paragraph(f"<b>{md_inline(line[4:].strip())}</b>", S["body"]))
            i += 1
            continue

        # Markdown table
        if line.startswith("|") and i + 1 < len(lines) and lines[i+1].startswith("|---"):
            table_lines = []
            while i < len(lines) and lines[i].startswith("|"):
                if not re.match(r"^\|[-| :]+\|$", lines[i]):
                    row = [c.strip() for c in lines[i].split("|")[1:-1]]
                    table_lines.append(row)
                i += 1
            if table_lines:
                # Determine col widths
                ncols = len(table_lines[0])
                avail = PAGE_W - 2 * MARGIN
                col_w = [avail / ncols] * ncols
                t = Table(table_lines, colWidths=col_w, repeatRows=1)
                t.setStyle(TableStyle([
                    ("BACKGROUND",  (0, 0), (-1, 0), colors.HexColor("#2d6a4f")),
                    ("TEXTCOLOR",   (0, 0), (-1, 0), colors.white),
                    ("FONTSIZE",    (0, 0), (-1, -1), 7),
                    ("FONTNAME",    (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f0f4f0")]),
                    ("GRID",        (0, 0), (-1, -1), 0.25, colors.lightgrey),
                    ("VALIGN",      (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 4),
                    ("RIGHTPADDING",(0, 0), (-1, -1), 4),
                    ("TOPPADDING",  (0, 0), (-1, -1), 3),
                    ("BOTTOMPADDING",(0, 0), (-1, -1), 3),
                ]))
                story.append(t)
                story.append(Spacer(1, 6))
            continue

        # Bullet
        if line.startswith("- ") or line.startswith("* "):
            story.append(Paragraph(f"• {md_inline(line[2:].strip())}", S["bullet"]))
            i += 1
            continue

        # Numbered list
        if re.match(r"^\d+\.\s", line):
            text = re.sub(r"^\d+\.\s", "", line)
            story.append(Paragraph(f"• {md_inline(text.strip())}", S["bullet"]))
            i += 1
            continue

        # Code block
        if line.startswith("```"):
            i += 1
            code_lines = []
            while i < len(lines) and not lines[i].startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1  # skip closing ```
            for cl in code_lines:
                story.append(Paragraph(esc(cl) or " ", S["code"]))
            story.append(Spacer(1, 4))
            continue

        # Horizontal rule
        if line.strip() in ("---", "***", "___"):
            story.append(HRFlowable(width="100%", thickness=0.5, color=colors.lightgrey, spaceAfter=4))
            i += 1
            continue

        # Normal paragraph
        story.append(Paragraph(md_inline(line.strip()), S["body"]))
        i += 1

    return story


# ── Section files ─────────────────────────────────────────────────────────────
PAPER = Path("paper")
SECTIONS = [
    ("abstract.md",     "Abstract"),
    ("introduction.md", "Introduction"),
    ("methods.md",      "Methods"),
    ("results.md",      "Results"),
    ("discussion.md",   "Discussion"),
    ("references.md",   "References"),
]


# ── Page template with header/footer ─────────────────────────────────────────
def on_page(canvas, doc):
    canvas.saveState()
    # Header
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.grey)
    canvas.drawString(MARGIN, PAGE_H - 1.5 * cm, "NanoGT Dissertation Draft")
    canvas.drawRightString(PAGE_W - MARGIN, PAGE_H - 1.5 * cm, f"Generated {date.today():%d %B %Y}")
    canvas.line(MARGIN, PAGE_H - 1.7 * cm, PAGE_W - MARGIN, PAGE_H - 1.7 * cm)
    # Footer
    canvas.drawCentredString(PAGE_W / 2, 1.2 * cm, f"Page {doc.page}")
    canvas.restoreState()


# ── Build PDF ─────────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    str(OUT),
    pagesize=A4,
    leftMargin=MARGIN, rightMargin=MARGIN,
    topMargin=2.5 * cm, bottomMargin=2.5 * cm,
)

story = []

# Cover
story.append(Spacer(1, 3 * cm))
story.append(Paragraph("NanoGT", S["title"]))
story.append(Paragraph(
    "A Computational Framework for Mapping Monogenic Rare Diseases<br/>"
    "to Gene-Therapy Development Precedents",
    S["subtitle"]
))
story.append(Spacer(1, 0.5 * cm))
story.append(Paragraph(f"<b>Dissertation Draft</b> — Generated {date.today():%d %B %Y}", S["body"]))
story.append(Paragraph("Imperial College London", S["body"]))
story.append(Spacer(1, 1 * cm))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#2d6a4f"), spaceAfter=12))
story.append(Paragraph(
    "<b>40-disease proof-of-concept cohort</b> · 14-dimension heuristic scoring (v2) · "
    "39 diseases with ranked precedents · 1 packaging hard-fail (NF1)",
    S["caption"]
))
story.append(PageBreak())

# Sections
for filename, title in SECTIONS:
    path = PAPER / filename
    if not path.exists():
        continue
    text = path.read_text()
    story += parse_markdown(text, section_title=title)
    story.append(PageBreak())

doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print(f"Saved {OUT}  ({OUT.stat().st_size // 1024} KB)")
