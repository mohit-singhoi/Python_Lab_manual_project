
**Python Lab Manual: Practical Exercises & Mini-Projects**

## Overview

This repository contains a sequence of hands-on lab exercises that teach core Python programming, data manipulation, visualization, numerical computing with NumPy, data analysis with Pandas, and fundamental machine learning workflows. It is designed for undergraduate or postgraduate students taking a lab course or for anyone who wants a practical, example-driven introduction to Python-based data science.

The labs progress from basic programming concepts to complete end-to-end machine learning projects, covering 19 topics:

1. Demonstrate variables, different data types, and arithmetic operations.
2. Implement if-elif-else conditions and loops (for, while) with real-world examples.
3. Create Python functions for mathematical operations and demonstrate reading/writing files.
4. Store and manipulate data using different data structures (lists, tuples, dicts, sets).
5. Use NumPy for array operations.
6. Use NumPy for indexing and slicing.
7. Pandas for data manipulation (load CSV, basic analysis).
8. Handle missing values.
9. Normalize and regularize numerical features.
10. Use visualization techniques (histograms).
11. Use visualization techniques (heatmaps).
12. Use visualization techniques (scatter plots).
13. Train a Linear Regression model on a dataset (e.g., house price prediction) and evaluate performance.
14. Implement Logistic Regression to classify a dataset (e.g., predicting student pass/fail).
15. Train and visualize a Decision Tree model for classification tasks.
16. Implement k-NN for classification problems and find the optimal k value.
17. Apply k-Means clustering on an unlabeled dataset and visualize cluster formation.
18. Compare multiple ML models using metrics like confusion matrix, precision, recall, and F1-score.
19. Implement an end-to-end ML project (e.g., spam detection, customer churn) and supply a detailed `README.md` for the project.

---

## Repository Structure (recommended)

LAB_MANNUAL_PROJECT/
├── .git/
├── DataSets/
├── Images/
├── Lab19/
├── Lab20_House_Price_P...
├── model/
├── lab1.py
├── lab2.py
├── lab3.py
├── lab4.py
├── lab5.py
├── lab6.py
├── Lab7.py
├── Lab8.py
├── Lab9.py
├── Lab10.py
├── Lab11.py
├── Lab12.py
├── Lab13.py
├── Lab14.py
├── Lab15.py
├── Lab16.py
├── Lab17.py
├── Lab18.py
└── results.txt

---

## Prerequisites

* Python 3.8+
* Recommended packages (listed in `requirements.txt`):

  * numpy
  * pandas
  * matplotlib
  * scikit-learn
  * seaborn
  * jupyterlab or notebook

Install with:

```bash
pip install -r requirements.txt
```

---

## How to use this Lab Manual

1. Clone the repository.
2. Review the dataset(s) in the `data/` folder.
3. Open a notebook from `notebooks/` in JupyterLab or Jupyter Notebook.
4. Run cells sequentially. Each notebook contains: learning objectives, brief theory, step-by-step code, exercises, and a mini assignment.

Each topic notebook follows a consistent layout:

* **Objective** — what you will learn
* **Theory** — short conceptual notes
* **Code walkthrough** — runnable examples
* **Exercises** — tasks for practice
* **Mini assignment** — small project to test learning

---

## Topic highlights (what you'll find in the notebooks)

### 1 — Variables, data types, arithmetic

* Demonstrations of `int`, `float`, `str`, `bool`, and type conversion.
* Arithmetic operators and simple expressions.
* Small exercises: calculate student grade percentages, currency conversion snippet.

### 2 — Control flow: if/elif/else and loops

* Real-world examples: grade categorization, attendance counting.
* `for` loops, `while` loops, `break`/`continue` usage.
* Exercise: implement passing criteria and aggregate statistics.

### 3 — Functions and file I/O

* `def` functions for math ops (add, subtract, factorial, gcd).
* Reading/writing CSV and text files with `open()` and `pandas`.
* Example: function to compute class averages and save results to a file.

### 4 — Data structures

* Use and manipulation of `list`, `tuple`, `dict`, `set`.
* When to use which structure, time complexity notes, examples.
* Exercise: aggregate student marks using dictionaries.

### 5–6 — NumPy arrays, operations, indexing, slicing

* Creating arrays, broadcasting, vectorized ops, reshaping.
* Indexing, boolean masking, fancy indexing and slicing examples.
* Exercises: normalize arrays, compute column-wise statistics.

### 7 — Pandas for data manipulation

* Loading CSV (`pd.read_csv`), inspecting data (`head()`, `info()`, `describe()`), filtering, groupby.
* Exercise: load `students.csv` and compute subject-wise averages.

### 8 — Handling missing values

* Detect (`isnull()`), drop (`dropna()`), and impute (`fillna()`, `SimpleImputer`) strategies.
* Case studies: mean/median imputation, forward/backward fill.

### 9 — Normalization & Regularization

* Scaling: MinMaxScaler, StandardScaler, RobustScaler.
* Regularization concepts (brief): L1 vs L2, where used (linear/logistic regression).
* Exercises: scale features for regression model.

### 10–12 — Visualizations

* Histograms: distribution of age, marks, prices.
* Heatmaps: correlation matrices (Pearson) for feature relationships.
* Scatter plots: relationship between features (e.g., sqft vs price).
* Each notebook contains plotting code using `matplotlib` and `seaborn` plus interpretation notes.

### 13 — Linear Regression

* Train/test split, fit a linear regression model, calculate RMSE, MAE, R².
* Visualize predictions vs actual values and residuals.

### 14 — Logistic Regression

* Binary classification (e.g., pass/fail), confusion matrix, precision, recall, ROC curve.

### 15 — Decision Tree

* Train a decision tree classifier, visualize with `plot_tree`, discuss overfitting and pruning.

### 16 — k-NN

* Implement k-NN using `sklearn.neighbors.KNeighborsClassifier`, use cross-validation to find optimal `k`.

### 17 — k-Means clustering

* Run k-Means, elbow method to choose k, visualize clusters on 2D PCA projection.

### 18 — Model comparison

* Train several models (Logistic Regression, Decision Tree, k-NN, SVM optionally), compare via confusion matrix, precision, recall, F1-score, and classification report.

### 19 — End-to-end ML project

* A complete project folder that includes: data, EDA notebook, preprocessing script, model training notebook, evaluation, saved model, and a project-level `README.md` (this file also describes how to run the project and interpret results).

---

## Example commands

* Run Jupyter Lab: & Vs Code

```bash
jupyter lab
```

* Run a notebook to train a model (example):

```bash
python src/train_model.py --config configs/linear_regression.yaml
```

(If you prefer notebooks only, open `notebooks/13_linear_regression.ipynb`.)

---

## Datasets & Sources

* Small synthetic datasets are included in `data/` for exercises.
* For larger examples (house prices, spam detection) we recommend using public datasets such as the UCI repository, Kaggle datasets, or generated synthetic data. Always include a `data/README.md` in the project folder describing the dataset and its license.

---

## Assessment & Exercises

Each notebook ends with exercises and a mini-assignment. Suggested grading rubric for assignments:

* Correctness of code: 40%
* Code readability and comments: 20%
* Analysis and interpretation of results: 30%
* Plots and visualizations quality: 10%

---

## Contributing

Contributions are welcome. Suggested workflow:

1. Fork the repo.
2. Create a branch `feature/<topic-number-summary>`.
3. Add notebooks or improve explanations.
4. Open a pull request with a description of changes.

---


