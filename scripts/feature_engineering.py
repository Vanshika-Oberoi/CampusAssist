
import pandas as pd
import re
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "data" / "chunks" / "document_chunks.csv"
OUTPUT_FILE = BASE_DIR / "data" / "processed" / "feature_engineered_chunks.csv"

# Load prepared chunks
df = pd.read_csv(INPUT_FILE)

# Feature 1: Character count
df["character_count"] = df["content"].fillna("").apply(len)

# Feature 2: Sentence count
def count_sentences(text):
    sentences = re.split(r"[.!?]+", str(text))
    return len([s for s in sentences if s.strip()])

df["sentence_count"] = df["content"].apply(count_sentences)

# Feature 3: Average word length
def average_word_length(text):
    words = re.findall(r"\b\w+\b", str(text))
    if not words:
        return 0
    return round(sum(len(word) for word in words) / len(words), 2)

df["avg_word_length"] = df["content"].apply(average_word_length)

# Feature 4: Whether the chunk contains a question
df["has_question"] = df["content"].str.contains(r"\?", regex=True, na=False)

# Feature 5: Whether the chunk contains a number
df["has_number"] = df["content"].str.contains(r"\d", regex=True, na=False)

# Save feature-engineered dataset
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT_FILE, index=False)

print("Feature engineering completed successfully!")
print("Total chunks:", len(df))
print("New features added:")
print("character_count, sentence_count, avg_word_length, has_question, has_number")
print("\nFeature-engineered dataset saved to:")
print(OUTPUT_FILE)

print("\nDataset preview:")
print(df[[
    "document_id",
    "chunk_id",
    "word_count",
    "character_count",
    "sentence_count",
    "avg_word_length",
    "has_question",
    "has_number"
]].head())
