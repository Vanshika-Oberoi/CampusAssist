# CampusAssist – User Guide

## 1. Overview

CampusAssist is a student information retrieval prototype. It searches sample course guides, assignment instructions, FAQs, and policy examples.

The application uses 12 synthetic documents. Results are for demonstration only and are not official university information.

## 2. Access the Application

Live application: https://campusassist.streamlit.app

GitHub: https://github.com/Vanshika-Oberoi/CampusAssist

## 3. Local Installation

Prerequisites: Python 3.10 or compatible version, Git, and internet access.

Clone the repository:

    git clone https://github.com/Vanshika-Oberoi/CampusAssist.git
    cd CampusAssist

For macOS, install dependencies:

    python3 -m pip install streamlit==1.65.0 pandas==2.3.3 numpy==2.2.6 scikit-learn==1.7.2 sentence-transformers==6.3.0

PyTorch must also be installed. Follow https://pytorch.org/get-started/locally/ if it is not already available.

Run the application:

    python3 -m streamlit run app.py

Open http://localhost:8501 in your browser.

Note: requirements.txt contains a CPU-specific PyTorch pin for cloud deployment. The local macOS installation command above avoids that pin.

## 4. How to Use CampusAssist

1. Open the live application or run it locally.
2. Select a retrieval model in the sidebar.
3. Choose the number of results using Top-K.
4. Enter your question.
5. Click Search Documents.
6. Review and expand the retrieved documents.

Example questions:
- What topics are covered in the Introduction to AI course?
- What should be included in an AI project report?
- How can students submit their assignments?

## 5. Retrieval Models

**Sentence Transformers:** Uses the pretrained all-MiniLM-L6-v2 model to compare semantic meaning between questions and document titles and content.

**TF-IDF:** Uses keyword and phrase-based vectorization with cosine similarity. It provides a lexical retrieval baseline.

## 6. Understanding Results

Results can include:
- Title
- Document ID
- Category
- Chunk ID
- Similarity score
- Retrieved document content

Similarity indicates retrieval relevance. It does not establish factual accuracy or answer confidence.

## 7. Input Validation

- Empty questions are rejected.
- Questions longer than 1,000 characters are rejected.
- Leading and trailing whitespace is removed.
- Retrieval errors are displayed to the user.

## 8. Troubleshooting

| Issue | Suggested action |
|---|---|
| Application does not open | Check the URL or restart Streamlit |
| Missing dependencies | Install the required packages |
| Semantic model loads slowly | Allow time for model initialization |
| Empty question warning | Enter a question |
| Question too long | Reduce it to 1,000 characters or fewer |
| Unexpected results | Try different wording or compare both models |
| Port already in use | Stop the existing process or choose another port |

## 9. Known Limitations

- Only 12 synthetic sample documents are included.
- The application retrieves documents; it does not generate LLM answers.
- Unsupported questions may still return documents.
- Reliable abstention is not implemented.
- Similarity scores are not factual confidence scores.
- Authentication and role-based access control are not implemented.
- Do not use this prototype as an official university source or for confidential student information.

## 10. Best Practices

Ask specific questions, try alternative wording, compare retrieval models when needed, read retrieved content, and verify important information with official university sources.

## 11. Conclusion

CampusAssist demonstrates semantic and keyword-based retrieval through a simple student information search interface. This guide explains how to access and use the prototype while highlighting its limitations.
