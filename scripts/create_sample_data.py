
from pathlib import Path
import csv
from datetime import date

# Main project directory
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"

# Create category folders
categories = [
    "course_guides",
    "assignment_instructions",
    "student_faqs",
    "policies"
]

for category in categories:
    (RAW_DIR / category).mkdir(parents=True, exist_ok=True)

# Synthetic educational documents created for CampusAssist.
# These are examples, NOT official university policies.

documents = [
    {
        "id": "DOC001",
        "title": "Introduction to Data Science",
        "category": "course_guides",
        "filename": "introduction_to_data_science.txt",
        "content": """
Course: Introduction to Data Science

This course introduces students to the fundamentals of data science.
Students learn how to collect, organize, clean, analyse and interpret data.

Main topics include Python programming, data types, statistics,
data visualization and exploratory data analysis.

Learning outcomes:
1. Understand basic data science concepts.
2. Work with structured datasets.
3. Perform basic data cleaning.
4. Create charts and interpret findings.
"""
    },
    {
        "id": "DOC002",
        "title": "Introduction to Artificial Intelligence",
        "category": "course_guides",
        "filename": "introduction_to_ai.txt",
        "content": """
Course: Introduction to Artificial Intelligence

This course introduces artificial intelligence concepts and applications.

Topics include machine learning, neural networks, natural language
processing, computer vision and responsible AI.

Students explore how AI systems learn from data and how they
can be evaluated for accuracy, reliability and fairness.
"""
    },
    {
        "id": "DOC003",
        "title": "Database Management Fundamentals",
        "category": "course_guides",
        "filename": "database_fundamentals.txt",
        "content": """
Course: Database Management Fundamentals

This course explains how databases store and organize information.

Topics include relational databases, SQL queries, primary keys,
foreign keys, normalization and database transactions.

Students learn to create tables, retrieve records and understand
the importance of data integrity.
"""
    },
    {
        "id": "DOC004",
        "title": "Data Science Assignment Guidelines",
        "category": "assignment_instructions",
        "filename": "data_science_assignment.txt",
        "content": """
Assignment: Data Science Analysis

Students must select a suitable dataset and perform exploratory
data analysis.

Required activities:
1. Describe the dataset and its source.
2. Identify missing and duplicate values.
3. Clean and prepare the data.
4. Calculate summary statistics.
5. Create meaningful visualizations.
6. Explain the findings.

The submission should include a report and supporting code.
"""
    },
    {
        "id": "DOC005",
        "title": "AI Project Submission Instructions",
        "category": "assignment_instructions",
        "filename": "ai_project_submission.txt",
        "content": """
Assignment: Artificial Intelligence Project

Students must identify a problem that can be addressed using AI.

The project report should explain the problem, objectives,
dataset, methodology, technology choices and evaluation approach.

Students should provide supporting implementation files
and describe the limitations of their solution.

All project claims should be supported by actual work and evidence.
"""
    },
    {
        "id": "DOC006",
        "title": "Presentation Submission Guide",
        "category": "assignment_instructions",
        "filename": "presentation_submission.txt",
        "content": """
Assignment: Project Presentation

Students must prepare a presentation describing their project.

Suggested sections include:
1. Project introduction.
2. Problem statement.
3. Objectives.
4. Proposed solution.
5. Technology and methodology.
6. Results and conclusions.

Slides should be readable and information should be presented
in a clear and organized manner.
"""
    },
    {
        "id": "DOC007",
        "title": "How should I submit an assignment?",
        "category": "student_faqs",
        "filename": "assignment_submission_faq.txt",
        "content": """
Question: How should I submit an assignment?

Answer: Follow the submission instructions provided with the
specific assignment. Check the required file format and upload
your completed work through the designated submission platform.

Question: Should I check my submission?

Answer: Yes. Confirm that the correct file has been uploaded
and that the submission status is visible.
"""
    },
    {
        "id": "DOC008",
        "title": "What should a project report contain?",
        "category": "student_faqs",
        "filename": "project_report_faq.txt",
        "content": """
Question: What should a project report contain?

Answer: A typical project report includes an introduction,
problem statement, objectives, methodology, implementation,
results, limitations and conclusion.

Question: Should I include references?

Answer: Yes. Include references for external sources
used in your project.
"""
    },
    {
        "id": "DOC009",
        "title": "What is exploratory data analysis?",
        "category": "student_faqs",
        "filename": "eda_faq.txt",
        "content": """
Question: What is exploratory data analysis?

Answer: Exploratory data analysis, also called EDA, is the
process of examining a dataset to understand its structure,
quality, distributions and relationships.

Question: Which tools can be used?

Answer: Python libraries such as Pandas, Matplotlib and
Seaborn are commonly used for data analysis and visualization.
"""
    },
    {
        "id": "DOC010",
        "title": "Academic Integrity Guidelines",
        "category": "policies",
        "filename": "academic_integrity.txt",
        "content": """
Sample Academic Integrity Guidelines

Students should submit original work and acknowledge
external sources appropriately.

Copying another person's work without attribution
is not acceptable.

Students should follow the academic integrity requirements
published by their own educational institution.

This is a synthetic example and is not an official policy.
"""
    },
    {
        "id": "DOC011",
        "title": "Sample Assignment Extension Guidelines",
        "category": "policies",
        "filename": "assignment_extension.txt",
        "content": """
Sample Assignment Extension Guidelines

Students who need additional time should contact the
appropriate course coordinator or academic support team.

Any extension request should follow the institution's
official process and applicable deadlines.

Approval is not automatic and depends on the applicable rules.

This is a synthetic example and is not an official policy.
"""
    },
    {
        "id": "DOC012",
        "title": "Sample Student Support Guidelines",
        "category": "policies",
        "filename": "student_support.txt",
        "content": """
Sample Student Support Guidelines

Students may contact academic support services for help
with course requirements, learning resources and assignment
instructions.

Students should use official institutional communication
channels for personal or confidential matters.

This is a synthetic example and is not an official policy.
"""
    }
]

# Save documents and create metadata
metadata = []

for doc in documents:
    file_path = RAW_DIR / doc["category"] / doc["filename"]

    file_path.write_text(
        doc["content"].strip(),
        encoding="utf-8"
    )

    metadata.append({
        "document_id": doc["id"],
        "title": doc["title"],
        "category": doc["category"],
        "file_name": doc["filename"],
        "source_type": "synthetic",
        "source_reference": "Created for CampusAssist project",
        "collection_date": str(date.today()),
        "format": "TXT"
    })

# Save metadata CSV
metadata_path = RAW_DIR / "document_metadata.csv"

with open(metadata_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=metadata[0].keys())
    writer.writeheader()
    writer.writerows(metadata)

print("CampusAssist data collection completed!")
print("Total documents created:", len(documents))
print("Metadata file:", metadata_path)
print("Data location:", RAW_DIR)
print("\nDocuments by category:")

for category in categories:
    count = len(list((RAW_DIR / category).glob("*.txt")))
    print(f"{category}: {count}")
