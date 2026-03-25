from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

SKILLS = [
    "python", "java", "c++", "machine learning",
    "deep learning", "sql", "data analysis",
    "flask", "django", "nlp", "tensorflow", "pandas"
]

def vectorize(resumes, job_desc):
    documents = resumes + [job_desc]
    tfidf = TfidfVectorizer()
    matrix = tfidf.fit_transform(documents)
    return matrix

def compute_similarity(vectors):
    job_vector = vectors[-1]
    resume_vectors = vectors[:-1]

    similarity = cosine_similarity(resume_vectors, job_vector)
    return similarity.flatten()

def compute_skill_score(text):
    score = 0
    for skill in SKILLS:
        if skill in text:
            score += 1
    return score / len(SKILLS)