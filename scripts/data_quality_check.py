
from pathlib import Path
import pandas as pd
import re

# Locate project folders
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
REPORT_DIR = BASE_DIR / "reports"

REPORT_DIR.mkdir(exist_ok=True)

# Load document metadata
metadata_file = RAW_DIR / "document_metadata.csv"
metadata = pd.read_csv(metadata_file)

# Create a lookup using file names
metadata_lookup = {
    str(row["file_name"]): row
    for _, row in metadata.iterrows()
}

# Find all text documents
document_files = list(RAW_DIR.rglob("*.txt"))

results = []
seen_content = {}

for file_path in document_files:

    text = file_path.read_text(
        encoding="utf-8",
        errors="replace"
    )

    # Normalize text for duplicate checking
    normalized_text = re.sub(
        r"\s+", " ", text.lower()
    ).strip()

    words = re.findall(r"\b\w+\b", text)

    file_name = file_path.name
    document_metadata = metadata_lookup.get(file_name)

    # Check duplicate content
    is_duplicate = False

    if normalized_text:
        if normalized_text in seen_content:
            is_duplicate = True
        else:
            seen_content[normalized_text] = file_name

    # Check missing metadata
    missing_metadata = document_metadata is None

    if document_metadata is not None:
        missing_fields = [
            field for field in ["document_id", "title",
                                "category", "source_type"]
            if pd.isna(document_metadata.get(field))
            or str(document_metadata.get(field)).strip() == ""
        ]
    else:
        missing_fields = ["metadata_record"]

    # Quality checks
    is_empty = len(text.strip()) == 0
    has_sufficient_content = len(words) >= 10

    results.append({
        "file_name": file_name,
        "category": file_path.parent.name,
        "word_count": len(words),
        "is_empty": is_empty,
        "has_sufficient_content": has_sufficient_content,
        "is_duplicate": is_duplicate,
        "missing_metadata": missing_metadata,
        "missing_metadata_fields": ", ".join(missing_fields),
        "readable": not is_empty
    })

# Create quality report
quality_df = pd.DataFrame(results)

report_path = REPORT_DIR / "data_quality_report.csv"
quality_df.to_csv(report_path, index=False)

# Calculate summary statistics
total_documents = len(quality_df)
empty_documents = int(quality_df["is_empty"].sum())
duplicate_documents = int(quality_df["is_duplicate"].sum())
missing_metadata_documents = int(
    quality_df["missing_metadata"].sum()
)
short_documents = int(
    (~quality_df["has_sufficient_content"]).sum()
)

print("\n======================================")
print(" CAMPUSASSIST DATA QUALITY ASSESSMENT")
print("======================================")

print("Total documents:", total_documents)
print("Empty documents:", empty_documents)
print("Duplicate documents:", duplicate_documents)
print("Missing metadata records:", missing_metadata_documents)
print("Documents with fewer than 10 words:", short_documents)

print("\nDocument category distribution:")
print(quality_df["category"].value_counts().to_string())

print("\nAverage document word count:",
      round(quality_df["word_count"].mean(), 2))

print("\nIndividual document results:")
print(quality_df[
    ["file_name", "word_count", "is_duplicate", "readable"]
].to_string(index=False))

print("\nQuality report saved at:")
print(report_path)

print("\nAssessment completed!")
