"""Summarise the example counts: mean per condition and log2 fold change per gene.

Run from the top folder of the repository:
    python python/summary.py
Needs pandas (pip install pandas).
"""
import math
import pandas as pd

counts = pd.read_csv("data/example_counts.csv", index_col="gene")
samples = pd.read_csv("data/samples.csv")

control = samples.loc[samples["condition"] == "control", "sample"]
treated = samples.loc[samples["condition"] == "treated", "sample"]

summary = pd.DataFrame({
    "mean_control": counts[control].mean(axis=1).round(1),
    "mean_treated": counts[treated].mean(axis=1).round(1),
})
summary["log2_fold_change"] = [
    round(math.log2(t / c), 2) for c, t in zip(summary["mean_control"], summary["mean_treated"])
]
summary = summary.sort_values("log2_fold_change")

print(summary.to_string())
summary.to_csv("results_summary.csv")
print("\nSaved results_summary.csv")
