
import pandas as pd
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
REPORT_DIR = BASE_DIR / "reports"
REPORT_DIR.mkdir(exist_ok=True)

# Load all datasets
metadata = pd.read_csv(BASE_DIR / "data/raw/document_metadata.csv")
cleaned = pd.read_csv(BASE_DIR / "data/processed/cleaned_documents.csv")
chunks = pd.read_csv(BASE_DIR / "data/chunks/document_chunks.csv")
evaluation = pd.read_csv(BASE_DIR / "data/evaluation/test_questions.csv")
features = pd.read_csv(
    BASE_DIR / "data/processed/feature_engineered_chunks.csv"
)

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


# ------------------------------------------------
# FEATURE ENGINEERING VALIDATION - CHECKS 14 TO 20
# ------------------------------------------------

# 14. Feature-engineered chunk coverage
feature_chunk_ids = set(features["chunk_id"].dropna())

add_check(
    "Feature-engineered chunk coverage",
    feature_chunk_ids == set(chunks["chunk_id"].dropna())
    and len(features) == len(chunks),
    f"{len(feature_chunk_ids)} feature chunk IDs / {len(chunks)} original chunks",
    "Every original chunk should have exactly one feature-engineered record."
)

# 15. Required engineered columns
required_features = [
    "character_count",
    "sentence_count",
    "avg_word_length",
    "has_question",
    "has_number"
]

missing_features = [
    column for column in required_features
    if column not in features.columns
]

add_check(
    "Required engineered features",
    len(missing_features) == 0,
    len(required_features) - len(missing_features),
    "All five engineered feature columns should exist."
)

# 16. Missing values in feature-engineered dataset
feature_missing_values = int(features.isnull().sum().sum())

add_check(
    "Feature-engineered dataset missing values",
    feature_missing_values == 0,
    feature_missing_values,
    "The feature-engineered dataset should not contain missing values."
)

# 17. Character count consistency
actual_char_counts = features["content"].astype(str).apply(len)
stored_char_counts = pd.to_numeric(
    features["character_count"], errors="coerce"
)

char_errors = int(
    (actual_char_counts != stored_char_counts).sum()
)

add_check(
    "Character count consistency",
    char_errors == 0,
    char_errors,
    "Character counts should match the actual text length."
)

# 18. Sentence count consistency
def count_sentences(text):
    sentences = re.split(r"[.!?]+", str(text))
    return len([sentence for sentence in sentences if sentence.strip()])


actual_sentence_counts = features["content"].apply(count_sentences)
stored_sentence_counts = pd.to_numeric(
    features["sentence_count"], errors="coerce"
)

sentence_errors = int(
    (actual_sentence_counts != stored_sentence_counts).sum()
)

add_check(
    "Sentence count consistency",
    sentence_errors == 0,
    sentence_errors,
    "Sentence counts should match the punctuation-based calculation."
)

# 19. Average word length consistency
def calculate_average_word_length(text):
    words = re.findall(r"\b\w+\b", str(text))
    if not words:
        return 0
    return round(sum(len(word) for word in words) / len(words), 2)


actual_avg_lengths = features["content"].apply(
    calculate_average_word_length
)

stored_avg_lengths = pd.to_numeric(
    features["avg_word_length"], errors="coerce"
)

avg_length_errors = int(
    (actual_avg_lengths != stored_avg_lengths).sum()
)

add_check(
    "Average word length consistency",
    avg_length_errors == 0,
    avg_length_errors,
    "Average word length should match the calculated text values."
)

# 20. Boolean feature consistency
expected_questions = features["content"].astype(str).str.contains(
    r"\?", regex=True
)

expected_numbers = features["content"].astype(str).str.contains(
    r"\d", regex=True
)

actual_questions = features["has_question"].astype(str).str.lower().eq("true")
actual_numbers = features["has_number"].astype(str).str.lower().eq("true")

boolean_errors = int(
    (expected_questions != actual_questions).sum()
    + (expected_numbers != actual_numbers).sum()
)

add_check(
    "Boolean feature consistency",
    boolean_errors == 0,
    boolean_errors,
    "Question and number indicators should match the actual text."
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
