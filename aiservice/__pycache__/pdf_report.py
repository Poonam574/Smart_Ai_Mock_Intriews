from reportlab.pdfgen import canvas
import os
from datetime import datetime

def save_pdf(questions, answers):

    # create results folder if not exists
    os.makedirs("results", exist_ok=True)

    filename = f"results/interview_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

    pdf = canvas.Canvas(filename)

    y = 800

    pdf.drawString(200,820,"AI Mock Interview Result")

    for i in range(len(questions)):

        pdf.drawString(50,y,"Q: " + questions[i])
        y -= 25

        pdf.drawString(70,y,"A: " + answers[i])
        y -= 40

    pdf.save()

    print("PDF Saved:", filename)