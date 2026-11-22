<a href="https://lsma.co.uk/courses"><img src="https://raw.githubusercontent.com/MultiOmics-Intelligence/.github/main/assets/lsma-walk-courses.svg" alt="LSMA, London School of Multiomics and AI: learn by doing, on real data" width="100%"></a>

# Welcome to the LSMA GitHub practice repository

From **MultiOmics Intelligence** and **LSMA, the London School of Multiomics & AI**.

This repository is a safe place to practise GitHub. It goes with the *GitHub essentials* lessons and study guide in the LSMA free courses: Omics, Bioinformatics and AI; Introduction to Python; and Introduction to R. You will make your own copy, change it, and finish with a small, tidy, citable repository that you can show to others.

- LSMA website and free courses: https://lsma.co.uk/courses
- MultiOmics Intelligence: https://multiomicsintelligence.co.uk
- Follow us on GitHub: https://github.com/MultiOmics-Intelligence

> Everything in this repository is made up for practice. The counts in `data/` are **synthetic**: they are not from any person, patient or real experiment.

## What is inside

| Path | What it is |
|---|---|
| `data/example_counts.csv` | Synthetic read counts for 10 genes in 6 samples |
| `data/samples.csv` | Which samples are control and which are treated |
| `python/summary.py` | Mean per condition and log2 fold change, in Python (needs pandas) |
| `r/summary.R` | The same summary in R (base R only) |
| `MY_ANALYSIS.md` | A page for you to fill in during the tasks |
| `CHECKLIST.md` | Tick off each task as you finish it |
| `.gitignore` | Files git should never track |
| `LICENSE` | MIT licence |

## The practice task: six steps

Do the steps in order. Each one matches a lesson in *GitHub essentials*; the study guide explains every step in detail.

### 1. Make your own copy (Lesson 1)
At the top of this page choose **Use this template**, then **Create a new repository**. Set yourself as the owner, name it, for example, `my-first-analysis`, choose **Public**, and create it. You now have your own copy with a fresh history. (You cannot change this repository directly, and you do not need to.)

### 2. Clone it and run the code (Lesson 2)
Clone **your** copy to your computer, then run one of the scripts from the top folder:

```
git clone https://github.com/YOUR-USERNAME/my-first-analysis.git
cd my-first-analysis
python python/summary.py      # or: Rscript r/summary.R
```

You should see a table of 10 genes, from CDKN2A (lowest fold change) to MYC (highest), and a new file `results_summary.csv`.

### 3. Describe your analysis (Lessons 1 and 2)
Fill in `MY_ANALYSIS.md`: your name, what the script does, and which two genes change most. Then add `results_summary.csv` to `.gitignore` (outputs that a script can recreate do not need to be tracked). Commit with a clear message and push.

### 4. Improve it on a branch and merge with a pull request (Lesson 3)
Open an issue in your copy, for example *Add a plot of the fold changes*. Make a branch, make the change (a plot, a clearer README, or a filter for genes with low counts), push the branch, open a pull request whose description says `Closes #1`, read the diff in **Files changed**, and merge it.

### 5. Make it citable and release it (Lesson 4)
Add a file called `CITATION.cff` with your own details (there is an example in the study guide), then publish release `v1.0.0` from **Releases**.

### 6. Check it and share it (Lesson 4)
Read through your copy and its history: no personal data, no passwords or keys, no large files. Then open your repository link in a private browser window, where you are not signed in. If it opens and shows your README, you are done: this is exactly the test a marker uses for LSMA project links. Pin it on your profile.

## Stuck?

- The *GitHub essentials* study guide has a troubleshooting table and a command cheat sheet.
- GitHub's own help: https://docs.github.com
- Questions about LSMA courses: info@lsma.co.uk

If this repository helped you, give it a star and follow **MultiOmics Intelligence** on GitHub.

---

**Follow LSMA**

<p>
  <a href="https://lsma.co.uk"><img src="https://raw.githubusercontent.com/MultiOmics-Intelligence/.github/main/assets/btn-lsma-website.svg" alt="LSMA: lsma.co.uk" height="54"></a>
  <a href="https://www.linkedin.com/showcase/113252126/"><img src="https://raw.githubusercontent.com/MultiOmics-Intelligence/.github/main/assets/btn-lsma-linkedin.svg" alt="LSMA on LinkedIn" height="54"></a>
  <a href="https://www.instagram.com/lsma.uk/"><img src="https://raw.githubusercontent.com/MultiOmics-Intelligence/.github/main/assets/btn-lsma-instagram.svg" alt="LSMA on Instagram: @lsma.uk" height="54"></a>
  <a href="mailto:info@lsma.co.uk"><img src="https://raw.githubusercontent.com/MultiOmics-Intelligence/.github/main/assets/btn-lsma-email.svg" alt="Email: info@lsma.co.uk" height="54"></a>
</p>

Welcome, and enjoy the course.

**Dr. Anas Alzaeem**<br>
Academic Director, LSMA

[![Dr. Anas Alzaeem, Academic Director, LSMA](https://raw.githubusercontent.com/MultiOmics-Intelligence/.github/main/assets/signature/LSMA_Banner_Anas_Alzaeem.png)](https://lsma.co.uk)

© 2026 MultiOmics Intelligence Ltd. LSMA is the education arm of MultiOmics Intelligence. Code licensed under MIT.
