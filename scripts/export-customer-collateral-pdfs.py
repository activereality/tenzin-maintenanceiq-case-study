from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable

from PIL import Image as PilImage
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    Frame,
    Image,
    KeepTogether,
    LongTable,
    PageBreak,
    PageTemplate,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
    BaseDocTemplate,
)
from reportlab.platypus.doctemplate import LayoutError
from xml.sax.saxutils import escape

REPO_ROOT = Path(__file__).resolve().parents[1]
CUSTOMER_DIR = REPO_ROOT / "docs" / "customer-facing"
PDF_DIR = CUSTOMER_DIR / "pdf"
DIAGRAM_DIR = REPO_ROOT / "assets" / "diagrams"

ONE_PAGE_MD = CUSTOMER_DIR / "tenzin-one-page-overview.md"
PACKET_MDS = [
    CUSTOMER_DIR / "pilot-discovery-questions.md",
    CUSTOMER_DIR / "demo-script.md",
    CUSTOMER_DIR / "pilot-success-criteria.md",
]

ONE_PAGE_PDF = PDF_DIR / "tenzin-maintenanceiq-one-page-overview.pdf"
PACKET_PDF = PDF_DIR / "tenzin-maintenanceiq-pilot-collateral-packet.pdf"
SYSTEM_OVERVIEW = DIAGRAM_DIR / "tenzin-maintenanceiq-system-overview.png"

PAGE_WIDTH, PAGE_HEIGHT = letter
BRAND = colors.HexColor("#17324D")
ACCENT = colors.HexColor("#2F6F7E")
LIGHT_BLUE = colors.HexColor("#EDF6FA")
LIGHT_GREEN = colors.HexColor("#EEF7F0")
LIGHT_GOLD = colors.HexColor("#FFF7E6")
TEXT = colors.HexColor("#17202A")
MUTED = colors.HexColor("#52616B")
BORDER = colors.HexColor("#B7C6D6")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="TenzinTitle",
    parent=styles["Title"],
    fontName="Helvetica-Bold",
    fontSize=19,
    leading=22,
    textColor=BRAND,
    spaceAfter=6,
    alignment=TA_LEFT,
))
styles.add(ParagraphStyle(
    name="TenzinSubtitle",
    parent=styles["BodyText"],
    fontName="Helvetica",
    fontSize=9.6,
    leading=12.2,
    textColor=TEXT,
    spaceAfter=7,
))
styles.add(ParagraphStyle(
    name="SectionHeading",
    parent=styles["Heading2"],
    fontName="Helvetica-Bold",
    fontSize=10.2,
    leading=12,
    textColor=BRAND,
    spaceBefore=0,
    spaceAfter=3,
))
styles.add(ParagraphStyle(
    name="BodySmall",
    parent=styles["BodyText"],
    fontName="Helvetica",
    fontSize=7.45,
    leading=9.0,
    textColor=TEXT,
    spaceAfter=3,
))
styles.add(ParagraphStyle(
    name="BulletSmall",
    parent=styles["BodySmall"],
    leftIndent=8,
    firstLineIndent=-6,
    bulletIndent=0,
    spaceAfter=1.5,
))
styles.add(ParagraphStyle(
    name="MutedSmall",
    parent=styles["BodySmall"],
    fontSize=6.9,
    leading=8.2,
    textColor=MUTED,
))
styles.add(ParagraphStyle(
    name="PacketTitle",
    parent=styles["Title"],
    fontName="Helvetica-Bold",
    fontSize=24,
    leading=29,
    textColor=BRAND,
    alignment=TA_CENTER,
    spaceAfter=14,
))
styles.add(ParagraphStyle(
    name="PacketSubtitle",
    parent=styles["BodyText"],
    fontName="Helvetica",
    fontSize=11,
    leading=15,
    textColor=TEXT,
    alignment=TA_CENTER,
    spaceAfter=8,
))
styles.add(ParagraphStyle(
    name="PacketH1",
    parent=styles["Heading1"],
    fontName="Helvetica-Bold",
    fontSize=18,
    leading=22,
    textColor=BRAND,
    spaceBefore=0,
    spaceAfter=8,
))
styles.add(ParagraphStyle(
    name="PacketH2",
    parent=styles["Heading2"],
    fontName="Helvetica-Bold",
    fontSize=12.5,
    leading=15,
    textColor=BRAND,
    spaceBefore=10,
    spaceAfter=4,
))
styles.add(ParagraphStyle(
    name="PacketBody",
    parent=styles["BodyText"],
    fontName="Helvetica",
    fontSize=9.2,
    leading=12.2,
    textColor=TEXT,
    spaceAfter=5,
))
styles.add(ParagraphStyle(
    name="PacketBullet",
    parent=styles["PacketBody"],
    leftIndent=14,
    firstLineIndent=-9,
    bulletIndent=2,
    spaceAfter=3,
))
styles.add(ParagraphStyle(
    name="TableHead",
    parent=styles["PacketBody"],
    fontName="Helvetica-Bold",
    fontSize=8.0,
    leading=10,
    textColor=colors.white,
))
styles.add(ParagraphStyle(
    name="TableCell",
    parent=styles["PacketBody"],
    fontSize=7.5,
    leading=9.1,
    spaceAfter=0,
))


