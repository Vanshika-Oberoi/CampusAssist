# Data Preparation Report

**Project:** CampusAssist  
**Date:** 2026-11-15  
**Module:** 3 - Data Preparation

## 1. Objective

Prepare the raw text corpus for document retrieval and future
RAG-based question answering.

## 2. Cleaning Activities

The preparation script performs:
- Text file loading
- Line-ending normalization
- Whitespace normalization
- Removal of unnecessary blank lines
- Empty-document checks
- Metadata association

## 3. Dataset Summary

- Raw documents: 12
- Cleaned documents: 12
- Generated text chunks: 12
- Average cleaned document length: 49.83 words
- Average chunk length: 49.83 words

## 4. Chunking Strategy

The preparation process uses a configured chunk size of 100 words
and an overlap of 20 words.

All current documents are shorter than 100 words. Therefore,
each document generated one chunk and the overlap was not needed.

Larger documents should be tested in future iterations to evaluate
the effect of chunk size and overlap on retrieval quality.

## 5. Feature Preparation

The prepared datasets retain useful retrieval metadata:
- document_id
- chunk_id
- title
- category
- source_type
- chunk_index
- content
- word_count

These fields support document identification, filtering,
retrieval and source attribution.

## 6. Validation

The prepared data validation script recorded:
- Total automated checks: 13
- Passed checks: 13
- Warnings: 0

These checks assess structural consistency and completeness,
not semantic accuracy.

## 7. Output Files

- data/processed/cleaned_documents.csv
- data/chunks/document_chunks.csv
- data/chunks/document_chunks.json
- data/evaluation/test_questions.csv

## 8. Conclusion

The initial corpus was cleaned, organized and converted into
retrieval-ready text chunks. The prepared dataset passed all
13 recorded automated validation checks.
