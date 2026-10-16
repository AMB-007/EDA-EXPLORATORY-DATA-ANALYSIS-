# Exploratory Data Analysis (EDA) & Machine Learning Practice Repository

Welcome to the **Exploratory Data Analysis (EDA) & Machine Learning Practice Repository**. This repository contains a structured, modular collection of practice programs, real-world data analysis tasks, Jupyter Notebooks, Machine Learning algorithms, and a publication-grade study handbook covering **NumPy**, **Pandas**, **Matplotlib**, **Seaborn**, and **Scikit-Learn**.

---

## 📚 Study Guide & Reference Notes

For in-depth explanations, formal definitions, and syntax examples covering every topic in this repository:
- **Downloadable PDF Handbook**: [`EDA_and_Machine_Learning_Comprehensive_Notes.pdf`](file:///d:/EDA_PRATICE/EDA_and_Machine_Learning_Comprehensive_Notes.pdf)
- **Markdown Notes Companion**: [`NOTES.md`](file:///d:/EDA_PRATICE/NOTES.md)

---

## 📌 Table of Contents

- [Overview & Objectives](#overview--objectives)
- [Study Guide & Reference Notes](#-study-guide--reference-notes)
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
├── EDA_and_Machine_Learning_Comprehensive_Notes.pdf  # 49-Page Master Reference Handbook (Eye-Comfort Palette)
├── NOTES.md                                         # Complete Markdown Reference Notes Companion
├── generated_figures/                               # 7 Publication-Quality 300-DPI Visualizations
├── scripts/
│   └── build_comprehensive_pdf.py                  # Standalone ReportLab PDF Generator
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
├── 04_Machine_Learning/                            # Machine Learning Modules (Classification & Regression)
│   ├── 00_ML_Foundations/                         # ML Taxonomies & Foundational Paradigms
│   │   └── 01_ml_introduction_and_types.py        # Supervised vs Unsupervised, Classification vs Regression
│   │
│   ├── 01_Classification/                         # Supervised Classification Algorithms & Tasks
│   │   ├── 01_KNN/                                # K-Nearest Neighbors (KNN)
│   │   │   ├── 01_Student_Result_Prediction/      # 01_knn_student_result_prediction.ipynb
│   │   │   ├── 02_Iris_Classification/            # 02_knn_iris_flower_classification.ipynb
│   │   │   ├── 03_Diabetes_Classification/        # diabetes.csv, diabetes_knn_classification.ipynb
│   │   │   └── 04_Student_Performance_Multiclass/ # Student_performance_data.csv, student_performance_classification.ipynb
│   │   │
│   │   ├── 02_Naive_Bayes/                        # Naive Bayes & Probability Theory
│   │   │   ├── 01_Probability_Theory/             # 01_probability_theory_intro.py, 02_naive_bayes_probability_sample.ipynb
│   │   │   ├── 02_Weather_Classification/         # 03_weather_type_naive_bayes_task.ipynb
│   │   │   ├── 03_Heart_Disease_Prediction/       # heart.csv, heart_disease_naive_bayes.ipynb
│   │   │   └── 04_Loan_Approval_Prediction/       # loan_train.csv, loan_approval_naive_bayes.ipynb
│   │   │
│   │   ├── 03_Decision_Trees/                     # Decision Trees & Information Gain
│   │   │   ├── 01_Theory_and_Concepts/            # 01_decision_tree_intro.py
│   │   │   ├── 02_Play_Tennis_Task/               # play_tennis_dataset.csv, play_tennis_decision_tree.ipynb
│   │   │   └── 03_Breast_Cancer_Classification/   # Breast_Cancer.csv, breast_cancer_decision_tree.ipynb
│   │   │
│   │   ├── 04_Random_Forest/                      # Ensemble Learning & Random Forest Classifiers
│   │   │   ├── 01_Car_Evaluation/                 # car_evaluation.csv, car_evaluation_random_forest.ipynb
│   │   │   ├── 02_Car_Price_Classification/       # cars_data.csv, car_price_random_forest.ipynb
│   │   │   └── 03_Instagram_Reach_Analysis/       # Instagram.csv, instagram_random_forest.ipynb
│   │   │
│   │   └── 05_Hybrid_Classification_Projects/     # Multi-Model Benchmark & Comparative Studies
│   │       └── 01_Employee_Turnover_KNN_vs_NB/    # Employee.csv, Employee_ML_Classification_Tasks.pdf, employee_classification_task.ipynb
│   │
│   └── 02_Regression/                             # Supervised Regression Algorithms & Continuous Modeling
│       ├── 01_Linear_Regression_Foundations/      # house_area_linear_regression.ipynb
│       ├── 02_Salary_Prediction/                  # Salary_Data.csv, salary_linear_regression.ipynb
│       └── 03_Watermelon_Quality_Prediction/      # melon.csv, watermelon_linear_regression.ipynb
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

#### 00_ML_Foundations
- Comprehensive overview of Supervised vs. Unsupervised learning, Classification vs. Regression taxonomies, distance metrics (Euclidean, Manhattan, Minkowski), and standard machine learning lifecycle workflows.

#### 01_Classification
- **01_KNN (K-Nearest Neighbors)**:
  - *Student Result Prediction*: Basic 2D feature KNN model predicting pass/fail from study hours and attendance.
  - *Iris Classification*: Multiclass classification of Iris flower species with 4 continuous features.
  - *Diabetes Classification*: Pima Indians diagnostic prediction handling hidden zero imputation, robust scaling, $K$-tuning, and ROC-AUC analysis.
  - *Student Performance Multiclass*: 5-class student academic performance classification (`GradeClass` 0 to 4) addressing data leakage and ordinal class balances.
- **02_Naive_Bayes**:
  - *Probability Theory*: Scripted and notebook demonstrations of Marginal, Joint, and Conditional probability and Bayes' Theorem.
  - *Weather Classification*: Multi-feature categorical Naive Bayes classification with one-hot encoding.
  - *Heart Disease Prediction*: Clinical diagnosis classifying cardiovascular risk using Gaussian Naive Bayes with feature scaling.
  - *Loan Approval Prediction*: Creditworthiness and financial risk classification with categorical encoding and missing value imputation.
- **03_Decision_Trees**:
  - *Theory & Concepts*: Python script covering root node selection, Shannon Entropy, Information Gain, Gini Impurity, and tree pruning mechanics.
  - *Play Tennis Task*: Classic decision tree classification mapping weather outlook, humidity, and wind conditions to binary game play.
  - *Breast Cancer Classification*: Diagnostic classification on medical tumor features with tree visualization and recall optimization.
- **04_Random_Forest**:
  - *Car Evaluation*: Multi-attribute vehicle acceptability classification using Random Forest ensemble bagging and ordinal encoding.
  - *Car Price Classification*: Large-scale vehicle dataset (97,000+ records) discretized into market segments (Budget, Mid-Range, Luxury) achieving 90%+ classification accuracy.
  - *Instagram Reach Analysis*: Fake account detection and engagement reach classification comparing Random Forest, KNN, Naive Bayes, and Decision Trees.
- **05_Hybrid_Classification_Projects**:
  - *Employee Turnover (KNN vs. NB)*: Rigorous, 19-task implementation comparing KNN and Gaussian Naive Bayes retention models on enterprise HR data.

#### 02_Regression
- **01_Linear_Regression_Foundations**: Simple Ordinary Least Squares (OLS) regression modeling house area vs. sale price ($y = mx + c$) with trendline plotting and unseen area forecasting.
- **02_Salary_Prediction**: Univariate linear regression predicting compensation from years of experience with `MinMaxScaler`, $R^2$, MAE, RMSE metrics, and regression scatter plots.
- **03_Watermelon_Quality_Prediction**: Fruit price estimation based on watermelon weight ($kg$), evaluating correlation heatmaps, model coefficients, and prediction error bounds.

---

## 🚀 How to Run the Code & Regenerate the PDF

### Regenerating the PDF Notes
```bash
python scripts/build_comprehensive_pdf.py
```

### Running Python Scripts
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
