
# Data Preparation Report

**Project:** CampusAssist  
**Date:** 2026-11-15  
**Module:** 3 - Data Preparation

## 1. Objective

The objective of data preparation was to clean, organize and transform the CampusAssist text corpus into a structured format suitable for document retrieval and future Retrieval-Augmented Generation (RAG) development.

## 2. Cleaning Activities

The preparation script performs the following activities:

- Loads the original text documents.
- Normalizes line endings.
- Normalizes unnecessary whitespace.
- Removes unnecessary blank lines.
- Checks for empty documents.
- Associates documents with their metadata.
- Calculates word counts.

A total of 12 raw documents were processed, producing 12 cleaned documents.

## 3. Dataset Summary

| Metric | Result |
|---|---:|
| Raw documents | 12 |
| Cleaned documents | 12 |
| Generated text chunks | 12 |
| Feature-engineered chunks | 12 |
| Average cleaned document length | 49.83 words |
| Average chunk length | 49.83 words |
| Missing values in feature-engineered dataset | 0 |

The original corpus contains four categories: course guides, assignment instructions, student FAQs and sample policies.

## 4. Chunking Strategy

The preparation process uses a configured chunk size of 100 words and an overlap of 20 words.

All current documents are shorter than 100 words. Therefore, each document generated one chunk, and overlap was not required.

Larger documents should be tested in future iterations to evaluate the effect of chunk size and overlap on retrieval quality.

## 5. Feature Engineering

Feature engineering was performed on the prepared document chunks to extract additional text-based characteristics.

Five new features were added:

| Feature | Description |
|---|---|
| character_count | Total number of characters in a text chunk. |
| sentence_count | Number of sentences identified using sentence punctuation. |
| avg_word_length | Average number of characters per word. |
| has_question | Indicates whether a chunk contains a question mark. |
| has_number | Indicates whether a chunk contains a numeric digit. |

These features provide additional information about the structure and characteristics of each text chunk.

The feature-engineered dataset contains 12 rows and 13 columns, including the original chunk fields and five additional features.

The sentence count is based on a simple punctuation-based method and may not identify every sentence perfectly.

## 6. Outlier and Data Quality Considerations

The initial data quality assessment found:

- No empty source documents.
- No duplicate source documents.
- No unreadable documents.
- No missing metadata records.
- No documents below the minimum content threshold used by the quality check.

No statistical outlier removal was performed. The corpus is small, and removing documents based only on text length could remove useful information.

The feature-engineered dataset was also checked for missing values. All 13 columns contained zero missing values.

## 7. Validation

The initial prepared-data validation included 13 structural checks. Following feature engineering, 7 additional checks were added.

The updated validation script recorded:

- Total automated checks: 20
- Passed checks: 20
- Warnings: 0

The checks cover document IDs, metadata, chunk references, word counts, evaluation question references, feature completeness and feature calculation consistency.

These checks assess structural consistency and calculated feature values. They do not establish semantic accuracy, factual correctness or retrieval performance.

The validation results are saved in `reports/prepared_data_validation.csv`.


## 8. Output Files

The following files were generated during data preparation:

- `data/processed/cleaned_documents.csv`
- `data/chunks/document_chunks.csv`
- `data/chunks/document_chunks.json`
- `data/processed/feature_engineered_chunks.csv`
- `data/evaluation/test_questions.csv`
- `data_dictionary/data_dictionary.csv`
- `data_dictionary/data_dictionary.md`

## 9. Conclusion

The CampusAssist corpus was cleaned, organized, chunked and enriched with five additional text-based features.

The feature-engineered dataset provides a more detailed representation of the text chunks and can support future retrieval analysis and model development.

The current dataset is a small synthetic prototype. Further testing with larger, approved and representative educational documents is required before evaluating real-world retrieval quality or using the system in an institutional environment.
