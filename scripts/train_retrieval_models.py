
import os
import json
import pickle
import numpy as np
import pandas as pd

from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Project paths
CHUNKS_FILE = "data/chunks/document_chunks.csv"
QUESTIONS_FILE = "data/evaluation/test_questions.csv"
MODEL_DIR = "models"
REPORT_DIR = "reports"

os.makedirs(MODEL_DIR, exist_ok=True)


# Load data
documents = pd.read_csv(CHUNKS_FILE).fillna("")
questions = pd.read_csv(QUESTIONS_FILE).fillna("")

texts = documents["content"].astype(str).tolist()
queries = questions["question"].astype(str).tolist()

print("Documents loaded:", len(texts))
print("Evaluation questions loaded:", len(queries))


# Model 1: TF-IDF
print("\nTraining TF-IDF retrieval model...")

tfidf = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
document_vectors = tfidf.fit_transform(texts)
query_vectors = tfidf.transform(queries)

tfidf_scores = cosine_similarity(query_vectors, document_vectors)

with open(f"{MODEL_DIR}/tfidf_vectorizer.pkl", "wb") as file:
    pickle.dump(tfidf, file)

with open(f"{MODEL_DIR}/tfidf_document_vectors.pkl", "wb") as file:
    pickle.dump(document_vectors, file)


# Model 2: Sentence Transformers
print("\nLoading Sentence Transformer...")

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

document_embeddings = model.encode(
    texts,
    convert_to_numpy=True,
    normalize_embeddings=True,
    show_progress_bar=True
)

query_embeddings = model.encode(
    queries,
    convert_to_numpy=True,
    normalize_embeddings=True,
    show_progress_bar=True
)

semantic_scores = np.dot(query_embeddings, document_embeddings.T)

np.save(f"{MODEL_DIR}/document_embeddings.npy", document_embeddings)


# Evaluation
def evaluate_model(scores, model_name):
    results = []

    for index, question in questions.iterrows():
        ranking = np.argsort(scores[index])[::-1]
        expected_id = str(question["expected_document_id"]).strip()

        top_index = ranking[0]
        top_document = str(documents.iloc[top_index]["document_id"])

        is_answerable = str(question["is_answerable"]).strip().lower() == "true"

        reciprocal_rank = 0.0

        if is_answerable:
            for rank, doc_index in enumerate(ranking, start=1):
                if str(documents.iloc[doc_index]["document_id"]) == expected_id:
                    reciprocal_rank = 1 / rank
                    break

        results.append({
            "question_id": question.get("question_id", index + 1),
            "model": model_name,
            "expected_document_id": expected_id,
            "retrieved_document_id": top_document,
            "top_similarity_score": float(scores[index][top_index]),
            "is_answerable": is_answerable,
            "top1_correct": (
                is_answerable and top_document == expected_id
            ),
            "reciprocal_rank": reciprocal_rank
        })

    result_df = pd.DataFrame(results)

    answerable = result_df[result_df["is_answerable"]]

    metrics = {
        "model": model_name,
        "total_questions": len(result_df),
        "answerable_questions": len(answerable),
        "top1_accuracy": float(answerable["top1_correct"].mean()),
        "mrr": float(answerable["reciprocal_rank"].mean()),
        "recall_at_3": float(
            sum(
                any(
                    str(documents.iloc[i]["document_id"]) ==
                    str(row["expected_document_id"])
                    for i in np.argsort(scores[idx])[::-1][:3]
                )
                for idx, row in questions.iterrows()
                if result_df.iloc[idx]["is_answerable"]
            ) / len(answerable)
        )
    }

    return result_df, metrics


tfidf_results, tfidf_metrics = evaluate_model(tfidf_scores, "TF-IDF")
semantic_results, semantic_metrics = evaluate_model(
    semantic_scores, "Sentence Transformers"
)


# Save evaluation results
all_results = pd.concat([tfidf_results, semantic_results], ignore_index=True)
all_results.to_csv(f"{REPORT_DIR}/retrieval_evaluation_results.csv", index=False)

comparison = pd.DataFrame([tfidf_metrics, semantic_metrics])
comparison.to_csv(f"{REPORT_DIR}/model_comparison.csv", index=False)

with open(f"{MODEL_DIR}/model_config.json", "w") as file:
    json.dump({
        "embedding_model": "sentence-transformers/all-MiniLM-L6-v2",
        "embedding_dimensions": 384,
        "tfidf_ngram_range": [1, 2],
        "similarity_metric": "cosine_similarity",
        "document_count": len(documents),
        "evaluation_question_count": len(questions)
    }, file, indent=4)


# Display results
print("\n========== MODEL COMPARISON ==========")
print(comparison.to_string(index=False))

print("\nEvaluation results saved in reports/")
print("Model artefacts saved in models/")
print("\nRetrieval model development completed!")
