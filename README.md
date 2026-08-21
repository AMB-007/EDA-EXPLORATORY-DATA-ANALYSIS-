# Exploratory Data Analysis (EDA) & NumPy Practice Repository

Welcome to the **Exploratory Data Analysis (EDA) & NumPy Practice Repository**. This repository contains a structured, 15-part step-by-step modular code collection covering fundamental to intermediate operations in Python for data science, vector math, array manipulation, and statistical analysis.

---

## 📌 Table of Contents

- [Overview & Objectives](#overview--objectives)
- [Python Data Science Ecosystem](#python-data-science-ecosystem)
- [Module Architecture & Program Index](#module-architecture--program-index)
- [Detailed Module Breakdown](#detailed-module-breakdown)
  - [Module 1: EDA Foundations & Array Creation](#module-1-eda-foundations--array-creation)
  - [Module 2: Array Generation & Structural Transformations](#module-2-array-generation--structural-transformations)
  - [Module 3: Arithmetic & Vectorized Operations](#module-3-arithmetic--vectorized-operations)
  - [Module 4: Aggregations & Statistical Summaries](#module-4-aggregations--statistical-summaries)
  - [Module 5: Slicing, Indexing, Searching & Sorting](#module-5-slicing-indexing-searching--sorting)
  - [Module 6: Comprehensive Practice Tasks](#module-6-comprehensive-practice-tasks)
- [Key NumPy Concepts Quick Reference](#key-numpy-concepts-quick-reference)
- [How to Run the Scripts](#how-to-run-the-scripts)

---

## 🎯 Overview & Objectives

Exploratory Data Analysis (EDA) is the foundational phase of data science where datasets are cleaned, explored, and summarized to uncover underlying patterns, detect anomalies, test hypotheses, and verify assumptions before applying Machine Learning algorithms.

---

## 📂 Module Architecture & Program Index

```
EDA_PRATICE/
│
├── 01_eda_intro.py                         # Detailed EDA lifecycle & toolset intro
├── 02_array_types_and_dimensions.py        # 1D, 2D, 3D arrays & inspection attributes
├── 03_special_matrices.py                  # Zeros, Ones, Full, Identity & Eye matrices
├── 04_reshape_and_flatten.py               # Sequence generation, reshaping & flattening
├── 05_arithmetic_operators.py              # Element-wise operators (+, -, *, /, %)
├── 06_scalar_broadcasting.py               # Scalar broadcasting & vector calculations
├── 07_universal_functions.py               # Explicit NumPy ufuncs (add, sqrt, etc.)
├── 08_sum_and_axis.py                      # Axis-wise sum calculations (axis=0, axis=1)
├── 09_statistical_metrics.py               # Statistical measures (mean, std, min, max)
├── 10_array_slicing.py                     # 2D grid slicing & sub-matrix extraction
├── 11_sorting_1d.py                        # Ascending & descending 1D array sorting
├── 12_index_positioning_argmax_argmin.py   # argsort, argmax, argmin in 1D & 2D arrays
├── 13_conditional_where.py                 # Conditional searching & value substitution
├── 14_sorting_2d.py                        # 2D matrix sorting along columns and rows
├── 15_numpy_matrix_practice_task.py        # Comprehensive 4x4 matrix operations practice task
└── README.md                               # Detailed repository documentation
```

---

## 📖 Detailed Module Breakdown

### Module 1: EDA Foundations & Array Creation
- [`01_eda_intro.py`](file:///d:/EDA_PRATICE/01_eda_intro.py): Comprehensive overview of EDA lifecycle (Data Inspection, Cleaning, Univariate, Bivariate, Modeling Prep).
- [`02_array_types_and_dimensions.py`](file:///d:/EDA_PRATICE/02_array_types_and_dimensions.py): Demonstrates 1D, 2D, 3D arrays, `.ndim`, `.shape`, `.dtype`.

### Module 2: Array Generation & Structural Transformations
- [`03_special_matrices.py`](file:///d:/EDA_PRATICE/03_special_matrices.py): `zeros`, `ones`, `full`, `identity`, `eye`.
- [`04_reshape_and_flatten.py`](file:///d:/EDA_PRATICE/04_reshape_and_flatten.py): `arange`, `reshape`, `flatten`.

### Module 3: Arithmetic & Vectorized Operations
- [`05_arithmetic_operators.py`](file:///d:/EDA_PRATICE/05_arithmetic_operators.py): Element-wise `+`, `-`, `*`, `/`, `%`.
- [`06_scalar_broadcasting.py`](file:///d:/EDA_PRATICE/06_scalar_broadcasting.py): Scalar multiplication and addition.
- [`07_universal_functions.py`](file:///d:/EDA_PRATICE/07_universal_functions.py): `np.add`, `np.subtract`, `np.multiply`, `np.divide`, `np.sqrt`.

### Module 4: Aggregations & Statistical Summaries
- [`08_sum_and_axis.py`](file:///d:/EDA_PRATICE/08_sum_and_axis.py): Sum across axes (`axis=None`, `axis=0`, `axis=1`).
- [`09_statistical_metrics.py`](file:///d:/EDA_PRATICE/09_statistical_metrics.py): `mean`, `min`, `max`, `std`.

### Module 5: Slicing, Indexing, Searching & Sorting
- [`10_array_slicing.py`](file:///d:/EDA_PRATICE/10_array_slicing.py): 2D grid slicing & sub-matrix extraction.
- [`11_sorting_1d.py`](file:///d:/EDA_PRATICE/11_sorting_1d.py): Ascending & descending 1D array sorting.
- [`12_index_positioning_argmax_argmin.py`](file:///d:/EDA_PRATICE/12_index_positioning_argmax_argmin.py): `argsort`, `argmax`, `argmin` in 1D & 2D.
- [`13_conditional_where.py`](file:///d:/EDA_PRATICE/13_conditional_where.py): Conditional searching & value substitution (`np.where`).
- [`14_sorting_2d.py`](file:///d:/EDA_PRATICE/14_sorting_2d.py): 2D matrix sorting along columns and rows.

### Module 6: Comprehensive Practice Tasks
- [`15_numpy_matrix_practice_task.py`](file:///d:/EDA_PRATICE/15_numpy_matrix_practice_task.py): Comprehensive 4x4 matrix operations practice combining attribute inspection, indexing, slicing, aggregations, argmax/argmin index positioning, and 2D row-wise sorting.

---

## 🚀 How to Run the Scripts

Execute any script individually from the terminal:
```bash
python 15_numpy_matrix_practice_task.py
```
