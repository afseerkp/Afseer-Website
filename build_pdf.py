"""Build the PDF version of the CV from the same content source.

Text is drawn as real selectable text (not an image) so ATS parsers can read it.
"""
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (BaseDocTemplate, Flowable, Frame, KeepTogether,
                                PageTemplate, Paragraph, Spacer)

import cv_content as C

DARK = HexColor("#1A1A1A")
ACCENT = HexColor("#003366")
BODY = 9.6
LEAD = 11.8

styles = {
    "name": ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=19, leading=22,
                           alignment=TA_CENTER, textColor=ACCENT, spaceAfter=2),
    "headline": ParagraphStyle("headline", fontName="Helvetica-Bold", fontSize=9.5, leading=12,
                               alignment=TA_CENTER, textColor=DARK, spaceAfter=2),
    "contact": ParagraphStyle("contact", fontName="Helvetica", fontSize=9, leading=11,
                              alignment=TA_CENTER, textColor=DARK),
    "heading": ParagraphStyle("heading", fontName="Helvetica-Bold", fontSize=10.5, leading=12,
                              textColor=ACCENT, spaceBefore=6.5, spaceAfter=1),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=BODY, leading=LEAD,
                           textColor=DARK, alignment=TA_LEFT),
    "company": ParagraphStyle("company", fontName="Helvetica", fontSize=BODY, leading=LEAD + 1,
                              textColor=DARK, spaceBefore=6),
    "role": ParagraphStyle("role", fontName="Helvetica-Oblique", fontSize=BODY, leading=LEAD,
                           textColor=DARK, spaceAfter=2),
    "bullet": ParagraphStyle("bullet", fontName="Helvetica", fontSize=BODY, leading=LEAD,
                             textColor=DARK, alignment=TA_LEFT,
                             leftIndent=9, firstLineIndent=-9, spaceAfter=1),
}


class Rule(Flowable):
    """Thin accent rule used under each section heading."""

    def __init__(self, width, thickness=0.6, space_after=3):
        Flowable.__init__(self)
        self.width = width
        self.thickness = thickness
        self.height = thickness + space_after

    def draw(self):
        self.canv.setStrokeColor(ACCENT)
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, self.height, self.width, self.height)


PAGE_W, PAGE_H = A4
MARGIN_X = 15 * mm
MARGIN_Y = 12 * mm
FRAME_W = PAGE_W - 2 * MARGIN_X

story = []


def heading(text):
    story.append(KeepTogether([Paragraph(text.upper(), styles["heading"]),
                               Rule(FRAME_W)]))


def bullet(text):
    story.append(Paragraph("\u2022&nbsp;&nbsp;" + text, styles["bullet"]))


story.append(Paragraph(C.NAME, styles["name"]))
story.append(Paragraph(C.HEADLINE.replace("|", "&nbsp;|&nbsp;"), styles["headline"]))
story.append(Paragraph(C.CONTACT.replace("|", "&nbsp;|&nbsp;"), styles["contact"]))

heading("Professional Summary")
story.append(Paragraph(C.SUMMARY, styles["body"]))

heading("Core Competencies")
story.append(Paragraph("&nbsp;&nbsp;\u2022&nbsp;&nbsp;".join(C.COMPETENCIES), styles["body"]))

heading("Technical Skills")
for label, detail in C.SKILLS:
    story.append(Paragraph(f"<b>{label}:</b> {detail}", styles["body"]))
    story.append(Spacer(1, 2))

heading("Professional Experience")
for job in C.EXPERIENCE:
    role = f"<b>{job['title']}</b>&nbsp;&nbsp;|&nbsp;&nbsp;{job['dates']}"
    if job["note"]:
        role += f" ({job['note']})"
    block = [
        Paragraph(f"<b>{job['company']}</b>&nbsp;&nbsp;\u2013&nbsp;&nbsp;{job['location']}",
                  styles["company"]),
        Paragraph(role, styles["role"]),
        Paragraph("\u2022&nbsp;&nbsp;" + job["bullets"][0], styles["bullet"]),
    ]
    story.append(KeepTogether(block))
    for b in job["bullets"][1:]:
        bullet(b)

heading("Certifications")
for c in C.CERTIFICATIONS:
    bullet(c)

heading("Education")
for e in C.EDUCATION:
    bullet(e)

heading("Languages")
story.append(Paragraph(C.LANGUAGES.replace("|", "&nbsp;|&nbsp;"), styles["body"]))

OUT = "/Users/afseer/CV/Afseer KP - IT Team Lead CV.pdf"
doc = BaseDocTemplate(OUT, pagesize=A4,
                      leftMargin=MARGIN_X, rightMargin=MARGIN_X,
                      topMargin=MARGIN_Y, bottomMargin=MARGIN_Y,
                      title=f"{C.NAME} - CV", author=C.NAME,
                      subject="Curriculum Vitae")
frame = Frame(MARGIN_X, MARGIN_Y, FRAME_W, PAGE_H - 2 * MARGIN_Y, id="body",
              leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
doc.addPageTemplates([PageTemplate(id="cv", frames=[frame])])
doc.build(story)
print("wrote", OUT, "-", doc.page, "page(s)")