def clean_inline(text: str) -> str:
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", text)
    text = text.replace("**", "")
    text = text.replace("`", "")
    return text.strip()


def para(text: str, style_name: str = "PacketBody", **kwargs) -> Paragraph:
    return Paragraph(escape(clean_inline(text)), styles[style_name], **kwargs)


def bullet(text: str, style_name: str = "PacketBullet") -> Paragraph:
    return Paragraph(escape(clean_inline(text)), styles[style_name], bulletText="-")


def numbered(text: str, number: int, style_name: str = "PacketBullet") -> Paragraph:
    return Paragraph(escape(clean_inline(text)), styles[style_name], bulletText=f"{number}.")


def read_sections(markdown_path: Path) -> tuple[str, str, dict[str, list[str]]]:
    lines = markdown_path.read_text(encoding="utf-8").splitlines()
    title = ""
    intro_lines: list[str] = []
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        if line.startswith("# "):
            title = clean_inline(line[2:])
            continue
        if line.startswith("## "):
            current = clean_inline(line[3:])
            sections[current] = []
            continue
        if line.startswith("!["):
            continue
        if current is None:
            intro_lines.append(line)
        else:
            sections[current].append(line)
    return title, " ".join(clean_inline(x) for x in intro_lines), sections


def split_section(lines: Iterable[str]) -> tuple[list[str], list[str], list[str]]:
    paragraphs: list[str] = []
    bullets: list[str] = []
    numbers: list[str] = []
    for line in lines:
        if line.startswith("- "):
            bullets.append(line[2:])
        elif re.match(r"^\d+\.\s+", line):
            numbers.append(re.sub(r"^\d+\.\s+", "", line))
        else:
            paragraphs.append(line)
    return paragraphs, bullets, numbers


def section_block(title: str, lines: list[str], fill_color=colors.white, compact: bool = True) -> list:
    body_style = "BodySmall" if compact else "PacketBody"
    bullet_style = "BulletSmall" if compact else "PacketBullet"
    block = [Paragraph(escape(title), styles["SectionHeading"])]
    paragraphs, bullets, numbers = split_section(lines)
    for text in paragraphs:
        block.append(para(text, body_style))
    for item in bullets:
        block.append(bullet(item, bullet_style))
    for idx, item in enumerate(numbers, start=1):
        block.append(numbered(item, idx, bullet_style))
    return block


def scale_image(path: Path, max_width: float, max_height: float) -> Image:
    with PilImage.open(path) as image:
        width, height = image.size
    scale = min(max_width / width, max_height / height)
    return Image(str(path), width * scale, height * scale)


