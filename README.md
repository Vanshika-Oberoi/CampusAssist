
# CampusAssist - AI-Powered Student Assistant

## Project Overview

CampusAssist is a proposed AI-powered student assistance system based on Retrieval-Augmented Generation (RAG).

The project aims to help students find relevant information from course guides, assignment instructions, FAQs and policy documents.

## Module 3 - Data Preparation

This module focuses on acquiring, cleaning, preparing and exploring the dataset required for CampusAssist.

## Dataset Overview

The initial prototype dataset contains 12 synthetic text documents.

| Category | Documents |
|---|---:|
| Course Guides | 3 |
| Assignment Instructions | 3 |
| Student FAQs | 3 |
| Policies | 3 |
| **Total** | **12** |

All documents are synthetic examples created for this project. They are not official university documents or policies.

## Data Preparation

The project includes:
- Text cleaning and whitespace normalization.
- Document metadata management.
- Text chunking with a configured chunk size of 100 words and overlap of 20 words.
- Document word-count calculation.
- CSV and JSON dataset generation.

## Exploratory Data Analysis

The analysis examines:
- Document category distribution.
- Document word-count distribution.
- Average word count by category.
- Number of chunks by category.

Four visualizations are available in the `visualizations` folder.

## Evaluation Dataset

A synthetic evaluation dataset of 15 questions was created:
- 12 answerable questions.
- 3 unanswerable questions.

The questions are designed to test source retrieval and whether the system avoids unsupported answers.

## Project Structure

```text
CampusAssist/
├── data/
│   ├── raw/
│   ├── processed/
│   ├── chunks/
│   └── evaluation/
├── data_dictionary/
├── notebooks/
├── reports/
├── scripts/
└── visualizations/
```

## Validation

The prepared dataset passed all 13 automated validation checks with zero warnings.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Limitations and Future Improvements

The current corpus is small and synthetic.

Future improvements include:
- Expanding the document collection.
- Adding approved institutional documents.
- Testing larger documents and chunking strategies.
- Implementing document embeddings and semantic retrieval.
- Evaluating retrieval accuracy and answer quality.

## Project Status

Module 3 data acquisition, preparation, validation and exploratory analysis have been completed for the initial prototype.
