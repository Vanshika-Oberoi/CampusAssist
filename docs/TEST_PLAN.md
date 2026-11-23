# CampusAssist – Module 7 Test Plan

## 1. Purpose

This test plan defines the strategy for validating CampusAssist before final capstone delivery. Testing covers data processing, retrieval models, application functionality, performance, security, usability, and operational readiness.

CampusAssist is a retrieval-based prototype using 12 synthetic sample documents. It retrieves and ranks document chunks; it does not generate answers using an LLM.

## 2. Testing Objectives

- Verify that prepared data and model artifacts are complete and consistent.
- Validate retrieval relevance using the existing evaluation dataset.
- Verify application workflows, input validation, and result presentation.
- Measure retrieval response time and model inference performance.
- Review security, privacy, and repository configuration.
- Evaluate usability through representative student scenarios.
- Identify defects and implement evidence-based improvements.
- Prepare reproducible testing evidence for final delivery.

## 3. Testing Scope

### In Scope

- Data preparation outputs and document chunk structure.
- TF-IDF and Sentence Transformers retrieval.
- Retrieval ranking and evaluation metrics.
- Streamlit application workflows and user interface.
- Empty input, long input, and unsupported questions.
- Response time and local resource observations.
- Input validation, secret handling, and synthetic-data safeguards.
- User task completion and usability review.
- Documentation and deployment verification.

### Out of Scope

- Production university data or confidential student records.
- Real institutional policy verification.
- Authentication and role-based access control, which are not implemented.
- Formal regulatory certification or penetration testing.
- Large-scale production load testing.
- LLM-generated answer evaluation, because the application does not generate answers.

## 4. Test Environment

- Operating system: macOS development environment.
- Python: system Python 3.10.7.
- Application: Streamlit.
- Retrieval models: TF-IDF and sentence-transformers/all-MiniLM-L6-v2.
- Dataset: 12 synthetic documents.
- Evaluation dataset: 15 questions (12 answerable and 3 unanswerable).
- Deployment: Streamlit Community Cloud.
- Repository: https://github.com/Vanshika-Oberoi/CampusAssist

Tests should record the environment, selected model, query, top-k setting, observed result, and execution time where applicable.

## 5. Testing Types and Methods

| Testing type | Method | Evidence |
|---|---|---|
| Data validation | Schema, row count, missing-value and artifact consistency checks | Command output and validation results |
| Model validation | Evaluate expected document ranking for answerable questions | Evaluation CSV and metrics |
| Functional testing | Execute application workflows and input scenarios | Test case results |
| Performance testing | Measure retrieval and application response times | Timing results and environment details |
| Security review | Inspect input validation, secret patterns and data exposure | Configuration review |
| Usability/UAT | Execute representative student tasks and collect feedback | Task outcomes and feedback |
| Regression testing | Repeat core tests after code changes | Before/after test results |

## 6. Test Scenarios and Cases

| ID | Area | Test scenario | Expected result / success criterion |
|---|---|---|---|
| TC01 | Data | Load document chunks | 12 documents load successfully |
| TC02 | Data | Verify required columns | All required document fields exist |
| TC03 | Models | Verify semantic embeddings | 12 rows and 384 dimensions |
| TC04 | Models | Verify TF-IDF vectors | 12 rows and matching vectorizer features |
| TC05 | Retrieval | Run answerable course query | Expected document appears at rank 1 |
| TC06 | Retrieval | Run assignment FAQ query | Expected document appears in top 3 |
| TC07 | Retrieval | Evaluate all answerable questions | Report top-1 accuracy, MRR and recall@3 |
| TC08 | Retrieval | Evaluate unanswerable questions | Record whether unsupported questions are incorrectly presented as relevant; abstention is not assumed |
| TC09 | UI | Submit an empty question | Warning is displayed; search is not performed |
| TC10 | UI | Submit a question over 1,000 characters | Input is rejected with a warning |
| TC11 | UI | Select TF-IDF model | TF-IDF results are displayed |
| TC12 | UI | Select Sentence Transformers | Semantic retrieval results are displayed |
| TC13 | UI | Change top-k from 1 to 5 | Result count respects selected value |
| TC14 | UI | Inspect retrieved result | Title, document ID, category, chunk ID and score are displayed |
| TC15 | Performance | Measure query retrieval time | Baseline recorded for both models |
| TC16 | Performance | Repeat representative queries | Timing variation and failures are recorded |
| TC17 | Security | Inspect input validation | Empty and oversized input are rejected |
| TC18 | Security | Inspect secret handling | Secret files and environment files are covered by ignore rules |
| TC19 | Security | Review displayed data | Only synthetic sample content is used and disclaimer is visible |
| TC20 | UAT | Complete representative student information tasks | User can locate and understand relevant source content |
| TC21 | Deployment | Open deployed Streamlit application | Application loads and core search workflow works |
| TC22 | Regression | Repeat core functional tests after changes | Previously passing core tests continue to pass |

