# AI-Powered-Resume-Ranker
Developed a web-based application that ranks resumes based on job descriptions using NLP techniques. Implemented text extraction, preprocessing with SpaCy, TF-IDF vectorization, and cosine similarity for scoring. Built a Flask-based interface for uploading resumes, displaying rankings, and generating downloadable HR reports.

### Project Architecture
```
User Uploads Resumes (PDF)
        ↓
Text Extraction (PDF → Text)
        ↓
NLP Preprocessing (SpaCy)
        ↓
Feature Extraction (TF-IDF)
        ↓
Similarity Scoring (JD vs Resume)
        ↓
Ranking Algorithm
        ↓
Flask Web UI (Display Results + Download Report)
```

### Folder Structure
```
resume-ranker/
│
├── app.py
├── uploads/
├── templates/
│   ├── index.html
│   └── result.html
├── static/
├── report.csv
└── utils/
    ├── extractor.py
    ├── preprocess.py
    ├── ranker.py
```
