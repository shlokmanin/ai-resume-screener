# AI Resume Screening and Candidate Management System

## Project Description
A full-stack web application for uploading resumes, extracting skills using AI, matching against job descriptions, and managing candidates. Built for final year B.Tech CSE (AI/ML) project.

## Technology Stack
- **Backend**: Python, Flask, SQLAlchemy
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Database**: SQLite (PostgreSQL compatible)
- **AI/ML**: scikit-learn, NLTK, PyPDF2
- **Auth**: Flask-Login, Werkzeug

## Installation
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and update values
4. Download NLTK data: Run `python` and execute:
   ```
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```
5. Run the app: `python app.py`

## Features
- User authentication (signup/login)
- Resume PDF upload and text extraction
- AI skill extraction
- Job description matching with score
- Results dashboard
- Feedback system
- Responsive design

## How to Run
```
python app.py
```
Visit `http://127.0.0.1:5000/`

## Deployment
- Update DATABASE_URL for PostgreSQL
- Set production SECRET_KEY
- Deploy to Heroku/Vercel/Railway

## Folder Structure
```
project/
├── app.py
├── requirements.txt
├── templates/
├── static/
├── models/
├── uploads/
└── database.db
```

