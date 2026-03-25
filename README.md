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
### UI

<img width="2560" height="1504" alt="image" src="https://github.com/user-attachments/assets/ae002bba-9631-484c-aefc-9a9e96eb3e67" />
<img width="2560" height="1504" alt="image" src="https://github.com/user-attachments/assets/6d82b173-db82-44a7-96f4-6f1d68f0840a" />

### 🚀 Installation & Setup

1️⃣ Clone the Repository
```
git clone https://github.com/your-username/AI-Powered-Resume-Ranker.git
cd AI-Powered-Resume-Ranker
```
2️⃣ Install Dependencies
```
pip install -r requirements.txt
```
3️⃣ Run the Application
```
python app.py
```
4️⃣ Open in Browser
```
http://localhost:5000
```