def build_one_page_pdf() -> None:
    title, intro, sections = read_sections(ONE_PAGE_MD)
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(ONE_PAGE_PDF),
        pagesize=letter,
        leftMargin=0.38 * inch,
        rightMargin=0.38 * inch,
        topMargin=0.34 * inch,
        bottomMargin=0.32 * inch,
        title="Tenzin MaintenanceIQ Customer Overview",
        author="Tenzin MaintenanceIQ",
    )

    image = scale_image(SYSTEM_OVERVIEW, 3.05 * inch, 3.05 * inch)
    left = [image, Spacer(1, 4), para("Diagram: how Tenzin connects facility users, asset knowledge, trusted retrieval, citations, and source opening.", "MutedSmall")]
    right = []
    for heading in ["The Problem", "What Tenzin MaintenanceIQ Does", "How It Works"]:
        right.extend(section_block(heading, sections.get(heading, []), compact=True))
        right.append(Spacer(1, 2))

    top_table = Table(
        [[left, right]],
        colWidths=[3.25 * inch, 3.85 * inch],
        hAlign="LEFT",
    )
    top_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("BOX", (0, 0), (-1, -1), 0.6, BORDER),
        ("BACKGROUND", (0, 0), (0, 0), LIGHT_BLUE),
        ("BACKGROUND", (1, 0), (1, 0), colors.white),
    ]))

    bottom_cells = []
    for heading, color in [
        ("Why Citations Matter", LIGHT_GOLD),
        ("Security And Data Boundaries", LIGHT_GREEN),
        ("Best-Fit Pilot Use Cases", colors.white),
        ("Suggested Pilot Outcome", colors.white),
    ]:
        bottom_cells.append(section_block(heading, sections.get(heading, []), compact=True))

    bottom_table = Table(
        [[bottom_cells[0], bottom_cells[1]], [bottom_cells[2], bottom_cells[3]]],
        colWidths=[3.55 * inch, 3.55 * inch],
        hAlign="LEFT",
    )
    bottom_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("BOX", (0, 0), (-1, -1), 0.5, BORDER),
        ("INNERGRID", (0, 0), (-1, -1), 0.35, BORDER),
        ("BACKGROUND", (0, 0), (0, 0), LIGHT_GOLD),
        ("BACKGROUND", (1, 0), (1, 0), LIGHT_GREEN),
    ]))

    story = [
        Paragraph(escape(title), styles["TenzinTitle"]),
        Paragraph(escape(intro), styles["TenzinSubtitle"]),
        top_table,
        Spacer(1, 7),
        bottom_table,
        Spacer(1, 4),
        para("Reference diagrams in the repo: document ingestion and retrieval flow; account / facility data boundary.", "MutedSmall"),
    ]
    try:
        doc.build(story)
    except LayoutError as exc:
        raise SystemExit(f"Could not fit the one-page overview PDF layout: {exc}")


