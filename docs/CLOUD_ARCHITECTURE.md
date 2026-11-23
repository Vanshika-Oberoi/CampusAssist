# CampusAssist – Cloud Architecture Document

## 1. Project Overview

CampusAssist is a cloud-deployed student information assistant prototype. It retrieves relevant information from course guides, assignment instructions, student FAQs and sample policy documents.

The application uses a synthetic dataset containing 12 sample documents. It is intended for demonstration and is not an official university information system.

## 2. Architecture Objectives

- Provide a simple web-based interface for student queries.
- Retrieve relevant documents using machine learning techniques.
- Support both semantic and keyword-based retrieval.
- Deploy the application through a cloud hosting platform.
- Maintain a modular and understandable project structure.
- Validate retrieval results through functional testing.

## 3. Cloud Platform

| Component | Technology |
|---|---|
| Cloud hosting | Streamlit Community Cloud |
| Source code repository | GitHub |
| Repository branch | main |
| Application framework | Streamlit |
| Runtime | Python 3.11 |
| Semantic retrieval | Sentence Transformers |
| Embedding model | all-MiniLM-L6-v2 |
| Keyword retrieval | TF-IDF |
| Similarity calculation | Cosine similarity / dot product |
| Data storage | CSV files in GitHub repository |
| Model artifacts | Files stored in GitHub repository |

Live application: https://campusassist.streamlit.app

GitHub repository: https://github.com/Vanshika-Oberoi/CampusAssist

## 4. High-Level Architecture

The architecture consists of the following layers:

1. **User Interface:** Students enter questions through the Streamlit web application.
2. **Cloud Hosting:** Streamlit Community Cloud hosts and runs the application.
3. **Application Logic:** Python processes queries and coordinates document retrieval.
4. **Data Layer:** The application reads the prepared document chunks from a CSV file.
5. **AI/ML Retrieval Layer:** TF-IDF or Sentence Transformers calculates document relevance.
6. **Results Layer:** The application ranks documents and displays their content and similarity scores.

## 5. Retrieval Architecture

CampusAssist supports two retrieval approaches.

### 5.1 TF-IDF Retrieval

- Loads the trained TF-IDF vectorizer.
- Converts the user's question into a numerical vector.
- Compares it with stored document vectors.
- Uses cosine similarity to rank documents.

### 5.2 Semantic Retrieval

- Loads the pretrained all-MiniLM-L6-v2 model.
- Converts the user's question into a normalized embedding.
- Compares the query embedding with stored document content embeddings.
- Generates title embeddings for the document collection.
- Combines title and content similarity scores using equal weighting.

Combined score:

`Final Score = 0.5 × Title Similarity + 0.5 × Content Similarity`

The highest-scoring documents are displayed first.

The model is used for pretrained inference. It is not fine-tuned, and the application does not generate answers using an LLM.

## 6. Data Flow

1. A student opens the deployed CampusAssist application.
2. The student enters a question.
3. The application validates the input.
4. The selected retrieval model processes the question.
5. Similarity scores are calculated against the document collection.
6. Documents are sorted by relevance.
7. The top-k documents and their content are displayed to the student.

## 7. Deployment Architecture

- Application source code is maintained in GitHub.
- The main branch is connected to Streamlit Community Cloud.
- Streamlit installs dependencies from requirements.txt.
- The cloud runtime executes app.py.
- Application data and model artifacts are loaded from the repository.
- GitHub updates trigger application redeployment through the connected hosting service.

## 8. Security and Governance

Implemented safeguards:

- Git ignore rules exclude environment files and Streamlit secrets files.
- User input is checked for empty values.
- Query length is limited to 1000 characters.
- The prototype clearly identifies its documents as synthetic.
- Similarity scores are described as relevance indicators, not factual accuracy or confidence.

Current limitations:

- User authentication and role-based access control are not implemented.
- No separate cloud database or object storage service is configured.
- No confidential student records are used.
- Advanced security monitoring and audit infrastructure are not implemented.

## 9. Monitoring and Operations

Basic operational monitoring is available through Streamlit Community Cloud application logs.

The application includes error handling for retrieval failures and displays an error message when a search fails.

Dedicated dashboards, alerting, distributed tracing and production-grade monitoring are outside the current prototype scope.

## 10. Architecture Limitations

- The dataset contains only 12 synthetic documents.
- The application is a retrieval-based prototype, not a complete generative RAG system.
- Retrieval quality must be evaluated on a larger and more diverse dataset before real-world use.
- Cloud resources and application availability depend on Streamlit Community Cloud.
- Infrastructure as Code has not been implemented.

## 11. Conclusion

CampusAssist demonstrates the integration of a Python web application, machine learning-based document retrieval, GitHub version control and cloud hosting.

The deployed prototype supports semantic and keyword-based search and displays ranked source documents through an accessible web interface.
