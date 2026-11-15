
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "data_dictionary"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Datasets included in the CampusAssist project
datasets = {
    "Raw Document Metadata": "data/raw/document_metadata.csv",
    "Cleaned Documents": "data/processed/cleaned_documents.csv",
    "Document Chunks": "data/chunks/document_chunks.csv",
    "Evaluation Questions": "data/evaluation/test_questions.csv"
}

# Description of every dataset column
descriptions = {
    "document_id": "Unique identifier assigned to each source document.",
    "title": "Title or name of the source document.",
    "category": "Document category, such as course guides, policies, FAQs or assignment instructions.",
    "file_name": "Original filename of the source text document.",
    "source_type": "Indicates whether the document is synthetic or comes from another source.",
    "source_reference": "Description of where the original document came from.",
    "collection_date": "Date when the document was added to the project dataset.",
    "format": "Original file format of the document.",
    "content": "Cleaned text content of the document or text chunk.",
    "word_count": "Number of words in the document or chunk.",
    "chunk_id": "Unique identifier assigned to a text chunk.",
    "chunk_index": "Position of the chunk within its original document.",
    "question_id": "Unique identifier assigned to an evaluation question.",
    "question": "Student question used to test the CampusAssist system.",
    "expected_answer": "Reference answer used to evaluate the system's response.",
    "is_answerable": "Boolean indicator showing whether the dataset contains enough information to answer the question.",
    "expected_behavior": "Expected system behavior when responding to the evaluation question.",
    "expected_document_id": "Document ID expected to support the answer. Empty when the question is unanswerable.",
    "expected_category": "Expected category of the supporting document. Empty when the question is unanswerable."
}

dictionary_rows = []

for dataset_name, relative_path in datasets.items():
    file_path = BASE_DIR / relative_path
    df = pd.read_csv(file_path)

    for column in df.columns:
        values = df[column].dropna()
        example = str(values.iloc[0]) if not values.empty else "No example available"

        dictionary_rows.append({
            "dataset_name": dataset_name,
            "dataset_file": relative_path,
            "column_name": column,
            "data_type": str(df[column].dtype),
            "description": descriptions.get(column, "Description not yet provided."),
            "example_value": example
        })

# Create the data dictionary CSV
dictionary_df = pd.DataFrame(dictionary_rows)
csv_path = OUTPUT_DIR / "data_dictionary.csv"
dictionary_df.to_csv(csv_path, index=False)

# Create readable Markdown documentation
md_path = OUTPUT_DIR / "data_dictionary.md"

with open(md_path, "w", encoding="utf-8") as file:
    file.write("# CampusAssist Data Dictionary\n\n")
    file.write(
        "This document describes the fields used in the raw, cleaned, "
        "chunked and evaluation datasets of the CampusAssist project.\n\n"
    )

    for dataset_name, relative_path in datasets.items():
        subset = dictionary_df[dictionary_df["dataset_name"] == dataset_name]

        file.write(f"## {dataset_name}\n\n")
        file.write(f"**Dataset file:** `{relative_path}`\n\n")
        file.write("| Column | Data Type | Description | Example |\n")
        file.write("|---|---|---|---|\n")

        for _, row in subset.iterrows():
            description = str(row["description"]).replace("|", "\\|")
            example = str(row["example_value"]).replace("|", "\\|")
            file.write(
                f"| {row['column_name']} | {row['data_type']} "
                f"| {description} | {example} |\n"
            )

        file.write("\n")

print("CAMPUSASSIST DATA DICTIONARY")
print("============================")
print(f"Datasets documented: {len(datasets)}")
print(f"Total columns documented: {len(dictionary_df)}")
print("\nGenerated files:")
print(csv_path)
print(md_path)
print("\nData dictionary created successfully!")
