
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
REPORT_DIR = BASE_DIR / "reports"
REPORT_DIR.mkdir(exist_ok=True)

# Load all datasets
metadata = pd.read_csv(BASE_DIR / "data/raw/document_metadata.csv")
cleaned = pd.read_csv(BASE_DIR / "data/processed/cleaned_documents.csv")
chunks = pd.read_csv(BASE_DIR / "data/chunks/document_chunks.csv")
evaluation = pd.read_csv(BASE_DIR / "data/evaluation/test_questions.csv")

results = []

def add_check(name, passed, observed, details):
    results.append({
        "check": name,
        "status": "PASS" if passed else "WARNING",
        "observed_result": observed,
        "details": details
    })

# 1. Document ID uniqueness
add_check(
    "Unique metadata document IDs",
    metadata["document_id"].is_unique,
    metadata["document_id"].nunique(),
    "Every source document should have a unique ID."
)

# 2. Filename uniqueness
add_check(
    "Unique source filenames",
    metadata["file_name"].is_unique,
    metadata["file_name"].nunique(),
    "Each source filename should appear only once in metadata."
)

# 3. Metadata completeness
missing_metadata = int(metadata.isnull().sum().sum())
add_check(
    "Missing metadata values",
    missing_metadata == 0,
    missing_metadata,
    "Checks for missing values across metadata columns."
)

# 4. Cleaned document coverage
metadata_ids = set(metadata["document_id"].dropna())
cleaned_ids = set(cleaned["document_id"].dropna())

add_check(
    "Cleaned document ID coverage",
    cleaned_ids == metadata_ids,
    f"{len(cleaned_ids)} cleaned IDs / {len(metadata_ids)} metadata IDs",
    "Every metadata document should have a corresponding cleaned document."
)

# 5. Chunk document references
chunk_ids = set(chunks["document_id"].dropna())

add_check(
    "Chunk document references",
    chunk_ids.issubset(cleaned_ids),
    len(chunk_ids),
    "Every chunk should refer to an existing cleaned document."
)

# 6. Unique chunk IDs
add_check(
    "Unique chunk IDs",
    chunks["chunk_id"].is_unique,
    chunks["chunk_id"].nunique(),
    "Each generated chunk should have a unique identifier."
)

# 7. Empty document content
empty_documents = int(
    cleaned["content"].fillna("").astype(str).str.strip().eq("").sum()
)

add_check(
    "Empty cleaned documents",
    empty_documents == 0,
    empty_documents,
    "Cleaned documents should contain readable text."
)

# 8. Word count consistency
actual_word_counts = cleaned["content"].fillna("").astype(str).apply(
    lambda text: len(text.split())
)

stored_word_counts = pd.to_numeric(
    cleaned["word_count"], errors="coerce"
)

word_count_errors = int(
    (actual_word_counts != stored_word_counts).sum()
)

add_check(
    "Cleaned document word counts",
    word_count_errors == 0,
    word_count_errors,
    "Stored word counts should match the actual content."
)

# 9. Chunk word count consistency
actual_chunk_counts = chunks["content"].fillna("").astype(str).apply(
    lambda text: len(text.split())
)

stored_chunk_counts = pd.to_numeric(
    chunks["word_count"], errors="coerce"
)

chunk_count_errors = int(
    (actual_chunk_counts != stored_chunk_counts).sum()
)

add_check(
    "Chunk word counts",
    chunk_count_errors == 0,
    chunk_count_errors,
    "Stored chunk word counts should match the actual chunk content."
)

# 10. Evaluation question IDs
add_check(
    "Unique evaluation question IDs",
    evaluation["question_id"].is_unique,
    evaluation["question_id"].nunique(),
    "Every evaluation question should have a unique ID."
)

# 11. Evaluation document references
answerable = evaluation["is_answerable"].astype(str).str.lower().eq("true")

expected_ids = set(
    evaluation.loc[answerable, "expected_document_id"].dropna()
)

invalid_references = expected_ids - metadata_ids

add_check(
    "Evaluation source document references",
    len(invalid_references) == 0,
    len(invalid_references),
    "Every answerable question should reference an existing document ID."
)

# 12. Unanswerable questions should not have source IDs
unanswerable = ~answerable

unexpected_sources = evaluation.loc[
    unanswerable, "expected_document_id"
].fillna("").astype(str).str.strip().ne("").sum()

add_check(
    "Unanswerable question source IDs",
    unexpected_sources == 0,
    int(unexpected_sources),
    "Unanswerable questions should not be assigned a supporting document."
)

# 13. Evaluation question completeness
missing_questions = int(
    evaluation[["question", "expected_answer", "expected_behavior"]]
    .isnull().sum().sum()
)

add_check(
    "Evaluation question completeness",
    missing_questions == 0,
    missing_questions,
    "Questions, reference answers and expected behaviors should be present."
)

# Save validation report
report = pd.DataFrame(results)
output_file = REPORT_DIR / "prepared_data_validation.csv"
report.to_csv(output_file, index=False)

print("\nCAMPUSASSIST PREPARED DATA VALIDATION")
print("=====================================")

for _, row in report.iterrows():
    print(f"{row['status']}: {row['check']} - {row['observed_result']}")

passed = (report["status"] == "PASS").sum()
warnings = (report["status"] == "WARNING").sum()

print("\nVALIDATION SUMMARY")
print("------------------")
print(f"Total checks: {len(report)}")
print(f"Passed: {passed}")
print(f"Warnings: {warnings}")
print(f"\nReport saved at: {output_file}")

if warnings == 0:
    print("\nAll automated validation checks passed!")
else:
    print("\nPlease review the warnings before finalizing the dataset.")
