from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from models.exam import Exam
import os

OUTPUT_FOLDER = "output"

if not os.path.exists(OUTPUT_FOLDER):
    os.mkdir(OUTPUT_FOLDER)


def create_pdf(filename: str, exam: Exam):
    output_path = f"{OUTPUT_FOLDER}/{filename}.pdf"
    c = canvas.Canvas(output_path, pagesize=letter)
    c.drawString(100, 750, exam.title)
    for i, question in enumerate(exam.questions):
        c.drawString(100, 735 - i * 20, f"{i + 1}. {question.text}")
        c.drawString(100, 720 - i * 20, f"Answer: {question.answer}")
    c.save()
