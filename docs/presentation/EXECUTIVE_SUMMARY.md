# CampusAssist – Executive Summary

## 1. Project Overview

CampusAssist is an AI-powered student information retrieval prototype designed to help students find relevant information from academic documents, including course guides, assignment instructions, frequently asked questions, and policy examples.

The project demonstrates how information retrieval techniques can make academic information easier to search and discover through a simple web application.

## 2. Problem and Business Value

Students may need to search through multiple documents to find information about assignments, courses, and academic procedures. This can make information discovery time-consuming and inconvenient.

CampusAssist explores a centralized search approach that allows users to enter a question and retrieve relevant document sections. Its potential value is reducing the effort involved in locating information and providing a foundation for more accessible student support services.

No institutional time savings or student satisfaction improvements have been measured at this prototype stage.

## 3. Solution Overview

CampusAssist provides two retrieval approaches:

- **Keyword-based search:** Finds documents using matching terms through TF-IDF.
- **Meaning-based search:** Uses a pretrained language model to identify documents with similar meaning, even when the wording differs.

The application ranks relevant document results in a Streamlit interface. It also includes data preparation, document chunking, model evaluation, automated validation, performance benchmarking, and cloud deployment.

## 4. Key Project Outcomes

| Measure | Result |
|---|---:|
| Synthetic sample documents | 12 |
| Evaluation questions | 15 |
| Answerable evaluation questions | 12 |
| Automated artifact tests passed | 13/13 |
| TF-IDF Top-1 Accuracy | 1.00 |
| Semantic Top-1 Accuracy | 1.00 |
| TF-IDF MRR | 1.00 |
| Semantic MRR | 1.00 |
| TF-IDF Recall@3 | 1.00 |
| Semantic Recall@3 | 1.00 |

The retrieval metrics were calculated using only the 12 answerable questions. The three unanswerable questions were excluded from these metrics.

## 5. Performance Improvement

An optimization that caches semantic title embeddings reduced average local warm-query retrieval time from 0.0814 seconds to 0.0079 seconds in a benchmark of five representative queries per model. This represents an approximate 90.3% reduction.

These are local benchmark measurements, not guaranteed cloud response times.

## 6. Recommendations

Before considering institutional adoption, the following improvements are recommended:

- Expand the document collection using verified and approved academic information.
- Evaluate retrieval quality with a larger and more diverse question set.
- Improve handling of questions for which the document collection has no relevant answer.
- Introduce authentication and role-based access controls if confidential or institution-specific information is used.
- Conduct stakeholder acceptance testing, security testing, and load testing.
- Establish a process for reviewing and updating academic documents.

## 7. Future Opportunities

Future development could include integration with university portals or learning management systems, additional document formats, multilingual search, improved relevance feedback, and carefully validated answer generation.

These enhancements would require further testing and appropriate data governance.

## 8. Important Limitations

CampusAssist is a demonstration prototype, not a production-ready university service.

- The current collection contains only 12 synthetic documents.
- Unsupported questions still receive retrieved results; reliable abstention is not implemented.
- Similarity scores do not represent factual confidence.
- The application retrieves source documents and does not generate LLM-based answers.
- Authentication and role-based access control are not implemented.
- Formal stakeholder UAT, penetration testing, and production-scale load testing were not performed.

## 9. Conclusion

CampusAssist demonstrates an end-to-end approach to student information retrieval, covering data preparation, retrieval model development, evaluation, application development, cloud deployment, and performance optimization.

The prototype achieved perfect retrieval metrics on its limited answerable evaluation set and passed all 13 automated artifact validation tests. It provides a foundation for further exploration of accessible academic information search, while broader data, stakeholder, security, and performance validation remain necessary.

## 10. Project Links

- Live application: https://campusassist.streamlit.app
- GitHub repository: https://github.com/Vanshika-Oberoi/CampusAssist
