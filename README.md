# Exploratory Data Analysis (EDA) & Machine Learning Practice Repository

Welcome to the **Exploratory Data Analysis (EDA) & Machine Learning Practice Repository**. This repository contains a structured, modular collection of practice programs, real-world data analysis tasks, Jupyter Notebooks, and Machine Learning algorithms covering **NumPy**, **Pandas**, **Matplotlib**, **Seaborn**, and **Scikit-Learn**.

---

## 📌 Table of Contents

- [Overview & Objectives](#overview--objectives)
- [Repository Directory Structure](#repository-directory-structure)
- [Module Breakdown](#module-breakdown)
  - [01. NumPy Core Practice](#01-numpy-core-practice)
  - [02. Pandas Basics](#02-pandas-basics)
  - [03. Data Analysis Tasks & Projects](#03-data-analysis-tasks--projects)
  - [04. Machine Learning Modules](#04-machine-learning-modules)
- [How to Run the Code](#how-to-run-the-code)

---

## 🎯 Overview & Objectives

Exploratory Data Analysis (EDA) is the foundational phase of data science where datasets are cleaned, explored, and summarized to uncover underlying patterns, detect anomalies, test hypotheses, and verify assumptions before applying Machine Learning algorithms.

---

## 📂 Repository Directory Structure

```
EDA_PRATICE/
│
├── 01_NumPy/                                       # 17 Modular NumPy Practice Scripts
│   ├── 01_eda_intro.py                            # EDA lifecycle guide & runnable matrix overview
│   ├── 02_array_types_and_dimensions.py           # 1D, 2D, 3D arrays & attributes (.ndim, .shape, .dtype)
│   ├── 03_special_matrices.py                     # Zeros, Ones, Full, Identity & Eye matrices
│   ├── 04_reshape_and_flatten.py                  # arange sequence, reshape & flatten
│   ├── 05_arithmetic_operators.py                 # Element-wise math operators (+, -, *, /, %)
│   ├── 06_scalar_broadcasting.py                  # Scalar broadcasting & vector calculations
│   ├── 07_universal_functions.py                  # Built-in NumPy math ufuncs (add, sqrt, etc.)
│   ├── 08_sum_and_axis.py                         # Axis-wise sum calculations (axis=0, axis=1)
│   ├── 09_statistical_metrics.py                  # Statistical measures (mean, std, min, max)
│   ├── 10_array_slicing.py                        # 2D grid slicing & sub-matrix extraction
│   ├── 11_sorting_1d.py                           # Ascending & descending 1D sorting
│   ├── 12_index_positioning_argmax_argmin.py      # argsort, argmax, argmin in 1D & 2D arrays
│   ├── 13_conditional_where.py                    # Conditional searching & np.where substitution
│   ├── 14_sorting_2d.py                           # 2D matrix sorting along columns and rows
│   ├── 15_numpy_matrix_practice_task.py           # Comprehensive 4x4 matrix practice task
│   ├── 16_numpy_rounding_functions.py            # Floating-point rounding (np.round, np.floor, np.ceil)
│   └── 17_advanced_2d_sorting_and_reversal.py    # Descending 2D row sorting & matrix reversals
│
├── 02_Pandas_Basics/                               # 3 Introductory Pandas Scripts
│   ├── 01_pandas_intro.py                         # Overview of Pandas DataFrames & Series
│   ├── 02_series_practice.py                      # Series creation, indexing & operations
│   └── 03_dataframe_operations.py                 # DataFrame inspection, slicing & filtering
│
├── 03_Data_Analysis_Tasks/                         # 10 Self-contained Data Analysis Task Folders
│   ├── 01_Employee_Analysis/                      # Employee EDA & Data Visualization Task
│   ├── 02_Customer_Filtering_Task/                # Customer Data Filtering & Indexing Task
│   ├── 03_Department_Employee_Relational/         # Employee & Department Relational Query Task
│   ├── 04_Ecommerce_Orders_Task/                  # E-Commerce Orders Analysis Task
│   ├── 05_Relational_Joins_Sample/                # Relational Merges & Table Joins Practice
│   ├── 06_Iris_Classification_EDA/                # Iris Dataset EDA & Preprocessing Task
│   ├── 07_Health_Dataset_EDA/                     # Health & Medical Records EDA Task (Health.csv)
│   ├── 08_Loan_Prediction_EDA/                    # Loan Eligibility & Financial Risk EDA Task (loan.csv)
│   ├── 09_Weather_Data_EDA/                       # Weather Conditions Dataset EDA Task (weather.csv)
│   └── 10_Student_Performance_EDA/                # Student Attendance & Performance EDA Task
│
├── 04_Machine_Learning/                            # Machine Learning Theory & Supervised Algorithms
│   ├── 01_ML_Foundations/                         # ML Concepts, Classifications & KNN Theory
│   │   └── 01_ml_introduction_and_types.py        # Supervised/Unsupervised, Classification/Regression notes
│   │
│   ├── 02_KNN_Classification/                     # K-Nearest Neighbors (KNN) Classification Tasks
│   │   ├── 01_knn_student_result_prediction.ipynb # KNN on Hours & Attendance (Pass/Fail)
│   │   └── 02_knn_iris_flower_classification.ipynb# KNN Classification on Iris Flower Dataset
│   │
│   └── 03_Naive_Bayes_Classification/             # Naive Bayes Classifier & Probability Theory
│       ├── 01_probability_theory_intro.py         # Marginal, Joint, & Conditional Probability Theory
│       ├── 02_naive_bayes_probability_sample.ipynb# Probability calculations on Weather dataset
│       └── 03_weather_type_naive_bayes_task.ipynb # Naive Bayes Classification on Weather dataset
│
└── README.md                                       # Master repository documentation
```

---

## 📖 Module Breakdown

### 01. NumPy Core Practice
- Contains 17 standalone, fully annotated Python scripts covering array creation, matrix math, axis-wise aggregations, slicing, sorting, indexing, and rounding routines.

### 02. Pandas Basics
- Contains 3 Python scripts covering Pandas Series and DataFrame creation, indexing, column manipulation, and descriptive statistics.

### 03. Data Analysis Tasks & Projects
- **01_Employee_Analysis**: Full EDA workflow on `sample.csv` with Matplotlib visual charts (bar charts, horizontal bars, histograms, pie charts).
- **02_Customer_Filtering_Task**: Extensive `loc`/`iloc` indexing, boolean filtering, string matching, and groupby queries on customer records.
- **03_Department_Employee_Relational**: Relational queries on department and employee datasets.
- **04_Ecommerce_Orders_Task**: Revenue calculation (`Quantity * UnitPrice`), category/city aggregations, and top order rankings.
- **05_Relational_Joins_Sample**: Practice performing `inner`, `left`, `right`, and `outer` joins using `pd.merge()`.
- **06_Iris_Classification_EDA**: Exploratory Data Analysis, feature/target (`X` and `y`) separation, categorical label encoding, distribution plots, heatmaps, and Scikit-Learn `train_test_split` with `StandardScaler`.
- **07_Health_Dataset_EDA**: Exploratory Data Analysis on medical and health records (`Health.csv`).
- **08_Loan_Prediction_EDA**: Exploratory Data Analysis on financial loan applications (`loan.csv`).
- **09_Weather_Data_EDA**: Exploratory Data Analysis on meteorological conditions (`weather.csv`).
- **10_Student_Performance_EDA**: EDA on student study hours, attendance percentage, and exam results.

### 04. Machine Learning Modules
- **01_ML_Foundations**: Overview of Supervised vs Unsupervised learning, Classification vs Regression, KNN algorithm theory, and Euclidean distance formulas.
- **02_KNN_Classification**: Practical implementations of K-Nearest Neighbors Classifier (`KNeighborsClassifier`) on student result prediction and Iris flower species classification.
- **03_Naive_Bayes_Classification**: Probability theory (Marginal, Joint, Conditional probability, Bayes' Theorem) and Gaussian/Multinomial Naive Bayes model training with `pd.get_dummies` and `LabelEncoder`.

---

## 🚀 How to Run the Code

### Python Scripts
```bash
# Run any NumPy module script
python 01_NumPy/01_eda_intro.py

# Run Machine Learning theory script
python 04_Machine_Learning/01_ML_Foundations/01_ml_introduction_and_types.py
```

### Jupyter Notebooks
Launch Jupyter Notebook or JupyterLab to interact with documented notebooks in `03_Data_Analysis_Tasks/` and `04_Machine_Learning/`:
```bash
jupyter notebook
```
