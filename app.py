from flask import Flask, render_template, request
import os
import joblib

from src.preprocessing.text_extractor import extract_text_from_pdf
from src.preprocessing.clean_text import clean_text

app = Flask(__name__)

UPLOAD_FOLDER = "uploaded_resumes"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

model = joblib.load("artifacts/model.pkl")
vectorizer = joblib.load("artifacts/vectorizer.pkl")


@app.route("/", methods=["GET", "POST"])
def home():

    score = None
    result = None
    matched_skills = []
    suggestion = ""

    if request.method == "POST":

        file = request.files["resume"]
        jd = request.form["jd"]

        path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(path)

        resume_text = extract_text_from_pdf(path)

        resume_clean = clean_text(resume_text)
        jd_clean = clean_text(jd)

        combined = resume_clean + " " + jd_clean

        vec = vectorizer.transform([combined])

        prob = model.predict_proba(vec)[0][1]

        score = round(prob * 100, 2)

        if score > 60:
            result = "Selected ✅"
        else:
            result = "Rejected ❌"

        skills_list = ["python","machine learning","c++","java","sql","ai","deep learning"]

        for skill in skills_list:
            if skill in resume_clean:
                matched_skills.append(skill.capitalize())

        if not matched_skills:
            matched_skills = ["No strong matching skills found"]

        if score < 60:
            suggestion = "Add more technical skills related to the job description."
        else:
            suggestion = "Your resume matches well with the job role."

    return render_template(
        "index.html",
        score=score,
        result=result,
        matched_skills=matched_skills,
        suggestion=suggestion
    )