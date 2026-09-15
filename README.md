# Exploratory Data Analysis (EDA) & Python Data Science Practice Repository

Welcome to the **Exploratory Data Analysis (EDA) & Python Data Science Practice Repository**. This repository contains a structured, modular collection of practice programs, real-world data analysis tasks, and Jupyter Notebooks covering **NumPy**, **Pandas**, **Matplotlib**, **Seaborn**, and **Scikit-Learn**.

---

## 📌 Table of Contents

- [Overview & Objectives](#overview--objectives)
- [Repository Directory Structure](#repository-directory-structure)
- [Module Breakdown](#module-breakdown)
  - [01. NumPy Core Practice](#01-numpy-core-practice)
  - [02. Pandas Basics](#02-pandas-basics)
  - [03. Data Analysis Tasks & Projects](#03-data-analysis-tasks--projects)
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
├── 03_Data_Analysis_Tasks/                         # 6 Self-contained EDA Tasks with Datasets & Notebooks
│   ├── 01_Employee_Analysis/                      # Employee EDA & Data Visualization Task
│   │   ├── sample.csv                             # Employee CSV dataset
│   │   ├── employee_eda_and_visualization.ipynb  # Documented Jupyter Notebook (37 cells)
│   │   ├── employee_script.py                     # Python execution script
│   │   └── avg_age_by_location.png                # Saved visualization plot
│   │
│   ├── 02_Customer_Filtering_Task/                # Customer Data Filtering & Indexing Task
│   │   ├── customer5_windows.csv                  # Customer CSV dataset
│   │   └── customer_data_filtering_task.ipynb     # Documented Jupyter Notebook (82 cells)
│   │
│   ├── 03_Department_Employee_Relational/         # Employee & Department Relational Query Task
│   │   ├── departments.csv                        # Departments dataset
│   │   ├── employees.csv                          # Employees dataset
│   │   ├── set_2.pdf                              # Task instructions PDF
│   │   └── employee_department_relational_task.ipynb # Documented Jupyter Notebook (85 cells)
│   │
│   ├── 04_Ecommerce_Orders_Task/                  # E-Commerce Orders Analysis Task
│   │   ├── customers.csv                          # Customers dataset
│   │   ├── orders.csv                             # Orders dataset
│   │   ├── pandas_join_task_questions.pdf         # Task instructions PDF
│   │   └── ecommerce_orders_analysis_task.ipynb   # Documented Jupyter Notebook (106 cells)
│   │
│   ├── 05_Relational_Joins_Sample/                # Relational Merges & Table Joins Practice
│   │   ├── custom_windows.csv                     # Customers dataset
│   │   ├── order_windows.csv                      # Orders dataset
│   │   └── pandas_relational_merges_practice.ipynb# Documented Jupyter Notebook (22 cells)
│   │
│   └── 06_Iris_Classification_EDA/                # Iris Dataset EDA & Train-Test Splitting Task
│       ├── Iris.csv                               # Iris CSV dataset
│       └── iris_eda_and_classification.ipynb      # Documented Jupyter Notebook (50 cells)
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
- **Employee Analysis**: Full EDA workflow on `sample.csv` with Matplotlib visual charts (bar charts, horizontal bars, histograms, pie charts).
- **Customer Filtering Task**: Extensive `loc`/`iloc` indexing, boolean filtering, string matching, and groupby queries on customer records.
- **Department & Employee Relational**: Relational queries on department and employee datasets.
- **E-Commerce Orders Task**: Revenue calculation (`Quantity * UnitPrice`), category/city aggregations, and top order rankings.
- **Relational Joins Sample**: Practice performing `inner`, `left`, `right`, and `outer` joins using `pd.merge()`.
- **Iris Classification EDA**: Complete Exploratory Data Analysis, feature/target (`X` and `y`) separation, categorical label encoding, distribution plots, heatmaps, and Scikit-Learn `train_test_split` with `StandardScaler`.

---

## 🚀 How to Run the Code

### Python Scripts
```bash
# Run any NumPy module script
python 01_NumPy/01_eda_intro.py

# Run any Pandas module script
python 02_Pandas_Basics/01_pandas_intro.py
```

### Jupyter Notebooks
Launch Jupyter Notebook or JupyterLab to interact with documented notebooks in `03_Data_Analysis_Tasks/`:
```bash
jupyter notebook
```
