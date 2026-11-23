import json
import pickle
import unittest
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


class CampusAssistArtifactTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.documents = pd.read_csv(
            ROOT / "data/chunks/document_chunks.csv"
        ).fillna("")

        cls.questions = pd.read_csv(
            ROOT / "data/evaluation/test_questions.csv"
        ).fillna("")

        cls.embeddings = np.load(
            ROOT / "models/document_embeddings.npy"
        )

        with open(ROOT / "models/tfidf_vectorizer.pkl", "rb") as f:
            cls.vectorizer = pickle.load(f)

        with open(ROOT / "models/tfidf_document_vectors.pkl", "rb") as f:
            cls.tfidf_vectors = pickle.load(f)

        with open(ROOT / "models/model_config.json") as f:
            cls.config = json.load(f)

    def test_document_count(self):
        self.assertEqual(len(self.documents), 12)

    def test_required_document_columns(self):
        required = {
            "document_id", "chunk_id", "title",
            "category", "content", "word_count"
        }
        self.assertTrue(required.issubset(self.documents.columns))

    def test_document_ids_are_unique(self):
        self.assertEqual(
            self.documents["document_id"].nunique(),
            len(self.documents)
        )

    def test_semantic_embedding_shape(self):
        self.assertEqual(
            self.embeddings.shape,
            (len(self.documents), 384)
        )

    def test_semantic_embeddings_are_finite(self):
        self.assertTrue(np.isfinite(self.embeddings).all())

    def test_tfidf_vector_count(self):
        self.assertEqual(
            self.tfidf_vectors.shape[0],
            len(self.documents)
        )

    def test_tfidf_feature_count(self):
        self.assertEqual(
            self.tfidf_vectors.shape[1],
            len(self.vectorizer.get_feature_names_out())
        )

    def test_evaluation_question_count(self):
        self.assertEqual(len(self.questions), 15)

    def test_answerable_question_count(self):
        answerable = (
            self.questions["is_answerable"]
            .astype(str).str.lower() == "true"
        )
        self.assertEqual(int(answerable.sum()), 12)

    def test_unanswerable_question_count(self):
        answerable = (
            self.questions["is_answerable"]
            .astype(str).str.lower() == "true"
        )
        self.assertEqual(int((~answerable).sum()), 3)

    def test_evaluation_results_cover_both_models(self):
        results = pd.read_csv(
            ROOT / "reports/retrieval_evaluation_results.csv"
        )
        self.assertEqual(len(results), 30)
        self.assertEqual(
            set(results["model"]),
            {"TF-IDF", "Sentence Transformers"}
        )

    def test_model_comparison_metrics(self):
        comparison = pd.read_csv(
            ROOT / "reports/model_comparison.csv"
        )
        self.assertEqual(len(comparison), 2)

        for metric in ["top1_accuracy", "mrr", "recall_at_3"]:
            self.assertTrue((comparison[metric] == 1.0).all())

    def test_model_configuration(self):
        self.assertEqual(self.config["document_count"], 12)
        self.assertEqual(self.config["embedding_dimensions"], 384)
        self.assertEqual(self.config["evaluation_question_count"], 15)


if __name__ == "__main__":
    unittest.main(verbosity=2)
