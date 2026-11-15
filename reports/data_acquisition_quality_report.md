# Data Acquisition and Data Quality Report

**Project:** CampusAssist  
**Date:** 2026-11-15  
**Module:** 3 - Data Preparation

## 1. Introduction

CampusAssist is a proposed Retrieval-Augmented Generation (RAG)
student assistance system. This report describes the initial dataset
created for developing and evaluating its document retrieval workflow.

## 2. Data Sources and Acquisition

The initial prototype corpus contains 12 text documents.
The documents were organized into four categories:

category
course_guides              3
assignment_instructions    3
student_faqs               3
policies                   3

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
- Total documents: 12
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
