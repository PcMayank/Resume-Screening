# AI Resume Screening System

An AI-powered Resume Screening System that analyzes a candidate's resume against a job description and predicts whether the candidate is suitable for the role using Machine Learning and Natural Language Processing.

The system extracts text from uploaded resumes, cleans the text, converts it into numerical features using TF-IDF vectorization, and predicts the match score using a trained ML model.

---

## Features

* Upload resume in **PDF format**
* Paste **Job Description**
* Automatic **Resume–JD Matching**
* Displays **Match Score (%)**
* Shows **Selected / Rejected status**
* Displays **Matched Skills**
* Provides **Suggestions to improve the resume**

---

## Tech Stack

* Python
* Flask
* Scikit-learn
* Natural Language Processing (NLTK)
* TF-IDF Vectorization
* pdfplumber
* HTML
* CSS

---

## Project Structure

```
RESUME_SCREENING
│
├── artifacts
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── src
│   └── preprocessing
│       ├── clean_text.py
│       └── text_extractor.py
│
├── templates
│   └── index.html
│
├── static
│   └── style.css
│
├── uploaded_resumes
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```
git clone https://github.com/yourusername/resume-screening-ml.git
cd resume-screening-ml
```

Install dependencies

```
pip install -r requirements.txt
```

---

## Run the Application

```
python app.py
```

Open your browser and go to

```
http://127.0.0.1:5000
```

---

## How It Works

1. User uploads a **resume (PDF)**.
2. User pastes a **job description**.
3. The system extracts text from the resume using **pdfplumber**.
4. Text is cleaned using **NLP preprocessing**.
5. Resume text and job description are combined.
6. Text is converted to numerical features using **TF-IDF**.
7. The trained machine learning model predicts a **match probability**.
8. The system displays:

   * Match Score
   * Selection Status
   * Matched Skills
   * Resume Improvement Suggestion

---

## Example Output

The system provides:

* Resume Match Score (percentage)
* Selection status (Selected / Rejected)
* Matched technical skills
* Suggestions for improving the resume

---

## Future Improvements

* Add more training data for better accuracy
* Support multiple job roles
* Add resume ranking for multiple candidates
* Deploy the application online
* Improve the UI with dashboards

---

## Author

Mayank Singh

Machine Learning | AI | Python
