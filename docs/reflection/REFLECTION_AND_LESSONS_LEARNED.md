# CampusAssist
## Reflection and Lessons Learned Report

**Project:** AI-Powered Student Information Retrieval Assistant
**Repository:** https://github.com/Vanshika-Oberoi/CampusAssist
**Application:** https://campusassist.streamlit.app

---

## 1. Introduction

This report reflects on the development of CampusAssist throughout the capstone project. The project provided an opportunity to apply concepts from data science, artificial intelligence, cloud computing, data engineering, software development, testing, and project management.

CampusAssist was developed as an educational student information retrieval prototype. It combines structured document preparation, lexical and semantic retrieval, a Streamlit interface, and cloud deployment.

## 2. Project Achievements

The principal achievements were:

- Prepared a structured collection of 12 synthetic academic information documents.
- Completed data cleaning, exploratory analysis, and feature engineering.
- Implemented TF-IDF lexical retrieval.
- Implemented semantic retrieval using a pretrained Sentence Transformers model.
- Developed a Streamlit application for searching and comparing retrieval models.
- Deployed the prototype using Streamlit Community Cloud.
- Integrated document data, model artifacts, and application components.
- Evaluated retrieval using 15 questions, including 12 answerable and 3 unanswerable questions.
- Achieved Top-1 Accuracy, MRR, and Recall@3 of 1.00 for both models on the 12 answerable questions.
- Created automated artifact validation tests, with all 13 tests passing.
- Optimized repeated semantic retrieval by caching title embeddings.
- Prepared technical documentation, architecture diagrams, testing reports, deployment instructions, and a user guide.

These achievements demonstrate completion of the principal technical components within the defined prototype scope.

## 3. Challenges Encountered

### 3.1 Dataset Limitations

A major challenge was working with a small synthetic dataset. The 12 documents were sufficient to demonstrate the retrieval workflow but did not represent the diversity of real academic information.

**Response:** The dataset was structured consistently, and its synthetic nature was disclosed in the application and documentation.

### 3.2 Retrieval Quality

The initial semantic retrieval approach did not always rank the expected document first for every tested query.

**Response:** Title similarity was incorporated alongside content similarity using equal weights. This improved the ranking of the tested FAQ query.

### 3.3 Dependency and Cloud Deployment Issues

The application required compatible Python and machine-learning dependencies for the cloud environment. PyTorch compatibility and deployment configuration required attention.

**Response:** Dependency versions and CPU-compatible PyTorch configuration were documented for the hosted environment.

### 3.4 Repeated Computation

The semantic retrieval implementation initially encoded document titles during each search operation, introducing unnecessary repeated work.

**Response:** Title embeddings were cached so subsequent searches could reuse the precomputed representations. The local warm-query benchmark showed a reduction in average semantic retrieval time from 81.4 ms to 7.9 ms.

### 3.5 Unsupported Questions

The evaluation showed that both retrieval models returned documents even when questions were not answerable from the dataset.

**Response:** This limitation was recorded in the testing reports. An arbitrary similarity threshold was not introduced because the observed score distributions overlapped between answerable and unanswerable questions.

## 4. Problem-Solving Approaches

The project used an incremental development approach:

1. Inspect and understand the available source data.
2. Prepare and validate the document dataset.
3. Establish a lexical retrieval baseline.
4. Implement semantic retrieval.
5. Compare retrieval approaches using defined ranking metrics.
6. Integrate retrieval components into the Streamlit application.
7. Deploy the application and verify representative workflows.
8. Run automated artifact checks and manual application checks.
9. Benchmark performance and optimize repeated computation.
10. Document results, limitations, and future improvements.

Breaking the work into stages helped identify issues closer to their source and reduced unnecessary changes to already validated artifacts.

## 5. Skills Developed

### 5.1 Data Science and Data Engineering

Experience was gained in data cleaning, structured data preparation, feature engineering, exploratory analysis, dataset validation, and maintaining consistent data artifacts.

### 5.2 Artificial Intelligence and Machine Learning

