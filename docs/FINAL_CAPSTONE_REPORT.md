# CampusAssist
## Final Capstone Project Report

**Project:** AI-Powered Student Information Retrieval Assistant
**Application:** https://campusassist.streamlit.app
**Repository:** https://github.com/Vanshika-Oberoi/CampusAssist

---

## 1. Abstract

CampusAssist is an AI-powered student information retrieval prototype designed to help users locate relevant information from course guides, assignment instructions, student FAQs, and policy examples.

The system combines data preparation, feature engineering, lexical retrieval using TF-IDF, and semantic retrieval using a pretrained Sentence Transformers model. A Streamlit application provides an interface for searching documents and comparing retrieval approaches. The prototype is deployed using Streamlit Community Cloud.

Evaluation was performed using 12 synthetic sample documents and 15 questions. Both retrieval models achieved Top-1 Accuracy, Mean Reciprocal Rank (MRR), and Recall@3 of 1.00 across the 12 answerable questions. Automated artifact validation passed 13 tests.

Performance optimization through caching semantic title embeddings reduced average local warm-query time from 81.4 ms to 7.9 ms in the measured benchmark.

The project also identified limitations, including unreliable handling of unsupported questions, a small synthetic dataset, and the absence of formal stakeholder UAT and production-scale testing.

## 2. Introduction

Students often need to locate information across course materials, assignment guidelines, FAQs, and academic documents. Manually searching multiple documents can take time and make relevant information difficult to find.

CampusAssist demonstrates how information retrieval techniques can provide a simple search interface over a structured document collection.

The project focuses on retrieving relevant source content rather than generating answers with a large language model. This approach allows users to inspect the retrieved information directly.

## 3. Problem Statement

Students may need to search different academic documents to find information about courses, assignments, and frequently asked questions.

A simple search system should:
- Accept natural-language questions.
- Identify relevant documents.
- Rank results by retrieval relevance.
- Display source content and document metadata.
- Support comparison between keyword-based and semantic retrieval.

CampusAssist addresses this problem through a small, demonstrative retrieval application.

## 4. Project Objectives

The main objectives are:

1. Prepare and validate a structured document dataset.
2. Perform data exploration and feature engineering.
3. Implement lexical and semantic retrieval models.
4. Evaluate retrieval quality using defined metrics.
5. Develop a user-friendly Streamlit application.
6. Deploy the application to Streamlit Community Cloud.
7. Integrate and validate the system components.
8. Measure and optimize retrieval performance.
9. Document testing, security considerations, and known limitations.

## 5. Scope and Dataset

The prototype uses 12 synthetic sample documents representing:
- Course information.
- Assignment instructions.
- Student FAQs.
- Policy examples.

The evaluation dataset contains 15 questions:
- 12 answerable questions.
- 3 unanswerable questions.

The document collection is intended for controlled demonstration and is not an official university knowledge base.

### 5.1 Data Schema

The prepared document chunks contain fields including:

| Field | Description |
|---|---|
| document_id | Unique document identifier |
| chunk_id | Unique chunk identifier |
| title | Document title |
| category | Document category |
| source_type | Source classification |
| chunk_index | Position of the chunk |
| content | Text content |
| word_count | Number of words |

### 5.2 Data Preparation

The data preparation workflow includes:
- Loading raw document metadata.
- Cleaning and validating document content.
- Preparing structured records.
- Splitting document content into chunks.
- Extracting descriptive features.
- Exporting processed data for model training and retrieval.

Five engineered features include character count, sentence count, average word length, question presence, and number presence.

The configured chunking parameters are 100 words with 20-word overlap. The current sample documents are shorter than the configured chunk size, so overlap is not exercised by this dataset.

## 6. Exploratory Data Analysis and Feature Engineering

Exploratory analysis was used to understand the sample dataset and its structure.

Feature engineering produced five descriptive features:
- `character_count`
- `sentence_count`
- `avg_word_length`
- `has_question`
- `has_number`

Data validation checked required fields, document identifiers, and consistency of prepared outputs.

The dataset is small and synthetic; therefore, the analysis should be interpreted as a demonstration of the data workflow rather than a representative statistical study of university information.

## 7. System Architecture

CampusAssist follows a retrieval-based architecture.

### 7.1 Main Components

1. **Raw data:** Sample document metadata and evaluation questions.
2. **Data preparation:** Cleaning, feature engineering, and chunk generation.
3. **Model training and evaluation pipeline:** Creates TF-IDF and semantic retrieval artifacts and evaluates retrieval performance.
4. **Model artifacts:** TF-IDF vectorizer, TF-IDF document vectors, semantic document embeddings, and model configuration.
5. **Streamlit application:** Accepts questions, selects a retrieval model, ranks documents, and displays results.
6. **Deployment:** Streamlit Community Cloud hosts the application.

