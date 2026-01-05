from docx import Document
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def export_docx(text, filename):
    doc = Document()
    for line in text.split("\n"):
        doc.add_paragraph(line)
    doc.save(filename)

def export_pdf(text, filename):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    y = height - 40

    for line in text.split("\n"):
        c.drawString(40, y, line)
        y -= 14
        if y < 40:
            c.showPage()
            y = height - 40

    c.save()