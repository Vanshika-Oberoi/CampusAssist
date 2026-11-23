# CampusAssist Deployment Guide

## 1. Overview

CampusAssist is a Streamlit-based student information assistant that retrieves relevant information from a small synthetic document collection using TF-IDF and Sentence Transformers.

Live application: https://campusassist.streamlit.app

GitHub repository: https://github.com/Vanshika-Oberoi/CampusAssist

## 2. Prerequisites

- Python 3.11
- Git
- GitHub account
- Streamlit Community Cloud account

## 3. Run Locally

Clone the repository:

    git clone https://github.com/Vanshika-Oberoi/CampusAssist.git
    cd CampusAssist

Install dependencies:

    python3 -m pip install -r requirements.txt

Start the application:

    streamlit run app.py

Open the local URL displayed in the terminal.

## 4. Deploy on Streamlit Community Cloud

1. Push the project to GitHub.
2. Sign in to Streamlit Community Cloud.
3. Select Create app.
4. Choose the CampusAssist GitHub repository.
5. Select the main branch.
6. Set the application entry point to app.py.
7. Select Python 3.11 in advanced settings.
8. Deploy the application.
9. Open the generated application URL and test retrieval.

## 5. Test the Application

Try these sample questions:

| Question | Expected top document |
|---|---|
| What topics are covered in the Introduction to AI course? | DOC002 |
| What should be included in an AI project report? | DOC005 |
| How can students submit their assignments? | DOC007 |

Test both Sentence Transformers and TF-IDF retrieval modes.

## 6. Updating the Application

1. Make the required changes locally.
2. Test the application using streamlit run app.py.
3. Commit and push changes to the main branch.
4. Streamlit Community Cloud will detect the update and redeploy the application.
5. Verify the live application after deployment.

## 7. Troubleshooting

- Dependency errors: Check requirements.txt and the configured Python version.
- Missing model artifacts: Confirm that the required files are present in the models directory.
- Missing document data: Confirm that data/chunks/document_chunks.csv exists.
- Application errors: Review the application logs in Streamlit Community Cloud.
- Slow first startup: The pretrained Sentence Transformers model may need to download before first use.

## 8. Operational Notes and Limitations

- The prototype uses 12 synthetic sample documents, not official university information.
- The application retrieves and ranks document passages; it does not generate answers using an LLM.
- Similarity scores are not factual accuracy or confidence scores.
- The prototype does not implement user authentication or role-based access control.
- Data and model artifacts are stored in the GitHub repository; no separate cloud database or object storage is configured.
- Basic application logs are available through Streamlit Community Cloud.
