
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Project folders
BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED_DIR = BASE_DIR / "data" / "processed"
CHUNKS_DIR = BASE_DIR / "data" / "chunks"
REPORT_DIR = BASE_DIR / "reports"
VISUAL_DIR = BASE_DIR / "visualizations"

REPORT_DIR.mkdir(exist_ok=True)
VISUAL_DIR.mkdir(exist_ok=True)

# Load prepared datasets
documents = pd.read_csv(
    PROCESSED_DIR / "cleaned_documents.csv"
)

chunks = pd.read_csv(
    CHUNKS_DIR / "document_chunks.csv"
)

sns.set_theme(style="whitegrid")

# 1. Dataset overview
print("\n================================")
print(" CAMPUSASSIST EXPLORATORY DATA ANALYSIS")
print("================================")

print("\nDataset shape:")
print("Documents:", documents.shape[0])
print("Document columns:", documents.shape[1])
print("Chunks:", chunks.shape[0])

print("\nDocument categories:")
print(documents["category"].value_counts())

print("\nDocument word count statistics:")
print(documents["word_count"].describe())

print("\nChunk word count statistics:")
print(chunks["word_count"].describe())

# 2. Documents by category
category_counts = (
    documents["category"]
    .value_counts()
    .reset_index()
)

category_counts.columns = [
    "category", "document_count"
]

plt.figure(figsize=(9, 5))

sns.barplot(
    data=category_counts,
    x="category",
    y="document_count"
)

plt.title("Number of Documents by Category")
plt.xlabel("Document Category")
plt.ylabel("Number of Documents")
plt.xticks(rotation=20)
plt.tight_layout()

plt.savefig(
    VISUAL_DIR / "documents_by_category.png",
    dpi=300
)

plt.close()

# 3. Document word count distribution
plt.figure(figsize=(9, 5))

sns.histplot(
    data=documents,
    x="word_count",
    bins=8,
    kde=True
)

plt.title("Distribution of Document Word Counts")
plt.xlabel("Number of Words")
plt.ylabel("Number of Documents")
plt.tight_layout()

plt.savefig(
    VISUAL_DIR / "document_word_distribution.png",
    dpi=300
)

plt.close()

# 4. Average word count by category
average_words = (
    documents.groupby("category")["word_count"]
    .mean()
    .reset_index()
)

plt.figure(figsize=(9, 5))

sns.barplot(
    data=average_words,
    x="category",
    y="word_count"
)

plt.title("Average Document Length by Category")
plt.xlabel("Document Category")
plt.ylabel("Average Word Count")
plt.xticks(rotation=20)
plt.tight_layout()

plt.savefig(
    VISUAL_DIR / "average_words_by_category.png",
    dpi=300
)

plt.close()

# 5. Chunks by category
chunk_counts = (
    chunks.groupby("category")
    .size()
    .reset_index(name="chunk_count")
)

plt.figure(figsize=(9, 5))

sns.barplot(
    data=chunk_counts,
    x="category",
    y="chunk_count"
)

plt.title("Number of Text Chunks by Category")
plt.xlabel("Document Category")
plt.ylabel("Number of Chunks")
plt.xticks(rotation=20)
plt.tight_layout()

plt.savefig(
    VISUAL_DIR / "chunks_by_category.png",
    dpi=300
)

plt.close()

# 6. Save summary statistics
summary = documents.groupby("category")["word_count"].agg(
    document_count="count",
    average_words="mean",
    minimum_words="min",
    maximum_words="max"
).reset_index()

summary.to_csv(
    REPORT_DIR / "eda_summary_statistics.csv",
    index=False
)

# 7. Save category counts
category_counts.to_csv(
    REPORT_DIR / "eda_category_counts.csv",
    index=False
)

print("\nEDA charts saved successfully!")

print("\nGenerated charts:")
print("1. documents_by_category.png")
print("2. document_word_distribution.png")
print("3. average_words_by_category.png")
print("4. chunks_by_category.png")

print("\nEDA summary files:")
print("1. eda_summary_statistics.csv")
print("2. eda_category_counts.csv")

print("\nExploratory Data Analysis completed!")
