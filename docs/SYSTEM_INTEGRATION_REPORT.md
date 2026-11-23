# CampusAssist – System Integration Report

**Module:** 6 – System Integration  
**Project:** CampusAssist  
**Date:** 23 November 2026  
**Status:** Integrated prototype – ready for further testing

## 1. Objective

The objective of this module is to integrate the data preparation pipeline, retrieval models and Streamlit application into one working solution. The integrated system is tested to verify data consistency, model connectivity, application workflows and basic input handling.

## 2. Integrated System Overview

CampusAssist uses a retrieval-based architecture to identify relevant content from a collection of 12 synthetic sample documents.

The integrated workflow is:

1. Raw synthetic documents and metadata are loaded.
2. The data preparation pipeline cleans documents, engineers features and creates document chunks.
3. The model training pipeline generates TF-IDF vectors and Sentence Transformer embeddings.
4. The Streamlit application loads the prepared document collection and model artifacts.
5. Users select a retrieval model and submit a question.
6. The selected model ranks relevant document chunks.
7. The application displays the top results and similarity scores.

The system is deployed using Streamlit Community Cloud.

## 3. Integrated Components

| Component | Implementation | Integration |
|---|---|---|
| Raw data | TXT documents and metadata CSV | Connected to preparation pipeline |
| Data preparation | scripts/prepare_data.py | Generates processed datasets and chunks |
| Chunk storage | CSV and JSON | Consumed by retrieval workflow |
| Evaluation dataset | data/evaluation/test_questions.csv | Used during model evaluation |
| TF-IDF retrieval | Scikit-learn | Vectorizer and document vectors loaded by app |
| Semantic retrieval | Sentence Transformers | Pretrained MiniLM model and document embeddings |
| Application | app.py | Connects retrieval models with Streamlit UI |
| Cloud deployment | Streamlit Community Cloud | Hosts the application |

## 4. Data and Model Integration Validation

The following consistency checks were performed:

| Validation | Observed Result | Status |
|---|---|---|
| Prepared document count | 12 | Passed |
| Required document columns | Present | Passed |
| Semantic embedding dimensions | 12 × 384 | Passed |
| TF-IDF document vector dimensions | 12 × 564 | Passed |
| Semantic embedding row alignment | 12 matching rows | Passed |
| TF-IDF vector row alignment | 12 matching rows | Passed |
| Python syntax compilation | No errors | Passed |

The document collection and both retrieval artifact sets have matching row counts.

## 5. Application Integration Testing

The application was launched locally and tested with both retrieval models.

### Test 1: Course information

**Query:** What topics are covered in the Introduction to AI course?

- Sentence Transformers returned DOC002 at rank 1.
- TF-IDF returned DOC002 at rank 1.
- Both returned three results with relevant retrieved content.

**Result:** Passed.

### Test 2: Student FAQ

**Query:** How can students submit their assignments?

- Sentence Transformers returned DOC007 at rank 1, with similarity 0.5809.
- TF-IDF returned DOC007 at rank 2, with similarity 0.0624.
- Both retrieved the correct FAQ within their top three results.

**Result:** Passed with a retrieval ranking limitation for TF-IDF.

### Test 3: Unsupported policy query

**Query:** What is the university's hostel fee refund policy?

- Sentence Transformers returned DOC012 at rank 1.
- TF-IDF returned DOC012 at rank 1.
- Neither model retrieved an actual hostel fee refund policy.

**Result:** Application execution passed. Unsupported-query rejection is not implemented.

### Test 4: Empty input validation

The search button was clicked without entering a question.

- The application displayed the expected warning.
- Retrieval was not initiated.

**Result:** Passed.

## 6. Integration Issues and Observations

### 6.1 Different ranking behaviour

The two retrieval models do not always rank documents identically. For the assignment submission FAQ, semantic retrieval ranked the correct document first, while TF-IDF ranked it second.

This is an observed retrieval quality difference, not an application failure.

### 6.2 Unsupported questions

The application currently returns the top-k documents even when the requested information is absent from the dataset.

There is no verified similarity threshold or abstention mechanism to reject unsupported questions.

Similarity scores must not be interpreted as factual accuracy or answer confidence.

### 6.3 Prototype data limitation

The system uses only 12 synthetic documents. Its results cannot establish the quality or reliability of a production university information service.

No changes to the existing retrieval algorithms were required to complete the current integration checks.

## 7. Security and Operational Considerations

- The application validates empty questions and limits question length to 1,000 characters.
- Deployment secrets are excluded through the project's Git ignore configuration.
- The application displays a notice explaining that its documents are synthetic.
- Similarity scores are explicitly described as retrieval relevance indicators.
- The current prototype does not implement user authentication, role-based access control or production-grade monitoring.

## 8. Updated Architecture

The end-to-end integration architecture is maintained in:

`docs/diagrams/07_end_to_end_integration.mmd`

The diagram represents raw data processing, model training, retrieval, application integration and cloud deployment.

## 9. Integration Conclusion

The data preparation pipeline, retrieval artifacts and Streamlit application have been integrated and verified through structural checks and local application tests.

Both retrieval models successfully retrieve relevant documents, and the application handles the tested input workflows without crashing.

The prototype is ready for further testing. Improvements such as unsupported-query rejection, larger real-world datasets and broader retrieval evaluation should be considered before any production use.

**Final status:** Core integration checks passed. Known limitations are documented.
