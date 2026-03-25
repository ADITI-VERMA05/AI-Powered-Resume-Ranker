from flask import Flask, render_template, request, send_file
import os
import pandas as pd

from utils.extractor import extract_text_from_pdf
from utils.preprocess import preprocess
from utils.ranker import vectorize, compute_similarity, compute_skill_score

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload():
    files = request.files.getlist("resumes")
    job_desc = request.form["job_desc"]

    resume_texts = []
    resume_names = []

    # Extract + preprocess
    for file in files:
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        text = extract_text_from_pdf(filepath)
        processed = preprocess(text)

        resume_texts.append(processed)
        resume_names.append(file.filename)

    job_desc_processed = preprocess(job_desc)

    # Vectorization
    vectors = vectorize(resume_texts, job_desc_processed)

    # Similarity
    similarity_scores = compute_similarity(vectors)

    # Final scoring
    results = []

    for i in range(len(resume_texts)):
        sim = similarity_scores[i]
        skill = compute_skill_score(resume_texts[i])

        final = (0.7 * sim) + (0.3 * skill)

        results.append({
            "name": resume_names[i],
            "similarity": round(sim, 4),
            "skill": round(skill, 4),
            "final_score": round(final, 4)
        })

    # Sort
    ranked = sorted(results, key=lambda x: x["final_score"], reverse=True)

    # Save CSV
    df = pd.DataFrame(ranked)
    df.to_csv("report.csv", index=False)

    return render_template("result.html", ranked=ranked)

@app.route('/download')
def download():
    return send_file("report.csv", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)