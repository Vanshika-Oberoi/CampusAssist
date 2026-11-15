# Data Acquisition and Data Quality Report

**Project:** CampusAssist  
**Module:** 3 - Data Preparation  
**Report updated:** 2026-11-15

## 1. Introduction

CampusAssist is a proposed Retrieval-Augmented Generation (RAG)
student assistance system. It is designed to retrieve relevant
information from educational documents and provide answers grounded
in the available document content.

This report documents the acquisition, organization, quality
assessment, suitability, and responsible use of the initial
CampusAssist prototype dataset.

## 2. Data Sources and Acquisition

The initial dataset contains 12 synthetic text documents.
All documents were created specifically for the CampusAssist
prototype using a Python data-generation script.

No external university database, public repository, third-party
provider, API, or real student information was used in this
initial acquisition phase.

The source type distribution is:

- synthetic: 12 documents

The source reference recorded in the metadata is:
"Created for CampusAssist project".

The recorded collection date is: 2026-11-14.

### 2.1 Dataset Categories

The documents are organized into four categories:

- assignment_instructions: 3 documents
- course_guides: 3 documents
- policies: 3 documents
- student_faqs: 3 documents

### 2.2 Collection Method

The documents were generated as individual TXT files and stored
under the data/raw directory. A central CSV metadata file was
created to maintain document identifiers, titles, categories,
filenames, source types, source references, collection dates,
and file formats.

### 2.3 File Formats

- TXT: 12 documents

## 3. Dataset Description and Suitability

The corpus contains course guides, assignment instructions,
student FAQs, and sample policy documents.

These categories were selected because they represent common
information needs in a student assistance application.

The dataset is suitable for:
- Developing an initial document ingestion workflow.
- Testing text cleaning and preprocessing.
- Experimenting with document chunking.
- Preparing retrieval-oriented metadata.
- Creating initial question-and-answer evaluation examples.

However, the dataset is small and synthetic. It is not sufficient
to establish real-world answer accuracy, institutional coverage,
or production readiness.

## 4. Data Quality Assessment

Automated checks were performed using the project quality
assessment script.

| Quality check | Result |
|---|---:|
| Total documents | 12 |
| Empty documents | 0 |
| Duplicate documents | 0 |
| Unreadable documents | 0 |
| Documents below the 10-word threshold | 0 |
| Missing metadata records | 0 |
| Records with missing metadata fields | 0 |

### 4.1 Word Count Statistics

| Metric | Words |
|---|---:|
| Average | 50.00 |
| Minimum | 40 |
| Median | 49.50 |
| Maximum | 64 |

### 4.2 Identified Data Issues

The automated checks did not identify empty files, duplicate
content, unreadable documents, missing metadata records, or
documents below the configured minimum word threshold.

These checks do not verify factual correctness, writing quality,
completeness of subject coverage, or whether document statements
reflect actual university rules.

The relatively short document lengths are a limitation for
testing retrieval over larger educational resources.

## 5. Privacy, Security and Ethical Considerations

The initial prototype corpus does not intentionally contain
private student records, grades, student identifiers, or personal
student information.

The following safeguards are relevant to future development:

- Use approved and traceable sources for additional documents.
- Exclude confidential student and institutional information
  unless explicit authorization and appropriate safeguards exist.
- Avoid presenting synthetic policy examples as official rules.
- Maintain source references and document metadata.
- Restrict access to confidential data if it is introduced later.
- Review document content for accuracy and suitability before
  including it in a production knowledge base.

## 6. Data Governance Considerations

The project maintains a central metadata CSV for document
identification and source tracking.

Raw documents are kept separately from processed documents and
retrieval chunks. This separation supports reproducibility and
allows the original source files to be retained.

Future improvements should include version tracking, documented
source approval, periodic content reviews, access controls,
and a process for removing outdated documents.

## 7. Limitations and Future Improvements

The current corpus has the following limitations:

1. All 12 documents are synthetic examples.
2. The corpus does not represent a complete university knowledge
   base.
3. The documents have limited length and subject coverage.
4. Factual accuracy has not been independently verified.
5. No production retrieval or answer-quality evaluation has
   been completed using this corpus.

Future work should incorporate approved public educational
documents or authorized institutional material, expand the
document collection, and evaluate retrieval quality using
representative questions.

## 8. Conclusion

The initial CampusAssist dataset contains 12 organized
synthetic documents across four categories.

The recorded automated quality checks found no empty documents,
duplicates, unreadable files, missing metadata records, or
documents below the configured word threshold.

The dataset provides an initial foundation for document
preprocessing and retrieval workflow development. Its synthetic
nature and limited size must be considered before using it
for broader model development or real-world deployment.
