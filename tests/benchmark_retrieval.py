import time
import pickle
import numpy as np
import pandas as pd

from pathlib import Path
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)

# Load project data and artifacts
start = time.perf_counter()
documents = pd.read_csv(ROOT / "data/chunks/document_chunks.csv").fillna("")
with open(ROOT / "models/tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)
with open(ROOT / "models/tfidf_document_vectors.pkl", "rb") as f:
    tfidf_vectors = pickle.load(f)
embeddings = np.load(ROOT / "models/document_embeddings.npy")
tfidf_load_time = time.perf_counter() - start

# Load semantic model separately
start = time.perf_counter()
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
semantic_load_time = time.perf_counter() - start

questions = [
    "What topics are covered in the Introduction to AI course?",
    "How can students submit their assignments?",
    "What should be included in an AI project report?",
    "Where can students find course information?",
    "What is the university hostel fee refund policy?"
]

contents = documents["content"].astype(str).tolist()
titles = documents["title"].astype(str).tolist()

def tfidf_search(question):
    query_vector = vectorizer.transform([question])
    scores = cosine_similarity(query_vector, tfidf_vectors)[0]
    return np.argsort(scores)[::-1][:3]

# Simulate Streamlit's cached title embeddings.
title_embeddings = model.encode(
    titles,
    convert_to_numpy=True,
    normalize_embeddings=True
)

def semantic_search(question):
    query_embedding = model.encode(
        [question],
        convert_to_numpy=True,
        normalize_embeddings=True
    )
    content_scores = np.dot(query_embedding, embeddings.T)[0]
    title_scores = np.dot(query_embedding, title_embeddings.T)[0]
    scores = 0.5 * content_scores + 0.5 * title_scores
    return np.argsort(scores)[::-1][:3]

records = []

for model_name, search_function in [
    ("TF-IDF", tfidf_search),
    ("Sentence Transformers", semantic_search)
]:
    # Warm-up run excluded from measurements
    search_function(questions[0])

    for question_number, question in enumerate(questions, start=1):
        start = time.perf_counter()
        search_function(question)
        elapsed = time.perf_counter() - start

        records.append({
            "model": model_name,
            "question_number": question_number,
            "latency_seconds": elapsed
        })

results = pd.DataFrame(records)
results.to_csv(REPORTS / "performance_benchmark.csv", index=False)

summary = results.groupby("model")["latency_seconds"].agg(
    ["mean", "min", "max"]
).round(4)

print("===== MODEL INITIALIZATION =====")
print(f"TF-IDF artifacts load time: {tfidf_load_time:.4f} seconds")
print(f"Semantic model load time: {semantic_load_time:.4f} seconds")
print("\n===== WARM QUERY PERFORMANCE =====")
print(summary.to_string())
print("\nDetailed measurements saved to reports/performance_benchmark.csv")
