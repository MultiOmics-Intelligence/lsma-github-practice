# Summarise the example counts: mean per condition and log2 fold change per gene.
# Run from the top folder of the repository:
#   Rscript r/summary.R
# Uses base R only.

counts  <- read.csv("data/example_counts.csv", row.names = "gene")
samples <- read.csv("data/samples.csv")

control <- samples$sample[samples$condition == "control"]
treated <- samples$sample[samples$condition == "treated"]

summary <- data.frame(
  mean_control = round(rowMeans(counts[, control]), 1),
  mean_treated = round(rowMeans(counts[, treated]), 1)
)
summary$log2_fold_change <- round(log2(summary$mean_treated / summary$mean_control), 2)
summary <- summary[order(summary$log2_fold_change), ]

print(summary)
write.csv(summary, "results_summary.csv")
cat("\nSaved results_summary.csv\n")