def parse_markdown(markdown_path: Path) -> list:
    lines = markdown_path.read_text(encoding="utf-8").splitlines()
    story: list = []
    paragraph_lines: list[str] = []
    table_lines: list[str] = []
    list_lines: list[tuple[str, str]] = []

    def flush_paragraph() -> None:
        nonlocal paragraph_lines
        if paragraph_lines:
            story.append(para(" ".join(paragraph_lines), "PacketBody"))
            paragraph_lines = []

    def flush_list() -> None:
        nonlocal list_lines
        if list_lines:
            for kind, text in list_lines:
                if kind == "bullet":
                    story.append(bullet(text))
                else:
                    story.append(numbered(text, int(kind)))
            list_lines = []

    def flush_table() -> None:
        nonlocal table_lines
        if not table_lines:
            return
        rows = []
        for line in table_lines:
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
                continue
            rows.append(cells)
        table_lines = []
        if not rows:
            return
        rendered = []
        for row_index, row in enumerate(rows):
            style = "TableHead" if row_index == 0 else "TableCell"
            rendered.append([Paragraph(escape(clean_inline(cell)), styles[style]) for cell in row])
        table = LongTable(rendered, colWidths=[1.25 * inch, 2.35 * inch, 2.7 * inch], repeatRows=1)
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), BRAND),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("GRID", (0, 0), (-1, -1), 0.35, BORDER),
            ("LEFTPADDING", (0, 0), (-1, -1), 5),
            ("RIGHTPADDING", (0, 0), (-1, -1), 5),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F7FAFC")]),
        ]))
        story.append(table)
        story.append(Spacer(1, 8))

    for raw in lines:
        line = raw.strip()
        if not line:
            flush_paragraph()
            flush_list()
            flush_table()
            story.append(Spacer(1, 3))
            continue
        if line.startswith("|"):
            flush_paragraph()
            flush_list()
            table_lines.append(line)
            continue
        flush_table()
        if line.startswith("# "):
            flush_paragraph()
            flush_list()
            story.append(Paragraph(escape(clean_inline(line[2:])), styles["PacketH1"]))
        elif line.startswith("## "):
            flush_paragraph()
            flush_list()
            story.append(Paragraph(escape(clean_inline(line[3:])), styles["PacketH2"]))
        elif line.startswith("### "):
            flush_paragraph()
            flush_list()
            story.append(Paragraph(escape(clean_inline(line[4:])), styles["PacketH2"]))
        elif line.startswith("- "):
            flush_paragraph()
            list_lines.append(("bullet", line[2:]))
        elif re.match(r"^\d+\.\s+", line):
            flush_paragraph()
            match = re.match(r"^(\d+)\.\s+(.*)$", line)
            assert match is not None
            list_lines.append((match.group(1), match.group(2)))
        elif line.startswith("!["):
            continue
        else:
            paragraph_lines.append(line)
    flush_paragraph()
    flush_list()
    flush_table()
    return story


def packet_footer(canvas, doc) -> None:
    canvas.saveState()
    canvas.setFont("Helvetica", 7.2)
    canvas.setFillColor(MUTED)
    canvas.drawString(0.62 * inch, 0.35 * inch, "Tenzin MaintenanceIQ Pilot Collateral Packet")
    canvas.drawRightString(PAGE_WIDTH - 0.62 * inch, 0.35 * inch, f"Page {doc.page}")
    canvas.restoreState()


def build_packet_pdf() -> None:
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(PACKET_PDF),
        pagesize=letter,
        leftMargin=0.62 * inch,
        rightMargin=0.62 * inch,
        topMargin=0.58 * inch,
        bottomMargin=0.58 * inch,
        title="Tenzin MaintenanceIQ Pilot Collateral Packet",
        author="Tenzin MaintenanceIQ",
    )
    story: list = [
        Spacer(1, 2.15 * inch),
        Paragraph("Tenzin MaintenanceIQ", styles["PacketTitle"]),
        Paragraph("Pilot Collateral Packet", styles["PacketTitle"]),
        Paragraph("Discovery questions, demo flow, and pilot success criteria for practical customer conversations.", styles["PacketSubtitle"]),
        Spacer(1, 0.22 * inch),
        Paragraph("Pilot success criteria are validation goals, not guaranteed outcomes. Tenzin supports maintenance teams without replacing technicians, engineers, OEM manuals, CMMS/EAM systems, or safety procedures.", styles["PacketSubtitle"]),
        PageBreak(),
    ]
    for index, markdown_path in enumerate(PACKET_MDS):
        if index > 0:
            story.append(PageBreak())
        story.extend(parse_markdown(markdown_path))
    doc.build(story, onFirstPage=packet_footer, onLaterPages=packet_footer)


def main() -> None:
    if not SYSTEM_OVERVIEW.exists():
        raise SystemExit(f"Missing diagram asset: {SYSTEM_OVERVIEW}")
    build_one_page_pdf()
    build_packet_pdf()
    print(f"Wrote {ONE_PAGE_PDF.relative_to(REPO_ROOT)}")
    print(f"Wrote {PACKET_PDF.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()