### 7.2 Retrieval Workflow

A user enters a question and selects a retrieval model.

For TF-IDF, the application transforms the query using the fitted vectorizer and calculates cosine similarity against stored document vectors.

For semantic retrieval, the application encodes the query using the pretrained Sentence Transformers model. It compares the query with document content embeddings and title embeddings. The final score combines content and title similarity with equal weights.

The application sorts the scores and displays the selected Top-K results.

### 7.3 Architecture Diagram

The editable Mermaid architecture source is available at:

`docs/diagrams/07_end_to_end_integration.mmd`

Additional infrastructure, data flow, retrieval, application, security, and integration diagrams are available in `docs/diagrams/`.

## 8. Retrieval Models

### 8.1 TF-IDF

TF-IDF represents documents using term-frequency and inverse-document-frequency weighting.

The implementation uses:
- Scikit-learn `TfidfVectorizer`.
- English stop-word removal.
- Unigram and bigram features.
- Cosine similarity for ranking.

TF-IDF provides a keyword-based retrieval baseline.

### 8.2 Sentence Transformers

The semantic retrieval model uses the pretrained:

`sentence-transformers/all-MiniLM-L6-v2`

The model creates 384-dimensional embeddings.

The application compares query embeddings against document content embeddings and title embeddings. The combined score is:

`Final Score = 0.5 × Content Similarity + 0.5 × Title Similarity`

The model is used for inference and has not been fine-tuned on the project dataset.

## 9. Evaluation Methodology and Results

The evaluation dataset contains 15 questions. Aggregate retrieval metrics are calculated over the 12 answerable questions.

| Metric | TF-IDF | Sentence Transformers |
|---|---:|---:|
| Top-1 Accuracy | 1.00 | 1.00 |
| MRR | 1.00 | 1.00 |
| Recall@3 | 1.00 | 1.00 |

These results indicate that both approaches retrieved the expected document successfully for the answerable questions in this controlled evaluation.

The three unanswerable questions are excluded from the aggregate metrics. Separate validation showed that both models still returned documents for unsupported questions.

Consequently, perfect answerable-question metrics do not demonstrate reliable answer rejection or generalization to unseen university queries.

## 10. Application Development

The user interface is developed using Streamlit.

Key application features include:
- Retrieval model selection.
- Top-K result selection.
- Natural-language question input.
- Empty-input validation.
- A 1,000-character input limit.
- Expandable result sections.
- Document metadata and content display.
- Similarity scores with an explanation of their meaning.
- A synthetic-data disclaimer.

The application retrieves source documents. It does not generate LLM-based answers.

## 11. Cloud Deployment

The application is deployed using Streamlit Community Cloud.

Live application:

https://campusassist.streamlit.app

The repository contains the application code, prepared data, retrieval artifacts, and dependency configuration required by the deployment.

The deployment uses Python 3.11 and CPU-only PyTorch dependencies. The cloud application loads the committed document and model artifacts.

The cloud deployment and local development environments may have different dependency requirements.

## 12. System Integration and Testing

System integration validation checked consistency between the document collection and model artifacts.

Verified dimensions included:
- 12 document records.
- Semantic embeddings with shape 12 × 384.
- 12 TF-IDF document vectors.
- Consistent document and artifact row counts.
- Required document columns.

Previous integration testing exercised course-related questions, assignment-related questions, empty input, and unsupported policy questions using both retrieval modes.

### 12.1 Automated Validation

The Module 7 automated suite was executed using:

`python3 -m unittest discover -s tests -v`

All 13 artifact validation tests passed.

These tests validate data, model configuration, stored artifacts, and evaluation outputs. They are not a complete automated end-to-end UI test suite.

### 12.2 Unsupported Questions

The three unanswerable questions returned retrieved documents under both models.

The system does not reliably abstain when the dataset does not contain the requested information. Similarity-score overlap between answerable and unanswerable questions means a reliable threshold cannot be established from the current small dataset.

### 12.3 Security Review

The limited security review verified:
- Secret-file exclusion patterns in `.gitignore`.
- No matching local secret files in inspected paths.
- No matching secret-like files tracked by Git.
- Basic input validation and retrieval error handling.

Authentication and role-based access control are not implemented. Formal penetration testing and dependency vulnerability assessment were not performed.

## 13. Performance Optimization

A local benchmark was conducted using five representative queries per retrieval model, with warm-up before timed measurements.

The original semantic retrieval path encoded all document titles during each query. This repeated computation was identified as an optimization opportunity.

