# CampusAssist – Module 7 Test Results

## 1. Test Execution Summary

| Item | Result |
|---|---|
| Automated test framework | Python unittest |
| Automated tests executed | 13 |
| Automated tests passed | 13 |
| Automated tests failed | 0 |
| Execution time | Approximately 1 second |
| Test outcome | Passed |

## 2. Automated Validation Results

The following checks passed:

- Document count: 12.
- Document identifiers are unique.
- Required document columns are present.
- Evaluation question count: 15.
- Answerable questions: 12.
- Unanswerable questions: 3.
- Semantic embedding shape: 12 × 384.
- Semantic embeddings contain finite values.
- TF-IDF document vector count matches the document count.
- TF-IDF feature count matches the fitted vectorizer.
- Evaluation results include both retrieval models.
- Model comparison metrics are consistent with the saved evaluation results.
- Model configuration matches the project dataset and embedding dimensions.

## 3. Existing Retrieval Evaluation

The saved model comparison reports the following metrics over the 12 answerable questions:

| Metric | TF-IDF | Sentence Transformers |
|---|---:|---:|
| Top-1 Accuracy | 1.00 | 1.00 |
| Mean Reciprocal Rank | 1.00 | 1.00 |
| Recall@3 | 1.00 | 1.00 |

These are results on a small, controlled synthetic dataset. They should not be interpreted as evidence of production-level retrieval quality.

## 4. Unanswerable Query Validation

Three questions are labelled unanswerable in the evaluation dataset. The saved evaluation results show that both retrieval models still return a document for every such question.

| Question | TF-IDF Retrieved | TF-IDF Score | Semantic Retrieved | Semantic Score |
|---|---|---:|---|---:|
| Q013 | DOC005 | 0.3218 | DOC005 | 0.4595 |
| Q014 | DOC001 | 0.3868 | DOC004 | 0.5242 |
| Q015 | DOC012 | 0.2198 | DOC011 | 0.5615 |

**Result: Abstention validation failed.**

The current application does not implement a reliable mechanism to decline unsupported questions. It displays retrieved documents even when the requested information is not represented in the corpus.

## 5. Similarity Score Analysis

| Model | Answerable Range | Unanswerable Range |
|---|---|---|
| TF-IDF | 0.1596–0.5558 | 0.2198–0.3868 |
| Sentence Transformers | 0.5600–0.8243 | 0.4595–0.5615 |

The ranges overlap. A universal similarity threshold is therefore not justified by this small dataset. Introducing a threshold without further validation could reject valid questions.

## 6. Limitations and Follow-up Actions

1. Expand the evaluation dataset with more answerable and unanswerable questions.
2. Include paraphrased, ambiguous, and out-of-domain queries.
3. Evaluate abstention precision, recall, and false rejection rates.
4. Investigate model-specific confidence calibration or a validated abstention mechanism.
5. Conduct usability testing with actual student users.
6. Perform dedicated security and performance testing before production use.

## 7. Evidence and Scope

This report records automated artifact validation and previously saved retrieval evaluation results.

The 13 automated tests were executed locally using Python unittest. The existing model evaluation metrics were read from saved CSV reports; the model training pipeline was not rerun.

The unanswerable-query results are observed failures, not passing tests. This report does not claim formal stakeholder UAT, penetration testing, or production readiness.
