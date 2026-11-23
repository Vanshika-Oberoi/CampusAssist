import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPORTS = ROOT / "reports"
RESULTS = pd.read_csv(REPORTS / "retrieval_evaluation_results.csv")
COMPARISON = pd.read_csv(REPORTS / "model_comparison.csv")

# Graph 1: Model performance comparison
metrics = ["top1_accuracy", "mrr", "recall_at_3"]
labels = ["Top-1 Accuracy", "MRR", "Recall@3"]

ax = COMPARISON.set_index("model")[metrics].plot(
    kind="bar", figsize=(9, 5), ylim=(0, 1.1)
)
ax.set_title("Retrieval Model Performance Comparison")
ax.set_ylabel("Score")
ax.set_xlabel("Model")
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
ax.legend(labels)
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig(REPORTS / "model_performance_comparison.png", dpi=200)
plt.close()

# Graph 2: Average top similarity score
answerable = RESULTS[RESULTS["is_answerable"] == True]
similarity = answerable.groupby("model")["top_similarity_score"].mean()

ax = similarity.plot(kind="bar", figsize=(8, 5))
ax.set_title("Average Top Similarity Score")
ax.set_ylabel("Average Cosine Similarity")
ax.set_xlabel("Model")
ax.tick_params(axis="x", rotation=0)
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig(REPORTS / "average_similarity_comparison.png", dpi=200)
plt.close()

# Graph 3: Correct vs incorrect retrievals
counts = answerable.groupby("model")["top1_correct"].value_counts().unstack(fill_value=0)
counts = counts.rename(columns={True: "Correct", False: "Incorrect"})

ax = counts.plot(kind="bar", figsize=(8, 5))
ax.set_title("Correct vs Incorrect Top-1 Retrievals")
ax.set_ylabel("Number of Questions")
ax.set_xlabel("Model")
ax.tick_params(axis="x", rotation=0)
ax.legend(title="Result")
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig(REPORTS / "retrieval_correctness_comparison.png", dpi=200)
plt.close()

print("Model visualizations generated successfully!")
for name in [
    "model_performance_comparison.png",
    "average_similarity_comparison.png",
    "retrieval_correctness_comparison.png",
]:
    print(REPORTS / name)