Title embeddings were cached using Streamlit's data cache so that repeated queries could reuse them.

| Measurement | Before optimization | After optimization |
|---|---:|---:|
| Semantic average query time | 0.0814 s | 0.0079 s |
| Semantic minimum | 0.0156 s | 0.0066 s |
| Semantic maximum | 0.3390 s | 0.0092 s |
| TF-IDF average query time | 0.0003 s | 0.0004 s |

Average semantic query time decreased by approximately 90.3%, or about 10.3 times in this benchmark.

These figures represent local warm-query measurements, not cloud end-to-end latency or production-scale performance.

## 14. Limitations

The current prototype has the following limitations:

1. The dataset contains only 12 synthetic documents.
2. The evaluation includes only 12 answerable and 3 unanswerable questions.
3. Both retrieval models return documents for unsupported questions.
4. Similarity scores are not factual confidence scores.
5. The application does not generate LLM-based answers.
6. Authentication and role-based access control are not implemented.
7. No formal stakeholder UAT was performed.
8. No formal penetration test or production-scale load test was performed.
9. Local benchmark results may differ from deployed cloud performance.
10. The dataset does not represent the complexity or diversity of a real university knowledge base.

## 15. Future Enhancements

Potential improvements include:

- Expanding the document collection using approved university information.
- Adding more realistic, paraphrased, ambiguous, and unanswerable evaluation questions.
- Developing model-specific abstention and confidence calibration.
- Evaluating alternative embedding and retrieval models.
- Adding metadata filters and improved document organization.
- Introducing authentication and role-based access where required.
- Performing formal stakeholder UAT.
- Adding performance, load, and security testing.
- Exploring an optional LLM-based answer generation layer with source-grounded responses and explicit abstention.

## 16. Conclusion

CampusAssist demonstrates an end-to-end student information retrieval prototype, covering data preparation, feature engineering, lexical and semantic retrieval, application development, cloud deployment, system integration, testing, and performance optimization.

Both retrieval models achieved perfect aggregate metrics on the 12 answerable questions in the controlled evaluation. The automated artifact validation suite passed all 13 tests, and caching semantic title embeddings improved measured local warm-query performance.

The project also identified important limitations, particularly unreliable abstention, limited dataset size, and the absence of formal stakeholder and production-scale testing.

CampusAssist is suitable as an educational demonstration of retrieval techniques. Additional data, validation, security controls, and operational testing are required before production use.

## 17. Supporting Project Documentation

- `README.md`
- `docs/TEST_PLAN.md`
- `docs/TESTING_AND_VALIDATION_REPORT.md`
- `docs/testing/TEST_RESULTS.md`
- `docs/testing/SECURITY_REVIEW_REPORT.md`
- `docs/SOLUTION_OPTIMIZATION_REPORT.md`
- `docs/USER_GUIDE.md`
- `docs/CLOUD_ARCHITECTURE.md`
- `docs/SYSTEM_INTEGRATION_REPORT.md`
- `docs/deployment/DEPLOYMENT_GUIDE.md`
- `docs/deployment/CLOUD_DEPLOYMENT_REPORT.md`


## 18. Literature Review and Technical Background

This section presents a focused review of the concepts and technologies used in CampusAssist.

### 18.1 Information Retrieval and TF-IDF

Information retrieval systems identify and rank documents relevant to a user's information need. Traditional lexical retrieval methods represent documents using terms and assign weights based on their occurrence and distribution.

Salton and Buckley (1988) discussed term-weighting approaches for automatic text retrieval and established the importance of effective term weighting in document search. TF-IDF is a widely used approach that gives greater importance to terms that are informative within a document collection.

CampusAssist uses scikit-learn's TfidfVectorizer with English stop-word removal and unigrams and bigrams. This provides a lightweight lexical baseline for comparison with semantic retrieval.

### 18.2 Semantic Search and Sentence Embeddings

Keyword-based retrieval can have difficulty matching queries and documents that express similar meanings using different words. Semantic retrieval addresses this limitation by representing text as numerical embeddings.

Reimers and Gurevych (2019) introduced Sentence-BERT, which produces sentence embeddings that can be compared using cosine similarity. Their work supports the use of sentence-level representations for semantic similarity and retrieval tasks.

CampusAssist uses the pretrained sentence-transformers/all-MiniLM-L6-v2 model. Its model card describes 384-dimensional sentence and paragraph embeddings intended for semantic search and similarity tasks. The model is used for inference; it is not fine-tuned as part of this project.

### 18.3 Similarity-Based Ranking

