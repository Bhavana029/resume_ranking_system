# AI-Powered Resume Screening and Ranking System

## 📌 Project Overview
This AI-powered Resume Screening and Ranking System automates the process of analyzing resumes based on job descriptions and ranks candidates accordingly. The system uses **Natural Language Processing (NLP) techniques** to match skills, experience, and qualifications with job requirements, making recruitment smarter and more efficient.

## 🔥 Features
- Extracts and processes resume text using **NLTK** and **spaCy**.
- Vectorizes text data with **TF-IDF (Scikit-learn)**.
- Uses **BERT (Hugging Face Transformers)** for deep learning-based matching.
- Ranks candidates based on job relevance using **cosine similarity**.
- Provides a user-friendly interface with **Flask/Django**.
- Supports **multiple resume formats (PDF, DOCX, TXT)**.
- Enables users to upload resumes and job descriptions through a web interface.
- Displays ranked candidates with relevance scores.

## 🚀 Tech Stack
- **Programming Language**: Python
- **Libraries & Frameworks**: 
  - NLP: `NLTK`, `spaCy`, `Scikit-learn`, `transformers`
  - Data Processing: `Pandas`, `NumPy`
  - Model Training: `TensorFlow/PyTorch`
  - Web Framework: `Flask` or `Django`
  - File Handling: `PyPDF2`, `python-docx`
  - Database: `SQLite` or `MongoDB`

## 📂 Project Structure
```
resume_screening/
│── models/                # Pretrained NLP models
│── static/                # CSS, JS, images (if using Flask/Django frontend)
│── templates/             # HTML files (if using Flask/Django frontend)
│── uploads/               # Resume files uploaded by users
│── app.py                 # Main Flask application (if using Flask)
│── views.py               # Django views (if using Django)
│── utils.py               # Helper functions for text processing
│── database/              # Stores application data (if using SQLite/MongoDB)
│── requirements.txt       # Dependencies
│── README.md              # Project Documentation
```

## 🛠 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/resume-screening.git
cd resume-screening
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv env
source env/bin/activate   # On Mac/Linux
env\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application
For Flask:
```bash
python app.py
```
For Django:
```bash
python manage.py runserver
```

## 🏗️ How It Works
1. **Upload Resumes** – Users upload resumes in PDF, DOCX, or TXT format.
2. **Preprocessing** – Extracts text, removes stopwords, and vectorizes using TF-IDF.
3. **Matching & Ranking** – Compares resumes with the job description using NLP models like **BERT**.
4. **Display Results** – Shows ranked candidates based on relevance.
5. **User Dashboard** – Displays uploaded resumes and job descriptions with ranking results.

## 📌 Future Enhancements
- Add support for multiple job descriptions.
- Implement deep learning models for improved accuracy.
- Integrate with ATS (Applicant Tracking Systems).
- Provide downloadable ranking reports.
- Add user authentication and role-based access control.

## 🤝 Contributions
Contributions are welcome! Feel free to fork the repository, open issues, or submit pull requests.

## 📜 License
This project is licensed under the MIT License.

## 📬 Contact
For queries, reach out via LinkedIn or GitHub.

**GitHub Repository:** [GitHub Link](https://github.com/yourusername/resume-screening)

---
✨ *Built with AI to simplify recruitment!*
