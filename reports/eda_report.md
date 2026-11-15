# Exploratory Data Analysis Report

**Project:** CampusAssist  
**Date:** 2026-11-15  
**Module:** 3 - Data Preparation

## 1. Objective

Explore the prepared document corpus to understand its size,
category distribution and text-length characteristics.

## 2. Dataset Overview

- Number of documents: 12
- Number of chunks: 12
- Number of categories: 4
- Average document length: 49.83 words
- Minimum document length: 40 words
- Maximum document length: 64 words

## 3. Category Distribution

category
course_guides              3
assignment_instructions    3
student_faqs               3
policies                   3

The corpus contains an equal number of documents in each category.

## 4. Word Count Analysis

count    12.00
mean     49.83
std       7.07
min      40.00
25%      45.25
50%      49.50
75%      54.25
max      64.00

## 5. Average Word Count by Category

                         count   mean  min  max
category                                       
assignment_instructions      3  53.00   48   57
course_guides                3  50.33   41   64
policies                     3  47.33   43   52
student_faqs                 3  48.67   40   55

## 6. Visualizations

The following charts were generated:

1. documents_by_category.png
2. document_word_distribution.png
3. average_words_by_category.png
4. chunks_by_category.png

All charts are stored in the visualizations directory.

## 7. Key Findings

- The dataset contains 12 documents across four categories.
- Each category contains three documents.
- Document lengths range from 40 to 64 words.
- Every current document produces one chunk.
- The current corpus is evenly distributed by category.

## 8. Limitations

The small synthetic dataset limits the generalizability of findings.
The balanced category distribution was created during sample data
generation and should not be interpreted as a real university
document distribution.

No predictive correlation or model-performance conclusions
can be drawn from this descriptive analysis alone.

## 9. Conclusion

EDA provided an initial understanding of the prepared corpus.
The generated summaries and visualizations can guide future
dataset expansion and retrieval experiments.