Cosine similarity measures the orientation between two vectors and is commonly used to compare normalized text representations. Scikit-learn documents cosine similarity as the normalized dot product of vectors.

CampusAssist uses cosine similarity for TF-IDF retrieval and normalized embedding dot products for semantic retrieval. Semantic ranking combines content and title similarity with equal weights:

- Content similarity weight: 0.5
- Title similarity weight: 0.5

This design allows both the document title and its content to influence the final ranking.

### 18.4 Application and Cloud Deployment

Streamlit provides a Python framework for building interactive data applications. Streamlit Community Cloud supports deployment from GitHub repositories and provides a hosted application URL.

CampusAssist uses Streamlit for its search interface and Streamlit Community Cloud for hosting. The application is connected to the project's GitHub repository.

### 18.5 Relevance to the Project

The reviewed concepts informed the choice to implement both a traditional lexical baseline and a pretrained semantic retrieval model. Comparing the approaches provides a practical demonstration of how different representations can support information discovery.

This review is focused on the technologies directly used in the prototype. It is not a systematic literature review, and the small project evaluation should not be interpreted as a general comparison of retrieval algorithms.

## 19. Requirements Analysis

### 19.1 Functional Requirements

The system was designed to meet the following functional requirements:

1. Load the prepared document collection.
2. Accept a natural-language search question.
3. Allow users to select TF-IDF or Sentence Transformers retrieval.
4. Allow users to choose the number of results to display.
5. Rank documents according to retrieval similarity.
6. Display document titles, identifiers, categories, content, and similarity scores.
7. Validate empty questions and questions exceeding the configured length limit.
8. Provide access through a browser-based interface.

### 19.2 Non-Functional Requirements

The project considered the following non-functional requirements:

- Usability: provide a simple interface for submitting questions and reviewing results.
- Performance: avoid unnecessary repeated computation during retrieval.
- Maintainability: keep application code, data, models, scripts, and documentation organized.
- Reproducibility: retain prepared datasets, model artifacts, evaluation files, and configuration.
- Portability: document local setup and deployment dependencies.
- Transparency: disclose the synthetic nature of the dataset and explain the limitations of similarity scores.
- Security awareness: exclude common local secret files through Git ignore rules and validate user input.

### 19.3 Constraints

The prototype operates with a small synthetic dataset, limited evaluation questions, and a lightweight cloud-hosted environment. Authentication, role-based access control, production monitoring, and formal security certification are outside the implemented scope.

## 20. Research Findings and Design Decisions

The project adopted a comparative retrieval approach rather than relying on only one model.

TF-IDF was selected as a transparent and computationally inexpensive lexical baseline. Sentence Transformers was selected to demonstrate semantic representations and retrieval across differently worded queries.

The pretrained MiniLM model was selected because it provides compact 384-dimensional embeddings suitable for semantic similarity tasks. The project did not undertake model fine-tuning because the available synthetic dataset was too small to support meaningful training.

Streamlit was selected to develop the interface using Python without requiring a separate frontend application. Streamlit Community Cloud was used to make the prototype accessible through a hosted URL.

The system displays retrieved source content instead of generating unsupported natural-language answers. This keeps the retrieval process inspectable and makes it easier for users to verify the source material.

The final design represents a balance between implementation simplicity, demonstrability, and the available project resources.

## 21. Project Outcomes Against Objectives

| Project objective | Outcome |
|---|---|
| Prepare structured data | Completed for 12 synthetic documents |
| Perform EDA and feature engineering | Five descriptive features prepared |
| Implement lexical retrieval | TF-IDF implemented |
| Implement semantic retrieval | Pretrained MiniLM embeddings implemented |
| Evaluate retrieval models | 12 answerable questions evaluated |
| Develop a user interface | Streamlit application implemented |
| Deploy to the cloud | Streamlit Community Cloud deployment completed |
| Integrate system components | Data, model artifacts, and application integrated |
| Validate project artifacts | 13 automated artifact tests passed |
| Optimize retrieval performance | Title embedding caching implemented and benchmarked |
| Document the project | Technical, testing, deployment, and user documentation prepared |

The evaluation achieved Top-1 Accuracy, MRR, and Recall@3 of 1.00 for both models on the 12 answerable evaluation questions. These results apply only to the controlled evaluation dataset.

The three unanswerable questions exposed an important limitation: both models returned ranked documents instead of reliably abstaining. Therefore, the project demonstrates a functioning retrieval prototype, but does not establish reliable handling of unknown or unsupported questions.

## 22. Lessons Learned and Reflection

### 22.1 Project Achievements

The project brought together data preparation, exploratory analysis, feature engineering, machine learning, application development, cloud deployment, testing, and documentation in one integrated prototype.

