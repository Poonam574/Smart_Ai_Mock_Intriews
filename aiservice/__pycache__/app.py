from flask import Flask, render_template, request, redirect, session
from reportlab.pdfgen import canvas
import os
import threading

from proctor import start_camera

app = Flask(__name__)
app.secret_key = "secret123"

questions = [
"Tell me about yourself",
"What is Java?",
"What is OOP?",
"What is Spring Boot?"
]

# LOGIN PAGE
@app.route("/")
def login_page():
    return render_template("login.html")


# LOGIN CHECK
@app.route("/login", methods=["POST"])
def login():

    username = request.form.get("username")
    password = request.form.get("password")

    # simple login check
    if username == "admin" and password == "1234":
        session["user"] = username
        return redirect("/interview")

    return "❌ Invalid Login"


# INTERVIEW PAGE (YOUR EXISTING PAGE)
@app.route("/interview")
def interview():

    if "user" not in session:
        return redirect("/")

    return render_template("index.html", questions=questions)


# CAMERA ROUTE
@app.route("/camera")
def camera():

    threading.Thread(target=start_camera).start()

    return "Camera Started"


# SUBMIT ANSWERS
@app.route("/submit", methods=["POST"])
def submit():

    if "user" not in session:
        return redirect("/")

    answers = []

    for i in range(len(questions)):
        answers.append(request.form.get(f"answer{i}"))

    os.makedirs("results", exist_ok=True)

    pdf = canvas.Canvas("results/interview_result.pdf")

    y = 800

    for i in range(len(questions)):

        pdf.drawString(50,y,"Q: "+questions[i])
        y -= 30

        pdf.drawString(70,y,"A: "+answers[i])
        y -= 40

    pdf.save()

    return "🎉 Congratulations! Interview Completed"


if __name__ == "__main__":
    app.run(debug=True)