The project strengthened understanding of TF-IDF, sentence embeddings, cosine similarity, semantic search, ranking metrics, and the practical differences between lexical and semantic retrieval.

### 5.3 Software Development

Developing the Streamlit application provided experience in Python application structure, input validation, error handling, caching, dependency management, and integration of machine-learning artifacts.

### 5.4 Cloud Computing and Deployment

Deploying the application provided practical exposure to GitHub-connected cloud deployment, environment configuration, dependency compatibility, and hosted application verification.

### 5.5 Testing and Project Management

The project developed skills in test planning, automated validation, defect documentation, performance benchmarking, version control, technical writing, and organizing deliverables across project milestones.

## 6. Evaluation of Project Objectives

The core objectives of preparing data, implementing two retrieval approaches, developing the interface, deploying the prototype, integrating its components, and documenting the results were achieved.

However, successful completion of these objectives does not mean the prototype is production-ready.

The evaluation was performed on a small controlled dataset. Unsupported-question handling remains unreliable, and formal stakeholder UAT, penetration testing, and production-scale load testing were not performed.

The project should therefore be considered a completed educational prototype with clearly identified opportunities for further development.

## 7. Lessons Learned

The most important lessons from this project were:

1. Data quality and dataset diversity strongly influence the usefulness of retrieval systems.
2. High evaluation scores on a small dataset do not guarantee performance on real-world information.
3. Lexical and semantic retrieval approaches have different strengths and should be evaluated against realistic questions.
4. Similarity scores should not automatically be interpreted as factual confidence.
5. Caching repeated computations can improve performance without changing the underlying retrieval model.
6. Cloud deployment requires attention to dependency versions and runtime compatibility.
7. Testing unsupported inputs is as important as testing expected successful workflows.
8. Clear documentation of limitations is part of responsible technical delivery.
9. Incremental integration and version control make complex project work easier to manage.

## 8. What Could Be Done Differently

If the project were started again, the following improvements would be made:

- Gather approved and representative academic documents earlier.
- Define stakeholder requirements and acceptance criteria before implementation.
- Prepare a larger evaluation dataset with paraphrased and unsupported questions.
- Establish baseline performance measurements before optimization.
- Plan user acceptance testing with representative users.
- Include formal security and load testing in the project schedule.
- Introduce model-specific abstention evaluation from the beginning.
- Maintain a structured record of test evidence and design decisions throughout development.

## 9. Future Development Opportunities

Future development could include:

- Expanding the knowledge base using verified university information.
- Improving chunking and metadata-based retrieval.
- Comparing additional embedding models and hybrid retrieval techniques.
- Calibrating abstention behaviour using a representative validation dataset.
- Adding source-grounded answer generation as an optional feature.
- Introducing authentication and role-based access control.
- Adding usage analytics, monitoring, and operational logging.
- Conducting formal usability and accessibility evaluation.

Any future generative answer layer should cite retrieved source material and communicate when the available documents do not contain sufficient information.

## 10. Overall Reflection

CampusAssist provided practical experience in taking a data and AI concept through preparation, implementation, evaluation, integration, deployment, and documentation.

The project demonstrated that building a working prototype involves more than selecting a machine-learning model. Data quality, evaluation design, software reliability, deployment compatibility, user experience, and transparent communication of limitations are equally important.

The most valuable outcome was developing an understanding of the complete lifecycle of a small AI-enabled application and learning how to identify and communicate areas where additional evidence or engineering work is needed.

## 11. Conclusion

The CampusAssist capstone achieved its main educational objectives and provided an opportunity to apply concepts from the Bachelor of Science in Data Science, Artificial Intelligence, and Cloud Computing programme.

The experience strengthened technical problem-solving, analytical thinking, software development, cloud deployment, testing, and communication skills. It also highlighted the importance of realistic evaluation, responsible system design, and continuous improvement.

---

**Document status:** Prepared for final capstone review. Add any personal learning examples, institution-required declarations, and supervisor feedback before submission.
