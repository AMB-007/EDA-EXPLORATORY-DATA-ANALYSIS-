<div align="center">

# 📊 Exploratory Data Analysis (EDA) Practice

### *A Comprehensive Hands-on Suite for Data Wrangling, Relational Analysis & Visual Storytelling*

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/NumPy-1.24%2B-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" />
  <img src="https://img.shields.io/badge/Pandas-2.0%2B-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/Matplotlib-3.7%2B-11557c?style=for-the-badge&logo=python&logoColor=white" alt="Matplotlib" />
  <img src="https://img.shields.io/badge/Seaborn-0.12%2B-4c72b0?style=for-the-badge&logo=python&logoColor=white" alt="Seaborn" />
  <img src="https://img.shields.io/badge/Jupyter-Lab%20%2F%20Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" />
</p>

<p align="center">
  <b>Mastering the 5-Stage Exploratory Lifecycle:</b><br/>
  <i>Inspection &bull; Cleaning &bull; Transformation &bull; Visualization &bull; Business Insights</i>
</p>

</div>

---

## 📌 Table of Contents

- [🎯 Overview & Objectives](#-overview--objectives)
- [🧩 Module 1: NumPy Numerical Computing (17 Scripts)](#-module-1-numpy-numerical-computing)
- [🐼 Module 2: Pandas Tabular Manipulation (3 Scripts)](#-module-2-pandas-tabular-manipulation)
- [💼 Module 3: Real-World Data Analysis Tasks (10 Projects)](#-module-3-real-world-data-analysis-tasks)
- [📈 Module 4: Visual Figure Gallery](#-module-4-visual-figure-gallery)
- [🔄 The 5-Stage EDA Analytical Lifecycle](#-the-5-stage-eda-analytical-lifecycle)
- [🚀 Quick Start & Execution Guide](#-quick-start--execution-guide)

---

## 🎯 Overview & Objectives

**Exploratory Data Analysis (EDA)** is the foundational phase of data science where datasets are dissected, cleansed, transformed, and summarized to uncover hidden patterns, detect anomalies, test hypotheses, and verify assumptions through statistical summaries and visual graphs.

This repository offers an exhaustive, reproducible practice framework covering:
- **⚡ Numerical Arrays & Vectorization**: Multidimensional matrix slicing, broadcasting rules, ufuncs, and axis reductions with NumPy.
- **🧹 Tabular Data Wrangling**: Missing data handling, deduplication, type coercion, conditional subsetting, and grouping with Pandas.
- **🔗 Relational Database Analytics**: Table joins (`inner`, `left`, `right`, `outer`), foreign-key mapping, and cross-table metric aggregation.
- **🎨 Publication-Grade Visualization**: High-resolution distribution histograms, correlation heatmaps, categorical bar charts, pie charts, and pairwise scatter plots using Matplotlib and Seaborn.

---

## 🧩 Module 1: NumPy Numerical Computing

A 17-part modular script collection covering fundamental to advanced multidimensional array operations:

| # | Script Name | Core Concepts & Operations |
| :---: | :--- | :--- |
| **01** | [`01_eda_intro.py`](01_NumPy/01_eda_intro.py) | EDA lifecycle introduction, ndarray memory architecture & matrix creation |
| **02** | [`02_array_types_and_dimensions.py`](01_NumPy/02_array_types_and_dimensions.py) | 1D, 2D, 3D array memory layout, `.ndim`, `.shape`, `.size`, and `.dtype` |
| **03** | [`03_special_matrices.py`](01_NumPy/03_special_matrices.py) | Structural initializers: `np.zeros`, `np.ones`, `np.full`, `np.eye`, and `np.identity` |
| **04** | [`04_reshape_and_flatten.py`](01_NumPy/04_reshape_and_flatten.py) | Sequence generation (`np.arange`), dimension reshaping (`.reshape`), and `.flatten()` |
| **05** | [`05_arithmetic_operators.py`](01_NumPy/05_arithmetic_operators.py) | Vectorized element-wise math operators (`+`, `-`, `*`, `/`, `%`, `**`) |
| **06** | [`06_scalar_broadcasting.py`](01_NumPy/06_scalar_broadcasting.py) | Scalar-to-array broadcasting and dimension compatibility rules |
| **07** | [`07_universal_functions.py`](01_NumPy/07_universal_functions.py) | C-accelerated math ufuncs: `np.add`, `np.subtract`, `np.sqrt`, `np.power`, `np.exp` |
| **08** | [`08_sum_and_axis.py`](01_NumPy/08_sum_and_axis.py) | Axis-wise aggregation mechanics: column collapse (`axis=0`) vs row collapse (`axis=1`) |
| **09** | [`09_statistical_metrics.py`](01_NumPy/09_statistical_metrics.py) | Statistical measures: `np.mean`, `np.std`, `np.var`, `np.min`, `np.max` |
| **10** | [`10_array_slicing.py`](01_NumPy/10_array_slicing.py) | Multi-axis coordinate slicing `[row_start:row_end, col_start:col_end]` |
| **11** | [`11_sorting_1d.py`](01_NumPy/11_sorting_1d.py) | Ascending sorting (`np.sort`) and reverse indexing `[::-1]` |
| **12** | [`12_index_positioning_argmax_argmin.py`](01_NumPy/12_index_positioning_argmax_argmin.py) | Index search functions: `np.argsort`, `np.argmax`, and `np.argmin` across axes |
| **13** | [`13_conditional_where.py`](01_NumPy/13_conditional_where.py) | Boolean masking, condition filtering, and vectorized branching with `np.where` |
| **14** | [`14_sorting_2d.py`](01_NumPy/14_sorting_2d.py) | 2D matrix sorting along columns (`axis=0`) and rows (`axis=1`) |
| **15** | [`15_numpy_matrix_practice_task.py`](01_NumPy/15_numpy_matrix_practice_task.py) | Comprehensive 4x4 matrix diagnostic test assessing statistical aggregations |
| **16** | [`16_numpy_rounding_functions.py`](01_NumPy/16_numpy_rounding_functions.py) | IEEE 754 precision rounding: `np.round`, `np.floor`, `np.ceil`, and `np.trunc` |
| **17** | [`17_advanced_2d_sorting_and_reversal.py`](01_NumPy/17_advanced_2d_sorting_and_reversal.py) | Descending row-wise matrix sorting and 2D subgrid reversals |

---

## 🐼 Module 2: Pandas Tabular Manipulation

Foundational scripts introducing data structures, explicit coordinate slicing, and metadata auditing:

| # | Script Name | Focus Areas | Key Functions & Attributes |
| :---: | :--- | :--- | :--- |
| **01** | [`01_pandas_intro.py`](02_Pandas_Basics/01_pandas_intro.py) | Architecture & Primitives | `pd.Series`, `pd.DataFrame`, `.shape`, `.columns`, `.dtypes` |
| **02** | [`02_series_practice.py`](02_Pandas_Basics/02_series_practice.py) | 1D Series Manipulation | Index mapping, dictionary initialization, vectorized scalar operations |
| **03** | [`03_dataframe_operations.py`](02_Pandas_Basics/03_dataframe_operations.py) | Tabular Inspection & Querying | `.head()`, `.tail()`, `.info()`, `.describe()`, `.loc[]`, `.iloc[]`, boolean masking |

---

## 💼 Module 3: Real-World Data Analysis Tasks

Ten self-contained projects solving authentic business scenarios with real datasets and interactive Jupyter Notebooks:

| Task Folder | Domain | Dataset(s) | Analytical Highlights |
| :--- | :---: | :--- | :--- |
| [`01_Employee_Analysis`](03_Data_Analysis_Tasks/01_Employee_Analysis) | 🏢 HR Analytics | `sample.csv` | Workforce demographics, salary distribution, location-based age aggregation, and Matplotlib bar charts |
| [`02_Customer_Filtering_Task`](03_Data_Analysis_Tasks/02_Customer_Filtering_Task) | 👥 CRM / Retail | `customer5_windows.csv` | Complex `loc`/`iloc` indexing, regex string filtering, quantile segmentation, and missing value checks |
| [`03_Department_Employee_Relational`](03_Data_Analysis_Tasks/03_Department_Employee_Relational) | 🏢 Enterprise DB | `employees.csv`<br/>`departments.csv` | Foreign-key joins, department salary metrics, staff headcount audits, and unassigned staff detection |
| [`04_Ecommerce_Orders_Task`](03_Data_Analysis_Tasks/04_Ecommerce_Orders_Task) | 🛒 E-Commerce | `customers.csv`<br/>`orders.csv` | Total basket calculations (`Quantity * UnitPrice`), customer lifetime value (CLV), and category rankings |
| [`05_Relational_Joins_Sample`](03_Data_Analysis_Tasks/05_Relational_Joins_Sample) | 🔗 Database Joins | `custom_windows.csv`<br/>`order_windows.csv` | Exhaustive comparison of `inner`, `left`, `right`, and `outer` joins with `pd.merge()` and null handling |
| [`06_Iris_Classification_EDA`](03_Data_Analysis_Tasks/06_Iris_Classification_EDA) | 🌸 Botany / Bio | `Iris.csv` | Feature distribution spread, pairwise scatter plots with species hue, and correlation matrix heatmaps |
| [`07_Health_Dataset_EDA`](03_Data_Analysis_Tasks/07_Health_Dataset_EDA) | 🏥 Healthcare | `Health.csv` | Diagnostic record auditing, null value treatment, continuous biomarker spreads, and outlier detection |
| [`08_Loan_Prediction_EDA`](03_Data_Analysis_Tasks/08_Loan_Prediction_EDA) | 💳 FinTech / Credit | `loan.csv` | Applicant income distributions, credit history impacts, co-borrower dependencies, and approval rates |
| [`09_Weather_Data_EDA`](03_Data_Analysis_Tasks/09_Weather_Data_EDA) | ⛅ Meteorology | `weather.csv` | Climate trend analysis, temperature-humidity correlations, wind velocity, and weather condition shares |
| [`10_Student_Performance_EDA`](03_Data_Analysis_Tasks/10_Student_Performance_EDA) | 🎓 Education | In-memory records | Academic attendance vs study hours correlation, bivariate regression lines, and pass/fail distributions |

---

## 📈 Module 4: Visual Figure Gallery

All figures are programmatically generated using **Matplotlib** and **Seaborn** at publication quality (300 DPI) and stored in [`generated_figures/`](generated_figures):

| Categorical Comparison | Correlation Heatmap |
| :---: | :---: |
| ![Bar Chart](generated_figures/eda_bar_chart.png) | ![Heatmap](generated_figures/eda_heatmap.png) |
| **Frequency Distribution** | **Proportional Composition** |
| ![Histogram](generated_figures/eda_histogram.png) | ![Pie Chart](generated_figures/eda_pie_chart.png) |
| **Pairwise Relationship** | **Horizontal Ranking** |
| ![Scatter Plot](generated_figures/eda_scatterplot.png) | ![Horizontal Bar](generated_figures/eda_horizontal_bar.png) |

---

## 🔄 The 5-Stage EDA Analytical Lifecycle

Every dataset in this repository is processed through a structured analytical workflow:

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  1. Inspection  │ ──> │   2. Cleaning   │ ──> │ 3. Transformation│ ──> │4. Visualization │ ──> │   5. Insights   │
│                 │     │                 │     │                 │     │                 │     │                 │
│ .head(), .shape │     │ .isna().sum()   │     │ Type casting    │     │ Histograms      │     │ Summary tables  │
│ .info(), dtypes │     │ Imputation      │     │ Feature creation│     │ Heatmaps        │     │ Business KPIs   │
│ .describe()     │     │ Deduplication   │     │ GroupBy / Aggs  │     │ Scatter plots   │     │ Actionable tips │
└─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘
```

1. **Structural Auditing**: Examine dimensions (`.shape`), column names, and primitive memory types (`.dtypes`).
2. **Data Cleansing**: Detect null values (`.isna().sum()`), deduplicate records (`.drop_duplicates()`), and treat anomalous outliers.
3. **Data Transformation**: Mutate analytical columns, filter targeted cohorts, and compute aggregations (`.groupby()`, `.agg()`).
4. **Visual Exploration**: Plot distributions, categorical ratios, and multivariate correlations.
5. **Business Synthesis**: Interpret visual charts into actionable business findings.

---

## 🚀 Quick Start & Execution Guide

### 1. Environment Setup
Clone the repository and install the required data science packages:
```bash
git clone https://github.com/AMB-007/EDA-EXPLORATORY-DATA-ANALYSIS-.git
cd EDA-EXPLORATORY-DATA-ANALYSIS-
pip install numpy pandas matplotlib seaborn jupyter
```

### 2. Running Standalone Scripts
Execute any NumPy or Pandas module directly in your terminal:
```bash
# Run a NumPy numerical script
python 01_NumPy/01_eda_intro.py
python 01_NumPy/08_sum_and_axis.py

# Run a Pandas foundational script
python 02_Pandas_Basics/01_pandas_intro.py
```

### 3. Launching Interactive Notebooks
Open Jupyter Notebook or JupyterLab to interact with any task:
```bash
jupyter notebook
```
Navigate to any task directory (e.g., `03_Data_Analysis_Tasks/01_Employee_Analysis/`) and run the `.ipynb` notebook.

---

<div align="center">
  <sub>Maintained with ❤️ for clean data analysis, reproducible workflows, and visual data exploration.</sub>
</div>
