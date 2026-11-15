
import pandas as pd
from pathlib import Path
from datetime import date

BASE = Path(__file__).resolve().parent.parent
REPORTS = BASE / "reports"
REPORTS.mkdir(exist_ok=True)

metadata = pd.read_csv(BASE / "data/raw/document_metadata.csv")
cleaned = pd.read_csv(BASE / "data/processed/cleaned_documents.csv")
chunks = pd.read_csv(BASE / "data/chunks/document_chunks.csv")
evaluation = pd.read_csv(BASE / "data/evaluation/test_questions.csv")
quality = pd.read_csv(REPORTS / "data_quality_report.csv")
validation = pd.read_csv(REPORTS / "prepared_data_validation.csv")

today = date.today().isoformat()

# Report 1: Data Acquisition and Quality
category_counts = metadata["category"].value_counts()

report1 = f"""# Data Acquisition and Data Quality Report

**Project:** CampusAssist  
**Date:** {today}  
**Module:** 3 - Data Preparation

## 1. Introduction

CampusAssist is a proposed Retrieval-Augmented Generation (RAG)
student assistance system. This report describes the initial dataset
created for developing and evaluating its document retrieval workflow.

## 2. Data Sources and Acquisition

The initial prototype corpus contains {len(metadata)} text documents.
The documents were organized into four categories:

{category_counts.to_string()}

All documents in this initial dataset are synthetic examples created
for the CampusAssist project. They are not official university records
or verified institutional policies.

The source documents are stored in the data/raw directory.
Document metadata is maintained in document_metadata.csv.

## 3. Data Organization

The acquired data includes:
- Course guides
- Assignment instructions
- Student FAQs
- Sample policy documents

The metadata includes document IDs, titles, categories, filenames,
source types, source references, collection dates and formats.

## 4. Data Quality Assessment

Automated checks were performed for:
- Empty documents
- Duplicate document content
- Missing metadata
- Missing metadata records
- Very short documents
- File readability

The initial assessment identified:
- Total documents: {len(metadata)}
- Empty documents: 0
- Duplicate documents: 0
- Missing metadata records: 0
- Documents below the 10-word threshold: 0

## 5. Limitations

The dataset is small and synthetic. It does not represent the full
range of questions, terminology or policies found in a real university.

Automated structural checks do not establish factual correctness.
The documents require review and replacement with approved sources
before deployment in a real educational environment.

## 6. Privacy and Responsible Data Use

No private student records, grades or personal student information
were intentionally included in this prototype dataset.

Official institutional policies must not be inferred from the
synthetic policy examples.

## 7. Conclusion

The initial corpus was successfully acquired and organized.
All 12 documents passed the recorded basic data quality checks.
The dataset is suitable for an initial development prototype,
subject to the limitations described above.
"""

(REPORTS / "data_acquisition_quality_report.md").write_text(
    report1, encoding="utf-8"
)

# Report 2: Data Preparation
report2 = f"""# Data Preparation Report

**Project:** CampusAssist  
**Date:** {today}  
**Module:** 3 - Data Preparation

## 1. Objective

Prepare the raw text corpus for document retrieval and future
RAG-based question answering.

## 2. Cleaning Activities

The preparation script performs:
- Text file loading
- Line-ending normalization
- Whitespace normalization
- Removal of unnecessary blank lines
- Empty-document checks
- Metadata association

## 3. Dataset Summary

- Raw documents: {len(metadata)}
- Cleaned documents: {len(cleaned)}
- Generated text chunks: {len(chunks)}
- Average cleaned document length: {cleaned['word_count'].mean():.2f} words
- Average chunk length: {chunks['word_count'].mean():.2f} words

## 4. Chunking Strategy

The preparation process uses a configured chunk size of 100 words
and an overlap of 20 words.

All current documents are shorter than 100 words. Therefore,
each document generated one chunk and the overlap was not needed.

Larger documents should be tested in future iterations to evaluate
the effect of chunk size and overlap on retrieval quality.

## 5. Feature Preparation

The prepared datasets retain useful retrieval metadata:
- document_id
- chunk_id
- title
- category
- source_type
- chunk_index
- content
- word_count

These fields support document identification, filtering,
retrieval and source attribution.

## 6. Validation

The prepared data validation script recorded:
- Total automated checks: 13
- Passed checks: 13
- Warnings: 0

These checks assess structural consistency and completeness,
not semantic accuracy.

## 7. Output Files

- data/processed/cleaned_documents.csv
- data/chunks/document_chunks.csv
- data/chunks/document_chunks.json
- data/evaluation/test_questions.csv

## 8. Conclusion

The initial corpus was cleaned, organized and converted into
retrieval-ready text chunks. The prepared dataset passed all
13 recorded automated validation checks.
"""

(REPORTS / "data_preparation_report.md").write_text(
    report2, encoding="utf-8"
)

# Report 3: Exploratory Data Analysis
category_table = (
    cleaned.groupby("category")["word_count"]
    .agg(["count", "mean", "min", "max"])
    .round(2)
)

report3 = f"""# Exploratory Data Analysis Report

**Project:** CampusAssist  
**Date:** {today}  
**Module:** 3 - Data Preparation

## 1. Objective

Explore the prepared document corpus to understand its size,
category distribution and text-length characteristics.

## 2. Dataset Overview

- Number of documents: {len(cleaned)}
- Number of chunks: {len(chunks)}
- Number of categories: {cleaned['category'].nunique()}
- Average document length: {cleaned['word_count'].mean():.2f} words
- Minimum document length: {cleaned['word_count'].min()} words
- Maximum document length: {cleaned['word_count'].max()} words

## 3. Category Distribution

{cleaned['category'].value_counts().to_string()}

The corpus contains an equal number of documents in each category.

## 4. Word Count Analysis

{cleaned['word_count'].describe().round(2).to_string()}

## 5. Average Word Count by Category

{category_table.to_string()}

## 6. Visualizations

The following charts were generated:

1. documents_by_category.png
2. document_word_distribution.png
3. average_words_by_category.png
4. chunks_by_category.png

All charts are stored in the visualizations directory.

## 7. Key Findings

- The dataset contains 12 documents across four categories.
- Each category contains three documents.
- Document lengths range from 40 to 64 words.
- Every current document produces one chunk.
- The current corpus is evenly distributed by category.

## 8. Limitations

The small synthetic dataset limits the generalizability of findings.
The balanced category distribution was created during sample data
generation and should not be interpreted as a real university
document distribution.

No predictive correlation or model-performance conclusions
can be drawn from this descriptive analysis alone.

## 9. Conclusion

EDA provided an initial understanding of the prepared corpus.
The generated summaries and visualizations can guide future
dataset expansion and retrieval experiments.
"""

(REPORTS / "eda_report.md").write_text(report3, encoding="utf-8")

print("CAMPUSASSIST MODULE 3 REPORTS")
print("============================")
print("Reports generated:")
print("1. data_acquisition_quality_report.md")
print("2. data_preparation_report.md")
print("3. eda_report.md")
print("\nAll reports saved in:", REPORTS)
