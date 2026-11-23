
# 🎓 CampusAssist

### AI-Powered Student Information Assistant

CampusAssist is a prototype that helps students find relevant information from course guides, assignment instructions, FAQs and policy examples.

**Live Demo:** https://campusassist.streamlit.app

**GitHub:** https://github.com/Vanshika-Oberoi/CampusAssist

> **Prototype notice:** This application uses 12 synthetic sample documents. Results are for demonstration only and are not official university information or policies.

## 1. Project Overview

CampusAssist retrieves relevant document passages in response to student questions using two approaches:

- **TF-IDF:** Lexical retrieval based on word and phrase matching.
- **Sentence Transformers:** Semantic retrieval using the pretrained `all-MiniLM-L6-v2` model.

The application ranks relevant documents and displays their content and similarity scores. It is a retrieval-based prototype, not a generative RAG chatbot.

## 2. Key Features

- Interactive Streamlit web application.
- Semantic and lexical retrieval modes.
- Configurable top-k document retrieval.
- Document title, category and content display.
- Similarity score comparison.
- Input validation.
- Cloud deployment through Streamlit Community Cloud.

## 3. Dataset

The prototype contains 12 synthetic documents.

| Category | Documents |
|---|---:|
| Course Guides | 3 |
| Assignment Instructions | 3 |
| Student FAQs | 3 |
| Policies | 3 |
| **Total** | **12** |

The evaluation dataset contains 15 questions: 12 answerable and 3 unanswerable questions.

## 4. Retrieval Model Evaluation

Both retrieval approaches achieved the following results on the 12 answerable evaluation questions:

| Metric | TF-IDF | Sentence Transformers |
|---|---:|---:|
| Top-1 Accuracy | 1.00 | 1.00 |
| Mean Reciprocal Rank | 1.00 | 1.00 |
| Recall@3 | 1.00 | 1.00 |

These results are based on a small, controlled synthetic dataset and should not be interpreted as evidence of real-world performance. Unanswerable-question abstention was not included in these aggregate metrics.

## 5. Technology Stack

- Python 3.11
- Streamlit
- Pandas and NumPy
- Scikit-learn
- Sentence Transformers
- PyTorch
- Git and GitHub
- Streamlit Community Cloud

## 6. Run Locally

Clone the repository:

```bash
git clone https://github.com/Vanshika-Oberoi/CampusAssist.git
cd CampusAssist
```

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Start the application:

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal.

## 7. Project Structure

```text
CampusAssist/
├── app.py
├── requirements.txt
├── data/
│   ├── raw/
│   ├── processed/
│   ├── chunks/
│   └── evaluation/
├── models/
├── scripts/
├── reports/
├── notebooks/
├── visualizations/
└── docs/
    ├── CLOUD_ARCHITECTURE.md
    ├── deployment/
    │   ├── CLOUD_DEPLOYMENT_REPORT.md
    │   └── DEPLOYMENT_GUIDE.md
    └── diagrams/
```

## 8. Documentation

### Final Capstone Deliverables

- [Final Capstone Project Report](docs/FINAL_CAPSTONE_REPORT.md)
- [Executive Project Summary](docs/presentation/EXECUTIVE_SUMMARY.md)
- [Final Project Presentation](docs/presentation/CampusAssist_Module_7_Presentation.pptx)
- [Live Demonstration Script](docs/presentation/DEMO_SCRIPT.md)
- [Reflection and Lessons Learned](docs/reflection/REFLECTION_AND_LESSONS_LEARNED.md)

### Technical Documentation

- [Test Plan](docs/TEST_PLAN.md)
- [Testing and Validation Report](docs/TESTING_AND_VALIDATION_REPORT.md)
- [Test Results](docs/testing/TEST_RESULTS.md)
- [Security Review Report](docs/testing/SECURITY_REVIEW_REPORT.md)
- [Solution Optimization Report](docs/SOLUTION_OPTIMIZATION_REPORT.md)
- [User Guide](docs/USER_GUIDE.md)
- [Cloud Architecture Document](docs/CLOUD_ARCHITECTURE.md)
- [Cloud Deployment Report](docs/deployment/CLOUD_DEPLOYMENT_REPORT.md)
- [Deployment Guide](docs/deployment/DEPLOYMENT_GUIDE.md)
- [System Integration Report](docs/SYSTEM_INTEGRATION_REPORT.md)
- [End-to-End Integration Architecture](docs/diagrams/07_end_to_end_integration.mmd)

Architecture diagrams are available in `docs/diagrams/`. Evaluation and performance evidence is available in `reports/`.

## 9. Cloud Deployment

The application is deployed using Streamlit Community Cloud and connected to the GitHub `main` branch.

**Live application:** https://campusassist.streamlit.app

The deployed environment uses Python 3.11 and dependencies specified in `requirements.txt`.

## 10. Security and Limitations

- The prototype uses synthetic sample data only.
- Basic input validation is implemented.
- Git ignore rules exclude environment and secret configuration files.
- User authentication and role-based access control are not implemented.
- No separate cloud database or object storage is configured.
- Monitoring is limited to Streamlit Community Cloud application logs.
- No infrastructure-as-code setup is currently included.
- Similarity scores indicate retrieval similarity, not factual accuracy or confidence.

## 11. Future Improvements

- Expand the document collection with approved institutional content.
- Test retrieval on larger and more diverse datasets.
- Evaluate unanswerable-question handling.
- Add grounded answer generation using an LLM.
- Introduce authentication and role-based access control.
- Add dedicated monitoring and production infrastructure.

## 12. Project Status

The prototype includes data preparation, exploratory analysis, retrieval model training and evaluation, a working Streamlit interface, and cloud deployment.

---

**CampusAssist | Capstone Project**
