
from pathlib import Path
import pandas as pd
import re
import json

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
CHUNKS_DIR = BASE_DIR / "data" / "chunks"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
CHUNKS_DIR.mkdir(parents=True, exist_ok=True)

metadata = pd.read_csv(RAW_DIR / "document_metadata.csv")

processed_documents = []
all_chunks = []

def clean_text(text):
    # Standardize line endings and whitespace
    text = text.replace("\r\n", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

def create_chunks(text, chunk_size=100, overlap=20):
    words = text.split()
    chunks = []

    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk_words = words[start:end]

        if not chunk_words:
            break

        chunks.append(" ".join(chunk_words))

        if end >= len(words):
            break

        start = end - overlap

    return chunks

for _, row in metadata.iterrows():

    category = row["category"]
    file_name = row["file_name"]

    file_path = RAW_DIR / category / file_name

    if not file_path.exists():
        print("Missing file:", file_name)
        continue

    original_text = file_path.read_text(
        encoding="utf-8"
    )

    cleaned_text = clean_text(original_text)

    if not cleaned_text:
        print("Skipping empty document:", file_name)
        continue

    document_id = row["document_id"]

    processed_documents.append({
        "document_id": document_id,
        "title": row["title"],
        "category": category,
        "file_name": file_name,
        "source_type": row["source_type"],
        "content": cleaned_text,
        "word_count": len(cleaned_text.split())
    })

    # Generate text chunks
    document_chunks = create_chunks(cleaned_text)

    for index, chunk in enumerate(document_chunks, start=1):

        all_chunks.append({
            "document_id": document_id,
            "chunk_id": f"{document_id}_C{index:02d}",
            "title": row["title"],
            "category": category,
            "source_type": row["source_type"],
            "chunk_index": index,
            "content": chunk,
            "word_count": len(chunk.split())
        })

# Save processed document dataset
processed_df = pd.DataFrame(processed_documents)

processed_df.to_csv(
    PROCESSED_DIR / "cleaned_documents.csv",
    index=False
)

# Save chunk dataset
chunks_df = pd.DataFrame(all_chunks)

chunks_df.to_csv(
    CHUNKS_DIR / "document_chunks.csv",
    index=False
)

# Save JSON version for later AI retrieval
with open(
    CHUNKS_DIR / "document_chunks.json",
    "w",
    encoding="utf-8"
) as file:
    json.dump(
        all_chunks,
        file,
        indent=4,
        ensure_ascii=False
    )

print("\n================================")
print(" CAMPUSASSIST DATA PREPARATION")
print("================================")

print("Original documents:", len(metadata))
print("Processed documents:", len(processed_df))
print("Generated text chunks:", len(chunks_df))

if len(chunks_df) > 0:
    print(
        "Average chunk word count:",
        round(chunks_df["word_count"].mean(), 2)
    )

print("\nFiles created:")
print("data/processed/cleaned_documents.csv")
print("data/chunks/document_chunks.csv")
print("data/chunks/document_chunks.json")

print("\nData preparation completed!")
