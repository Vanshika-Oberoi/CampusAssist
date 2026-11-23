# CampusAssist – Cloud Deployment Report

**Project:** CampusAssist  
**Module:** 5 – Cloud Deployment  
**Deployment Platform:** Streamlit Community Cloud  
**Deployment Date:** November 2026  
**Status:** Successfully deployed and tested

## 1. Deployment Overview

CampusAssist was deployed as a cloud-hosted student information assistant using Streamlit Community Cloud.

The application allows users to search a collection of synthetic student information documents using two retrieval models:

- Sentence Transformers (semantic retrieval)
- TF-IDF (keyword-based retrieval)

Live application: https://campusassist.streamlit.app

GitHub repository: https://github.com/Vanshika-Oberoi/CampusAssist

## 2. Deployment Environment

| Item | Configuration |
|---|---|
| Hosting platform | Streamlit Community Cloud |
| Source control | GitHub |
| Repository branch | main |
| Runtime | Python 3.11 |
| Application entry point | app.py |
| Application framework | Streamlit 1.65.0 |
| Data format | CSV |
| Semantic model | sentence-transformers/all-MiniLM-L6-v2 |
| Machine learning library | Sentence Transformers |
| Numerical processing | NumPy |
| Data processing | Pandas |
| Keyword retrieval | Scikit-learn TF-IDF |

Dependencies are defined in the repository's requirements.txt file.

## 3. Deployment Process

### Step 1: Application Preparation

The Streamlit application was created in app.py.

The application includes:
- A student query interface.
- Retrieval model selection.
- A configurable top-k results setting.
- Document ranking and similarity scores.
- Retrieved document content display.
- Input validation and error handling.

### Step 2: Dependency Configuration

A requirements.txt file was created to define application dependencies.

CPU-only PyTorch dependencies were configured to avoid unnecessary GPU package installation in the cloud environment.

### Step 3: Version Control

The application source code, requirements and required data/model artifacts were maintained in GitHub.

The repository's main branch was connected to Streamlit Community Cloud.

### Step 4: Cloud Configuration

The application was configured to use Python 3.11.

The cloud platform installed the required dependencies and launched app.py.

### Step 5: Deployment

The application was successfully deployed at:

https://campusassist.streamlit.app

### Step 6: Application Verification

The deployed application was opened in a browser and tested using student information queries.

### Step 7: Retrieval Improvement

Testing revealed that the original semantic retrieval method did not rank a relevant assignment FAQ within the top three results for one query.

The retrieval method was improved by combining title similarity and content similarity:

Final Score = (0.5 × Title Similarity) + (0.5 × Content Similarity)

The updated application was tested locally, committed to GitHub and successfully redeployed.

## 4. Functional Testing Results

| Test | Expected Result | Observed Result | Status |
|---|---|---|---|
| Introduction to AI query | DOC002 ranked first | DOC002 ranked first | Passed |
| Assignment report query | DOC005 ranked first | DOC005 ranked first | Passed |
| Assignment submission query after improvement | DOC007 ranked first | DOC007 ranked first | Passed |
| TF-IDF assignment query | Relevant assignment documents retrieved | DOC005 ranked first | Passed |
| Semantic retrieval | Relevant documents ranked and displayed | Working | Passed |
| Cloud application loading | Application accessible through public URL | Working | Passed |
| Updated cloud deployment | Latest retrieval improvement available | Verified | Passed |

These tests validate the demonstrated queries and application functionality. They do not establish production-level retrieval accuracy.

## 5. Deployment Improvement Evidence

For the query:

"How can students submit their assignments?"

Original semantic retrieval ranked DOC007 fourth, outside the default top three.

After combining title and content similarity:

| Document | Combined Similarity | Rank |
|---|---:|---:|
| DOC007 – Assignment FAQ | 0.5809 | 1 |
| DOC005 – AI Project Submission | 0.4835 | 2 |
| DOC011 – Assignment Extension Guidelines | 0.4622 | 3 |

The correct FAQ was ranked first in both local and cloud testing after deployment.

A separate course-guide regression test also returned DOC002 as the top result.

## 6. Version Control and Deployment History

Important Git commits include:

| Commit | Description |
|---|---|
| ffc48f8 | Add CampusAssist Streamlit application and deployment dependencies |
| 47021c8 | Use CPU-only PyTorch for cloud deployment |
| e9eebeb | Improve semantic retrieval using title and content scores |

The latest retrieval improvement was pushed to the main branch and verified on the live application.

## 7. Security and Operational Considerations

Implemented:
- Environment and secret-file patterns are excluded through .gitignore.
- Empty queries are rejected.
- Query input is limited to 1000 characters.
- Errors during retrieval are handled and displayed.
- Synthetic data is clearly identified in the application.

Not implemented:
- User authentication.
- Role-based access control.
- Dedicated cloud database or object storage.
- Advanced monitoring and alerting.
- Infrastructure as Code.

Basic operational information can be inspected through Streamlit Community Cloud logs.

## 8. Deployment Limitations

- The application uses 12 synthetic sample documents.
- The dataset does not contain official university records or policies.
- The application retrieves and displays source documents; it does not generate natural-language answers using an LLM.
- Similarity scores indicate retrieval relevance and are not confidence or factual accuracy scores.
- Functional testing covers selected queries rather than a large-scale production evaluation.
- The cloud deployment depends on Streamlit Community Cloud.

## 9. Conclusion

CampusAssist was successfully deployed to Streamlit Community Cloud and verified through browser-based functional tests.

The deployment demonstrates the integration of GitHub, Python, Streamlit, machine learning-based retrieval and cloud hosting.

The project provides a working cloud-based prototype and a foundation for future improvements such as larger datasets, authentication, expanded evaluation and production-grade monitoring.
