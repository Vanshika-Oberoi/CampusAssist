
from pathlib import Path
import pandas as pd
from datetime import date

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
REPORT_DIR = BASE_DIR / "reports"

metadata_path = RAW_DIR / "document_metadata.csv"
quality_path = REPORT_DIR / "data_quality_report.csv"

# Load actual project data
metadata = pd.read_csv(metadata_path)
quality = pd.read_csv(quality_path)

total_docs = len(metadata)

# Category distribution
category_counts = metadata["category"].value_counts().sort_index()

# Quality statistics
empty_docs = int(quality["is_empty"].sum())
duplicate_docs = int(quality["is_duplicate"].sum())
unreadable_docs = int((~quality["readable"]).sum())
short_docs = int((~quality["has_sufficient_content"]).sum())
missing_metadata = int(quality["missing_metadata"].sum())

missing_fields = int(
    quality["missing_metadata_fields"].fillna("").astype(str)
    .str.strip().ne("").sum()
)

word_stats = quality["word_count"].describe()

# Source information
source_counts = metadata["source_type"].value_counts().to_dict()
format_counts = metadata["format"].value_counts().to_dict()
collection_dates = sorted(metadata["collection_date"].dropna().unique())

category_text = "\n".join(
    f"- {category}: {count} documents"
    for category, count in category_counts.items()
)

source_text = "\n".join(
    f"- {source}: {count} documents"
    for source, count in source_counts.items()
)

format_text = "\n".join(
    f"- {file_format}: {count} documents"
    for file_format, count in format_counts.items()
)

date_text = ", ".join(str(d) for d in collection_dates)

report = f"""# Data Acquisition and Data Quality Report

**Project:** CampusAssist  
**Module:** 3 - Data Preparation  
**Report updated:** {date.today()}

## 1. Introduction

CampusAssist is a proposed Retrieval-Augmented Generation (RAG)
student assistance system. It is designed to retrieve relevant
information from educational documents and provide answers grounded
in the available document content.

This report documents the acquisition, organization, quality
assessment, suitability, and responsible use of the initial
CampusAssist prototype dataset.

## 2. Data Sources and Acquisition

The initial dataset contains {total_docs} synthetic text documents.
All documents were created specifically for the CampusAssist
prototype using a Python data-generation script.

No external university database, public repository, third-party
provider, API, or real student information was used in this
initial acquisition phase.

The source type distribution is:

{source_text}

The source reference recorded in the metadata is:
"Created for CampusAssist project".

The recorded collection date is: {date_text}.

### 2.1 Dataset Categories

The documents are organized into four categories:

{category_text}

### 2.2 Collection Method

The documents were generated as individual TXT files and stored
under the data/raw directory. A central CSV metadata file was
created to maintain document identifiers, titles, categories,
filenames, source types, source references, collection dates,
and file formats.

### 2.3 File Formats

{format_text}

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
| Total documents | {total_docs} |
| Empty documents | {empty_docs} |
| Duplicate documents | {duplicate_docs} |
| Unreadable documents | {unreadable_docs} |
| Documents below the 10-word threshold | {short_docs} |
| Missing metadata records | {missing_metadata} |
| Records with missing metadata fields | {missing_fields} |

### 4.1 Word Count Statistics

| Metric | Words |
|---|---:|
| Average | {word_stats["mean"]:.2f} |
| Minimum | {word_stats["min"]:.0f} |
| Median | {word_stats["50%"]:.2f} |
| Maximum | {word_stats["max"]:.0f} |

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

The initial CampusAssist dataset contains {total_docs} organized
synthetic documents across four categories.

The recorded automated quality checks found no empty documents,
duplicates, unreadable files, missing metadata records, or
documents below the configured word threshold.

The dataset provides an initial foundation for document
preprocessing and retrieval workflow development. Its synthetic
nature and limited size must be considered before using it
for broader model development or real-world deployment.
"""

output_path = REPORT_DIR / "data_acquisition_quality_report.md"
output_path.write_text(report, encoding="utf-8")

print("Data Acquisition and Data Quality Report updated!")
print(f"Documents analyzed: {total_docs}")
print(f"Report saved to: {output_path}")
