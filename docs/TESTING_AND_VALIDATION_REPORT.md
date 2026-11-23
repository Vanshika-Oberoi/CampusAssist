# CampusAssist – Testing and Validation Report

## 1. Executive Summary

This report documents the testing and validation performed for the CampusAssist educational prototype during Module 7.

Testing covered data and model artifacts, retrieval evaluation, application input handling, unsupported questions, performance benchmarking, and a limited security review.

The existing automated artifact validation suite passed all 13 tests. Both retrieval models achieved Top-1 Accuracy, Mean Reciprocal Rank (MRR), and Recall@3 of 1.00 on the 12 answerable evaluation questions.

However, unsupported questions are not reliably rejected. The application returns retrieved documents even when the expected answer is absent from the synthetic dataset. This remains an important limitation.

## 2. Testing Environment

| Component | Configuration |
|---|---|
| Operating system | macOS |
| Python | System Python 3.10.7 |
| Application | Streamlit |
| Semantic model | sentence-transformers/all-MiniLM-L6-v2 |
| Lexical model | TF-IDF |
| Dataset | 12 synthetic documents |
| Evaluation questions | 15 |
| Answerable questions | 12 |
| Unanswerable questions | 3 |

## 3. Testing Scope

Testing included:
- Dataset structure and document identifiers.
- Required document fields.
- Semantic embedding dimensions and numerical validity.
- TF-IDF vector and feature consistency.
- Existing retrieval evaluation results.
- Supported and unsupported question behaviour.
- Input validation and error handling through prior application checks.
- Local retrieval performance benchmarking.
- Basic security configuration inspection.

Formal penetration testing, production-scale load testing, and stakeholder UAT were not performed.

## 4. Automated Validation Results

The automated suite was executed using:

`python3 -m unittest discover -s tests -v`

<badge color="success">13 of 13 tests passed</badge>

The tests validated:
- Document and evaluation-question counts.
- Unique document identifiers.
- Required document columns.
- Semantic embedding shape of 12 × 384.
- Finite embedding values.
- TF-IDF feature and vector counts.
- Model configuration.
- Evaluation results for both retrieval models.
- Recorded model comparison metrics.

These tests validate stored project artifacts. They do not represent complete automated end-to-end testing of every Streamlit user interface interaction.

## 5. Retrieval Evaluation

The existing evaluation contains 15 questions: 12 answerable and 3 unanswerable.

| Metric | TF-IDF | Sentence Transformers |
|---|---:|---:|
| Top-1 Accuracy | 1.00 | 1.00 |
| MRR | 1.00 | 1.00 |
| Recall@3 | 1.00 | 1.00 |

The aggregate metrics are calculated over the 12 answerable questions only. Unanswerable questions are excluded from these aggregate scores.

The results demonstrate successful retrieval on this small, controlled evaluation set. They do not establish equivalent accuracy on a larger or real-world university dataset.

## 6. Unsupported Question Validation

Three evaluation questions have no expected answer in the dataset:
- Q013: Deadline information not present.
- Q014: Marks information not present.
- Q015: Official late-submission policy not present.

Both retrieval models returned documents for all three questions rather than abstaining.

| Model | Unsupported questions returning a document |
|---|---:|
| TF-IDF | 3 of 3 |
| Sentence Transformers | 3 of 3 |

Similarity-score analysis also showed overlap between answerable and unanswerable questions. Therefore, an arbitrary global similarity threshold cannot be justified using the current evaluation data.

**Result:** Reliable abstention is not achieved. This is a known functional limitation and requires further evaluation and calibration.

## 7. Performance Testing

A local benchmark used five representative queries per model, with warm-up before timed measurements.

| Measurement | Baseline | Optimized |
|---|---:|---:|
| Semantic average query time | 0.0814 s | 0.0079 s |
| Semantic minimum | 0.0156 s | 0.0066 s |
| Semantic maximum | 0.3390 s | 0.0092 s |
| TF-IDF average query time | 0.0003 s | 0.0004 s |

Caching title embeddings reduced average local semantic query time by approximately 90.3%, or about 10.3 times in this benchmark.

These are local warm-query measurements, not end-to-end response times from Streamlit Cloud. The benchmark is small and does not measure concurrent users or production-scale load.

## 8. Application and Input Validation

The application includes the following input checks:
- Empty questions are rejected with a warning.
- Questions longer than 1,000 characters are rejected.
- Leading and trailing whitespace is removed.
- Retrieval errors are caught and displayed to the user.
- The application displays retrieved document metadata and similarity scores.

Previous integration testing also exercised course-related queries, assignment-related queries, and an unsupported policy query using both retrieval modes.

## 9. Security Review Summary

The limited security review verified:
- `.env`, `.env.*`, and `.streamlit/secrets.toml` exclusion patterns in `.gitignore`.
- No matching local secret files in the inspected project paths.
- No matching secret-like files tracked by Git.
- Basic input validation and retrieval error handling.

Authentication and role-based access control are not implemented. No formal penetration test or dependency vulnerability assessment was performed.

Refer to `docs/testing/SECURITY_REVIEW_REPORT.md` for the detailed findings.

## 10. Defects and Known Limitations

| ID | Finding | Status |
|---|---|---|
| VAL-01 | Unsupported questions still return documents | Open |
| VAL-02 | Small synthetic dataset limits generalization | Open |
| VAL-03 | No authentication or role-based access | Open |
| VAL-04 | No formal load or stress testing | Not performed |
| VAL-05 | No formal stakeholder UAT | Not performed |

The application is a retrieval-based prototype. It does not generate natural-language answers using an LLM.

## 11. Recommendations

1. Expand the dataset with representative university documents.
2. Add more answerable, ambiguous, and unanswerable evaluation questions.
3. Investigate model-specific abstention thresholds using a larger validation set.
4. Evaluate retrieval quality using realistic student queries and paraphrases.
5. Perform end-to-end testing in the deployed environment.
6. Conduct stakeholder UAT and document feedback.
7. Add authentication and authorization if required for real users.
8. Conduct load, stress, and security testing before production use.

## 12. Overall Conclusion

CampusAssist passed the 13 automated artifact validation tests and achieved perfect retrieval metrics on its 12 answerable evaluation questions.

The semantic retrieval optimization reduced average local warm-query time from 81.4 ms to 7.9 ms in the measured benchmark.

The testing also identified important limitations, particularly the lack of reliable abstention for unsupported questions, the small synthetic dataset, and the absence of formal stakeholder UAT and production-scale testing.

The project is suitable for educational demonstration as a retrieval-based prototype. Further validation and development are required before production use.

## 13. Supporting Evidence

- `docs/TEST_PLAN.md`
- `docs/testing/TEST_RESULTS.md`
- `docs/testing/SECURITY_REVIEW_REPORT.md`
- `docs/SOLUTION_OPTIMIZATION_REPORT.md`
- `reports/model_comparison.csv`
- `reports/retrieval_evaluation_results.csv`
- `reports/performance_benchmark.csv`
- `tests/test_artifacts.py`
- `tests/benchmark_retrieval.py`
