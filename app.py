import pickle
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data/chunks/document_chunks.csv"
TFIDF_VECTORIZER = BASE_DIR / "models/tfidf_vectorizer.pkl"
TFIDF_VECTORS = BASE_DIR / "models/tfidf_document_vectors.pkl"
DOCUMENT_EMBEDDINGS = BASE_DIR / "models/document_embeddings.npy"
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


st.set_page_config(
    page_title="CampusAssist | Student Assistant",
    page_icon="🎓",
    layout="wide"
)


@st.cache_data
def load_documents():
    return pd.read_csv(DATA_FILE).fillna("")


@st.cache_resource
def load_tfidf():
    with open(TFIDF_VECTORIZER, "rb") as f:
        vectorizer = pickle.load(f)

    with open(TFIDF_VECTORS, "rb") as f:
        vectors = pickle.load(f)

    return vectorizer, vectors


@st.cache_resource
def load_semantic_model():
    return SentenceTransformer(MODEL_NAME)


@st.cache_data
def load_document_embeddings():
    return np.load(DOCUMENT_EMBEDDINGS)


def retrieve_documents(question, model_name, top_k):
    documents = load_documents()
    contents = documents["content"].astype(str).tolist()

    if model_name == "TF-IDF":
        vectorizer, document_vectors = load_tfidf()
        query_vector = vectorizer.transform([question])
        scores = cosine_similarity(query_vector, document_vectors)[0]

    else:
        model = load_semantic_model()
        document_embeddings = load_document_embeddings()
        query_embedding = model.encode(
            [question],
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        title_embeddings = model.encode(
            documents["title"].astype(str).tolist(),
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        content_scores = np.dot(
            query_embedding, document_embeddings.T
        )[0]

        title_scores = np.dot(
            query_embedding, title_embeddings.T
        )[0]

        scores = 0.5 * content_scores + 0.5 * title_scores

    ranked_indices = np.argsort(scores)[::-1][:top_k]

    results = []
    for index in ranked_indices:
        result = documents.iloc[index].to_dict()
        result["similarity_score"] = float(scores[index])
        results.append(result)

    return results


# ---------------- USER INTERFACE ----------------

st.title("🎓 CampusAssist")
st.subheader("Your AI-powered student information assistant")

st.write(
    "Find relevant information from course guides, assignment "
    "instructions, student FAQs and policy examples."
)

st.info(
    "Prototype notice: This application uses 12 synthetic sample "
    "documents. Results are for demonstration only and are not "
    "official university information or policies."
)

with st.sidebar:
    st.header("Search Settings")

    selected_model = st.selectbox(
        "Choose retrieval model",
        ["Sentence Transformers", "TF-IDF"]
    )

    top_k = st.slider(
        "Number of results",
        min_value=1,
        max_value=5,
        value=3
    )

    st.divider()
    st.caption("CampusAssist | Module 5 Cloud Deployment")

question = st.text_area(
    "What would you like to know?",
    placeholder="Example: What topics are covered in the Introduction to AI course?",
    height=100
)

search_clicked = st.button(
    "🔍 Search Documents",
    type="primary",
    use_container_width=True
)

if search_clicked:
    cleaned_question = question.strip()

    if not cleaned_question:
        st.warning("Please enter a question before searching.")

    elif len(cleaned_question) > 1000:
        st.warning("Please keep your question under 1000 characters.")

    else:
        try:
            with st.spinner("Searching relevant documents..."):
                results = retrieve_documents(
                    cleaned_question,
                    selected_model,
                    top_k
                )

            st.success(f"Retrieved {len(results)} relevant documents.")

            for rank, result in enumerate(results, start=1):
                title = str(result.get("title", "Untitled"))
                category = str(result.get("category", "Unknown"))
                score = result["similarity_score"]

                with st.expander(
                    f"{rank}. {title} | Similarity: {score:.4f}",
                    expanded=(rank == 1)
                ):
                    col1, col2 = st.columns(2)

                    with col1:
                        st.write(f"**Document ID:** {result.get('document_id', 'N/A')}")
                        st.write(f"**Category:** {category}")

                    with col2:
                        st.write(f"**Chunk ID:** {result.get('chunk_id', 'N/A')}")
                        st.write(f"**Similarity score:** {score:.4f}")

                    st.markdown("**Retrieved content**")
                    st.write(result.get("content", ""))

            st.caption(
                "Similarity scores indicate retrieval relevance, "
                "not factual accuracy or answer confidence."
            )

        except Exception as error:
            st.error(f"Search failed: {error}")

st.divider()
st.caption("CampusAssist | Student Assistant Prototype")
