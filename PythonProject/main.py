import os
import fitz  # PyMuPDF for PDF extraction
import nltk
import string
import numpy as np
from flask import Flask, request, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('stopwords')
from nltk.corpus import stopwords

app = Flask(__name__)


# Function to extract text from PDFs
def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text


# Function to preprocess text
def preprocess_text(text):
    stop_words = set(stopwords.words("english"))
    text = text.lower().translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/matcher', methods=['POST'])
def match_resumes():
    job_description = request.form['job_desc']
    resume_files = request.files.getlist('resumes')

    if not job_description or len(resume_files) < 1:
        return "Please enter a job description and upload at least one resume."

    job_description = preprocess_text(job_description)
    resume_texts = []
    resume_names = []

    for resume in resume_files:
        filename = resume.filename
        filepath = os.path.join("uploads", filename)
        resume.save(filepath)

        text = extract_text_from_pdf(filepath)
        processed_text = preprocess_text(text)

        resume_texts.append(processed_text)
        resume_names.append(filename)

    # Compute TF-IDF and similarity scores
    vectorizer = TfidfVectorizer()
    all_texts = [job_description] + resume_texts
    tfidf_matrix = vectorizer.fit_transform(all_texts)

    similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    ranked_resumes = sorted(zip(resume_names, similarity_scores), key=lambda x: x[1], reverse=True)

    return render_template('results.html', ranked_resumes=ranked_resumes)


if __name__ == '__main__':
    os.makedirs("uploads", exist_ok=True)
    app.run(debug=True)
