# CampusAssist Data Dictionary

This document describes the fields used in the raw, cleaned, chunked and evaluation datasets of the CampusAssist project.

## Raw Document Metadata

**Dataset file:** `data/raw/document_metadata.csv`

| Column | Data Type | Description | Example |
|---|---|---|---|
| document_id | object | Unique identifier assigned to each source document. | DOC001 |
| title | object | Title or name of the source document. | Introduction to Data Science |
| category | object | Document category, such as course guides, policies, FAQs or assignment instructions. | course_guides |
| file_name | object | Original filename of the source text document. | introduction_to_data_science.txt |
| source_type | object | Indicates whether the document is synthetic or comes from another source. | synthetic |
| source_reference | object | Description of where the original document came from. | Created for CampusAssist project |
| collection_date | object | Date when the document was added to the project dataset. | 2026-11-14 |
| format | object | Original file format of the document. | TXT |

## Cleaned Documents

**Dataset file:** `data/processed/cleaned_documents.csv`

| Column | Data Type | Description | Example |
|---|---|---|---|
| document_id | object | Unique identifier assigned to each source document. | DOC001 |
| title | object | Title or name of the source document. | Introduction to Data Science |
| category | object | Document category, such as course guides, policies, FAQs or assignment instructions. | course_guides |
| file_name | object | Original filename of the source text document. | introduction_to_data_science.txt |
| source_type | object | Indicates whether the document is synthetic or comes from another source. | synthetic |
| content | object | Cleaned text content of the document or text chunk. | Course: Introduction to Data Science

This course introduces students to the fundamentals of data science.
Students learn how to collect, organize, clean, analyse and interpret data.

Main topics include Python programming, data types, statistics,
data visualization and exploratory data analysis.

Learning outcomes:
1. Understand basic data science concepts.
2. Work with structured datasets.
3. Perform basic data cleaning.
4. Create charts and interpret findings. |
| word_count | int64 | Number of words in the document or chunk. | 64 |

## Document Chunks

**Dataset file:** `data/chunks/document_chunks.csv`

| Column | Data Type | Description | Example |
|---|---|---|---|
| document_id | object | Unique identifier assigned to each source document. | DOC001 |
| chunk_id | object | Unique identifier assigned to a text chunk. | DOC001_C01 |
| title | object | Title or name of the source document. | Introduction to Data Science |
| category | object | Document category, such as course guides, policies, FAQs or assignment instructions. | course_guides |
| source_type | object | Indicates whether the document is synthetic or comes from another source. | synthetic |
| chunk_index | int64 | Position of the chunk within its original document. | 1 |
| content | object | Cleaned text content of the document or text chunk. | Course: Introduction to Data Science This course introduces students to the fundamentals of data science. Students learn how to collect, organize, clean, analyse and interpret data. Main topics include Python programming, data types, statistics, data visualization and exploratory data analysis. Learning outcomes: 1. Understand basic data science concepts. 2. Work with structured datasets. 3. Perform basic data cleaning. 4. Create charts and interpret findings. |
| word_count | int64 | Number of words in the document or chunk. | 64 |

## Evaluation Questions

**Dataset file:** `data/evaluation/test_questions.csv`

| Column | Data Type | Description | Example |
|---|---|---|---|
| question_id | object | Unique identifier assigned to an evaluation question. | Q001 |
| question | object | Student question used to test the CampusAssist system. | What topics are covered in the Introduction to Data Science course? |
| expected_answer | object | Reference answer used to evaluate the system's response. | The course covers Python programming, data types, statistics, data visualization, data collection, data cleaning and exploratory data analysis. |
| is_answerable | bool | Boolean indicator showing whether the dataset contains enough information to answer the question. | True |
| expected_behavior | object | Expected system behavior when responding to the evaluation question. | Answer using the course guide. |
| expected_document_id | object | Document ID expected to support the answer. Empty when the question is unanswerable. | DOC001 |
| expected_category | object | Expected category of the supporting document. Empty when the question is unanswerable. | course_guides |

