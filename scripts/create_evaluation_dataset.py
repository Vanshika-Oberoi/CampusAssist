
import pandas as pd
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
METADATA_FILE = BASE_DIR / "data" / "raw" / "document_metadata.csv"
OUTPUT_DIR = BASE_DIR / "data" / "evaluation"
OUTPUT_FILE = OUTPUT_DIR / "test_questions.csv"

# Load document metadata
metadata = pd.read_csv(METADATA_FILE)

# Test questions based on the actual sample documents.
# source_file is used to look up the correct document ID.
questions = [
    {
        "question_id": "Q001",
        "question": "What topics are covered in the Introduction to Data Science course?",
        "expected_answer": "The course covers Python programming, data types, statistics, data visualization, data collection, data cleaning and exploratory data analysis.",
        "source_file": "introduction_to_data_science.txt",
        "is_answerable": True,
        "expected_behavior": "Answer using the course guide."
    },
    {
        "question_id": "Q002",
        "question": "Which topics are introduced in the Artificial Intelligence course?",
        "expected_answer": "The course introduces machine learning, neural networks, natural language processing, computer vision and responsible AI.",
        "source_file": "introduction_to_ai.txt",
        "is_answerable": True,
        "expected_behavior": "Answer using the course guide."
    },
    {
        "question_id": "Q003",
        "question": "What database concepts are covered in Database Management Fundamentals?",
        "expected_answer": "The course covers relational databases, SQL queries, primary keys, foreign keys, normalization and database transactions.",
        "source_file": "database_fundamentals.txt",
        "is_answerable": True,
        "expected_behavior": "Answer using the course guide."
    },
    {
        "question_id": "Q004",
        "question": "What activities are required for the Data Science Analysis assignment?",
        "expected_answer": "Students must describe the dataset and its source, identify missing and duplicate values, clean and prepare the data, calculate summary statistics, create visualizations and explain findings.",
        "source_file": "data_science_assignment.txt",
        "is_answerable": True,
        "expected_behavior": "Answer using the assignment instructions."
    },
    {
        "question_id": "Q005",
        "question": "What should be included in an Artificial Intelligence project report?",
        "expected_answer": "The report should explain the problem, objectives, dataset, methodology, technology choices and evaluation approach. Students should also provide implementation files and describe limitations.",
        "source_file": "ai_project_submission.txt",
        "is_answerable": True,
        "expected_behavior": "Answer using the assignment instructions."
    },
    {
        "question_id": "Q006",
        "question": "Which sections are suggested for the project presentation?",
        "expected_answer": "Suggested sections include project introduction, problem statement, objectives, proposed solution, technology and methodology, results and conclusions.",
        "source_file": "presentation_submission.txt",
        "is_answerable": True,
        "expected_behavior": "Answer using the presentation instructions."
    },
    {
        "question_id": "Q007",
        "question": "How should a student submit an assignment?",
        "expected_answer": "Students should follow the specific assignment instructions, check the required file format and upload completed work through the designated submission platform. They should confirm that the correct file was uploaded and the submission status is visible.",
        "source_file": "assignment_submission_faq.txt",
        "is_answerable": True,
        "expected_behavior": "Answer using the student FAQ."
    },
    {
        "question_id": "Q008",
        "question": "What is exploratory data analysis and which tools can be used?",
        "expected_answer": "Exploratory data analysis is the process of examining a dataset to understand its structure, quality, distributions and relationships. Python libraries such as Pandas, Matplotlib and Seaborn can be used.",
        "source_file": "eda_faq.txt",
        "is_answerable": True,
        "expected_behavior": "Answer using the student FAQ."
    },
    {
        "question_id": "Q009",
        "question": "What should a typical project report contain?",
        "expected_answer": "A typical project report includes an introduction, problem statement, objectives, methodology, implementation, results, limitations and conclusion. References should be included for external sources.",
        "source_file": "project_report_faq.txt",
        "is_answerable": True,
        "expected_behavior": "Answer using the student FAQ."
    },
    {
        "question_id": "Q010",
        "question": "What do the sample academic integrity guidelines say about copying another person's work?",
        "expected_answer": "The sample guidelines state that students should submit original work and acknowledge external sources. Copying another person's work without attribution is not acceptable. These are synthetic example guidelines, not official institutional policy.",
        "source_file": "academic_integrity.txt",
        "is_answerable": True,
        "expected_behavior": "Answer with a clear synthetic-example disclaimer."
    },
    {
        "question_id": "Q011",
        "question": "What should students do if they need an assignment extension according to the sample guidelines?",
        "expected_answer": "Students should contact the appropriate course coordinator or academic support team and follow the institution's official process and applicable deadlines. Approval is not automatic. These are synthetic example guidelines, not official institutional policy.",
        "source_file": "assignment_extension.txt",
        "is_answerable": True,
        "expected_behavior": "Answer with a clear synthetic-example disclaimer."
    },
    {
        "question_id": "Q012",
        "question": "Where can students seek help with course requirements and learning resources according to the sample support guidelines?",
        "expected_answer": "Students may contact academic support services and should use official institutional communication channels for personal or confidential matters. These are synthetic example guidelines, not official institutional policy.",
        "source_file": "student_support.txt",
        "is_answerable": True,
        "expected_behavior": "Answer with a clear synthetic-example disclaimer."
    },
    {
        "question_id": "Q013",
        "question": "What is the exact deadline for submitting the Artificial Intelligence project?",
        "expected_answer": "The provided documents do not specify an exact submission deadline. The assistant should not guess and should direct the student to the official assignment instructions or submission platform.",
        "source_file": None,
        "is_answerable": False,
        "expected_behavior": "Abstain because the information is not available."
    },
    {
        "question_id": "Q014",
        "question": "How many marks is the Data Science Analysis assignment worth?",
        "expected_answer": "The provided documents do not specify the assignment's marks or grading weight. The assistant should not invent a value.",
        "source_file": None,
        "is_answerable": False,
        "expected_behavior": "Abstain because the information is not available."
    },
    {
        "question_id": "Q015",
        "question": "What is the official university rule for late assignment submissions?",
        "expected_answer": "The dataset does not contain an official university late-submission policy. The extension document is only a synthetic example. The assistant should direct the student to official institutional sources.",
        "source_file": None,
        "is_answerable": False,
        "expected_behavior": "Abstain and clarify that no official policy is available."
    }
]

# Match source filenames to metadata and attach document IDs/categories
metadata_lookup = metadata.set_index("file_name").to_dict("index")

for item in questions:
    source_file = item.pop("source_file")

    if source_file:
        if source_file not in metadata_lookup:
            raise ValueError(f"Document missing from metadata: {source_file}")

        item["expected_document_id"] = metadata_lookup[source_file]["document_id"]
        item["expected_category"] = metadata_lookup[source_file]["category"]
    else:
        item["expected_document_id"] = ""
        item["expected_category"] = ""

# Create output folder and save dataset
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.DataFrame(questions)
df.to_csv(OUTPUT_FILE, index=False)

print("CAMPUSASSIST EVALUATION DATASET")
print("================================")
print(f"Total test questions: {len(df)}")
print(f"Answerable questions: {df['is_answerable'].sum()}")
print(f"Unanswerable questions: {(~df['is_answerable']).sum()}")

print("\nQuestions by category:")
print(df[df["expected_category"] != ""]["expected_category"].value_counts())

print("\nEvaluation dataset saved successfully:")
print(OUTPUT_FILE)

print("\nPreview:")
print(df[["question_id", "expected_document_id", "is_answerable"]].to_string(index=False))