It also provided practical experience in comparing lexical and semantic retrieval methods and interpreting evaluation metrics within the limits of a small dataset.

### 22.2 Challenges and Problem-Solving

Several challenges were encountered during development:

- Dependency compatibility: cloud deployment required careful dependency and Python environment configuration. Version pinning and CPU-compatible PyTorch dependencies were used for the deployed environment.
- Retrieval relevance: an FAQ query did not initially rank its expected document first in semantic retrieval. Combining title and content similarity improved the ranking for the tested query.
- Performance: title embeddings were initially recomputed during each semantic search. Caching these embeddings reduced repeated computation.
- Unsupported questions: evaluation showed that both models returned documents for unanswerable questions. This was documented rather than hidden through an arbitrary similarity threshold.
- Integration: the prepared datasets, model artifacts, and Streamlit application required consistency checks to ensure that their dimensions and document ordering matched.

### 22.3 Skills Developed

The project provided practical experience in:

- Python programming and data processing.
- Exploratory data analysis and feature engineering.
- Text vectorization and semantic embeddings.
- Retrieval evaluation using ranking metrics.
- Streamlit application development.
- Cloud deployment and dependency management.
- Automated testing and performance benchmarking.
- Git version control and technical documentation.
- Communicating technical limitations and project outcomes.

### 22.4 What Could Be Done Differently

A future project iteration would begin with a larger and more representative dataset, clearer stakeholder requirements, and a broader evaluation set. Evaluation questions would include paraphrases, ambiguous queries, and realistic unsupported questions.

Formal user acceptance testing would be planned earlier. Performance and security testing would also be included as explicit project activities rather than relying only on local benchmarks and configuration reviews.

## 23. Conclusions and Recommendations

CampusAssist demonstrates how data preparation, lexical retrieval, semantic embeddings, and cloud application development can be combined into a student information retrieval prototype.

The project achieved its principal educational and technical objectives within the defined prototype scope. The implementation supports document retrieval through two approaches, provides a browser-based interface, and includes documented testing and optimization activities.

The following recommendations are proposed before any real-world deployment:

1. Replace synthetic examples with approved, verified academic information.
2. Expand and diversify the evaluation dataset.
3. Develop and calibrate model-specific abstention behaviour.
4. Conduct formal stakeholder user acceptance testing.
5. Introduce authentication and access control where required.
6. Conduct security, privacy, and load testing.
7. Establish operational monitoring and maintenance procedures.
8. Evaluate additional retrieval methods using a larger benchmark.

## 24. References

1. Salton, G., & Buckley, C. (1988). Term-weighting approaches in automatic text retrieval. Information Processing & Management, 24(5), 513–523. https://doi.org/10.1016/0306-4573(88)90021-0

2. Reimers, N., & Gurevych, I. (2019). Sentence-BERT: Sentence embeddings using Siamese BERT-networks. Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing. https://arxiv.org/abs/1908.10084

3. scikit-learn developers. (n.d.). TfidfVectorizer documentation. https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html

4. scikit-learn developers. (n.d.). Cosine similarity documentation. https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html

5. Sentence Transformers. (n.d.). all-MiniLM-L6-v2 model card. Hugging Face. https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2

6. Streamlit. (n.d.). Streamlit Community Cloud documentation. https://docs.streamlit.io/deploy/streamlit-community-cloud

7. Streamlit. (n.d.). Deploy your app on Community Cloud. https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy

## 25. Appendices

### Appendix A – Project Repository

Source code, datasets, model artifacts, scripts, reports, and diagrams are maintained in the CampusAssist GitHub repository:

https://github.com/Vanshika-Oberoi/CampusAssist

### Appendix B – Application

Live prototype:

https://campusassist.streamlit.app

### Appendix C – Supporting Evidence

The following project files provide supplementary technical evidence:

- `reports/model_comparison.csv` – retrieval evaluation metrics.
- `reports/retrieval_evaluation_results.csv` – per-question evaluation results.
- `reports/performance_benchmark.csv` – local retrieval benchmark measurements.
- `docs/testing/TEST_RESULTS.md` – automated and retrieval validation results.
- `docs/testing/SECURITY_REVIEW_REPORT.md` – limited security review.
- `docs/diagrams/` – editable architecture diagrams.
- `tests/` – automated artifact validation and benchmark scripts.

### Appendix D – Evaluation and Testing Scope

The evaluation used 15 questions, of which 12 were answerable and 3 were unanswerable. Aggregate ranking metrics were calculated over the answerable questions only. The automated artifact validation suite contained 13 tests.

No formal stakeholder UAT, penetration test, or production-scale load test is claimed in this report.