## 7. Success Criteria

- Required data files and model artifacts load without errors.
- Data and embedding dimensions match the document collection.
- Retrieval metrics are calculated and documented on the answerable evaluation set.
- Expected documents appear within the specified ranking thresholds for the selected test scenarios.
- Empty and oversized inputs are rejected.
- Both retrieval models and supported top-k settings work.
- Performance measurements are documented with their environment and methodology.
- Security limitations are clearly identified; no unsupported security claims are made.
- UAT feedback and task outcomes are recorded, with simulated testing distinguished from stakeholder approval.
- Critical defects discovered during testing are fixed or explicitly documented as unresolved.
- Regression tests pass after implemented changes.

## 8. Testing Schedule

| Phase | Activity | Planned sequence |
|---|---|---|
| 1 | Test strategy and test plan | First |
| 2 | Data and model validation | Second |
| 3 | Functional and UI testing | Third |
| 4 | Performance evaluation | Fourth |
| 5 | Security and governance review | Fifth |
| 6 | UAT and usability evaluation | Sixth |
| 7 | Optimization and regression testing | Seventh |
| 8 | Reports, user guide and presentation package | Final |

## 9. Defect Tracking and Resolution

Each issue will be recorded with:
- Issue ID and description.
- Test case where it was identified.
- Severity and impact.
- Steps to reproduce.
- Expected and actual result.
- Corrective action.
- Retest result and final status.

Severity levels:
- Critical: application unusable or serious data/security exposure.
- High: major core workflow failure.
- Medium: partial functionality or significant usability/performance issue.
- Low: minor usability or documentation issue.

A fix is considered verified only after the affected test case is repeated successfully.

## 10. Risks and Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| Small synthetic dataset | Results may not generalize | State dataset limitations and avoid production claims |
| Unsupported questions retrieve unrelated documents | Misleading user experience | Test abstention explicitly and document the current limitation |
| Different models rank results differently | Inconsistent retrieval experience | Evaluate both models independently |
| Model download or dependency issues | Application startup failure | Record environment and verify dependencies |
| Cloud resource constraints | Slow first request or inference | Measure cold and warm behaviour separately |
| No authentication or access control | Unsuitable for confidential data | Restrict prototype to synthetic public demonstration data |
| No real stakeholder feedback | UAT evidence may be limited | Label simulated task evaluation honestly and record actual feedback if available |

## 11. Reporting and Evidence

Testing results will be stored under `docs/testing/` and `reports/`. Evidence may include:
- Test execution tables and status.
- Evaluation metrics and question-level results.
- Response-time measurements.
- Security review findings.
- UAT task outcomes and feedback.
- Defect and retest records.

No test will be marked as passed without observed evidence.

## 12. Approval and Readiness

This document defines the planned validation approach. It is not itself evidence that all tests have passed. Final readiness will be determined from the completed test results, unresolved risks, optimization report, and regression outcomes.
