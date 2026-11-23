# CampusAssist – Live Demonstration Script

## 1. Demo Objective

Demonstrate how CampusAssist searches a sample student information collection using semantic and keyword-based retrieval.

**Suggested duration:** 5–7 minutes.

**Live application:** https://campusassist.streamlit.app

## 2. Before the Demo

1. Open the deployed application.
2. Confirm that the page loads.
3. Check that the model selector and Top-K control are visible.
4. Keep the following sample questions ready:
   - What topics are covered in the Introduction to AI course?
   - How can students submit their assignments?
   - What is the university's hostel fee refund policy?

The dataset is synthetic and intended only for demonstration.

## 3. Demonstration Flow

### Step 1: Introduce the Application

Explain:

"CampusAssist is a retrieval-based student information assistant. It helps users find relevant information from sample course documents, assignment instructions, FAQs, and policy examples."

Point out the synthetic-data disclaimer.

### Step 2: Demonstrate Semantic Retrieval

1. Select Sentence Transformers in the sidebar.
2. Set Top-K to 3.
3. Enter:

   `What topics are covered in the Introduction to AI course?`

4. Click Search Documents.
5. Expand the top result.
6. Point out its title, document ID, category, similarity score, and content.

Explain that semantic retrieval compares the meaning of the query with document titles and content.

### Step 3: Demonstrate TF-IDF Retrieval

1. Change the model to TF-IDF.
2. Enter the same question.
3. Click Search Documents.
4. Compare the returned document rankings.

Explain that TF-IDF uses keyword and phrase matching, providing a lexical baseline.

### Step 4: Demonstrate an FAQ Query

Enter:

`How can students submit their assignments?`

Run the query using the available retrieval models.

Explain that this example demonstrates retrieval from the sample FAQ and assignment-related content.

### Step 5: Demonstrate Unsupported-Question Behaviour

Enter:

`What is the university's hostel fee refund policy?`

Explain:

"This information is not present in our sample dataset. The current prototype may still return documents because reliable unsupported-question detection has not yet been implemented."

This is a known limitation, not evidence that the retrieved document answers the question.

### Step 6: Explain Validation and Optimization

Present the project results:

- 12 synthetic sample documents.
- 15 evaluation questions.
- 13 automated artifact validation tests passed.
- Both models achieved 1.00 Top-1 Accuracy, MRR, and Recall@3 on the 12 answerable questions.
- Semantic average local warm-query time improved from 0.0814 seconds to 0.0079 seconds after caching title embeddings.

Clarify that aggregate retrieval metrics exclude the three unanswerable questions and performance figures are local benchmark measurements.

## 4. Suggested Presentation Timing

| Activity | Approximate time |
|---|---:|
| Introduction and problem | 1 minute |
| Semantic retrieval | 1 minute |
| TF-IDF comparison | 1 minute |
| FAQ and unsupported query | 1–2 minutes |
| Evaluation and optimization | 1–2 minutes |
| Conclusion | 30 seconds |

## 5. Closing Statement

"CampusAssist demonstrates how semantic and keyword-based retrieval can make a sample student information collection searchable through a simple web interface. The project covers data preparation, retrieval model evaluation, cloud deployment, testing, and performance optimization. Future work will focus on expanding the dataset, improving unsupported-query handling, and completing formal user and operational validation."

## 6. Demo Contingency

If the deployed application is unavailable:

- Use the project architecture and screenshots already available in the presentation materials, if prepared.
- Explain the retrieval workflow using the documented architecture.
- Do not claim that a live demonstration succeeded if the service is unavailable.

## 7. Demo Limitations to Disclose

- The dataset contains synthetic sample documents.
- The application retrieves documents and does not generate LLM answers.
- Unsupported questions may still return results.
- Similarity scores are not factual confidence scores.
- No formal stakeholder UAT has been completed.
