# Exploratory Data Analysis (EDA) Practice Repository

A structured, hands-on repository dedicated to **Exploratory Data Analysis (EDA)**, data manipulation, relational database analysis, and visual data exploration using **Python**, **NumPy**, **Pandas**, **Matplotlib**, and **Seaborn**.

---

## 📌 Table of Contents

- [Overview & Objectives](#-overview--objectives)
- [Repository Directory Structure](#-repository-directory-structure)
- [Module Breakdown](#-module-breakdown)
  - [01. NumPy Core Practice](#01-numpy-core-practice)
  - [02. Pandas Basics](#02-pandas-basics)
  - [03. Data Analysis Tasks & Projects](#03-data-analysis-tasks--projects)
  - [04. Generated Figures & Visualizations](#04-generated-figures--visualizations)
- [EDA Workflow & Analytical Techniques](#-eda-workflow--analytical-techniques)
- [How to Run the Code](#-how-to-run-the-code)

---

## 🎯 Overview & Objectives

**Exploratory Data Analysis (EDA)** is the fundamental analytical process of inspecting, cleaning, transforming, and visualizing datasets to discover underlying patterns, detect anomalies, test hypotheses, and verify assumptions through statistical and graphical representations.

This repository provides practical, reproducible scripts and interactive Jupyter Notebooks covering:
- **Numerical Computing**: Multidimensional array manipulation, vectorization, and matrix operations with NumPy.
- **Data Wrangling**: Data cleaning, missing value imputation, type casting, filtering, and indexing with Pandas.
- **Relational Analytics**: Relational table merges, inner/left/right/outer joins, and cross-table aggregations.
- **Data Visualization**: Statistical distribution charts, correlation heatmaps, pairwise scatter plots, bar charts, and pie charts using Matplotlib and Seaborn.

---

## 📂 Repository Directory Structure

```
EDA_PRATICE/
│
├── 01_NumPy/                                       # 17 Modular NumPy Numerical Computing Scripts
│   ├── 01_eda_intro.py                            # EDA lifecycle & ndarray matrix fundamentals
│   ├── 02_array_types_and_dimensions.py           # 1D, 2D, 3D arrays & attributes (.ndim, .shape, .dtype)
│   ├── 03_special_matrices.py                     # Zeros, Ones, Full, Eye, and Identity matrices
│   ├── 04_reshape_and_flatten.py                  # arange sequence generation, reshape, and flatten
│   ├── 05_arithmetic_operators.py                 # Vectorized element-wise arithmetic (+, -, *, /, %)
│   ├── 06_scalar_broadcasting.py                  # Scalar broadcasting rules and dimension alignment
│   ├── 07_universal_functions.py                  # NumPy ufuncs (add, subtract, sqrt, power, exp)
│   ├── 08_sum_and_axis.py                         # Axis-wise reductions (axis=0 columns, axis=1 rows)
│   ├── 09_statistical_metrics.py                  # Statistical metrics (mean, std, min, max, var)
│   ├── 10_array_slicing.py                        # 2D subgrid slicing and coordinate indexing
│   ├── 11_sorting_1d.py                           # Ascending and descending 1D vector sorting
│   ├── 12_index_positioning_argmax_argmin.py      # argsort, argmax, and argmin in 1D and 2D arrays
│   ├── 13_conditional_where.py                    # Boolean masking and np.where conditional assignment
│   ├── 14_sorting_2d.py                           # Row-wise and column-wise 2D matrix sorting
│   ├── 15_numpy_matrix_practice_task.py           # Comprehensive 4x4 matrix diagnostic task
│   ├── 16_numpy_rounding_functions.py            # Floating-point rounding (np.round, floor, ceil, trunc)
│   └── 17_advanced_2d_sorting_and_reversal.py    # Descending row sorting and matrix reversals
│
├── 02_Pandas_Basics/                               # 3 Foundational Pandas Practice Scripts
│   ├── 01_pandas_intro.py                         # Introduction to Pandas Series and DataFrames
│   ├── 02_series_practice.py                      # 1D Series creation, custom indexing, and vector math
│   └── 03_dataframe_operations.py                 # DataFrame inspection, loc/iloc slicing, and filtering
│
├── 03_Data_Analysis_Tasks/                         # 10 Real-World Data Analysis Projects & Tasks
│   ├── 01_Employee_Analysis/                      # HR Employee EDA & Matplotlib Visualization
│   │   ├── avg_age_by_location.png                # Rendered location-wise age bar chart
│   │   ├── employee_eda_and_visualization.ipynb   # Full interactive EDA notebook
│   │   ├── employee_script.py                     # Standalone Python script
│   │   └── sample.csv                             # Employee demographic dataset
│   │
│   ├── 02_Customer_Filtering_Task/                # Customer Records Querying & Filtering
│   │   ├── customer5_windows.csv                  # Multi-attribute customer dataset
│   │   └── customer_data_filtering_task.ipynb     # Complex loc/iloc queries, regex & boolean masking
│   │
│   ├── 03_Department_Employee_Relational/         # Multi-Table Relational Analysis
│   │   ├── departments.csv                        # Department metadata table
│   │   ├── employees.csv                          # Employee roster table
│   │   └── employee_department_relational_task.ipynb# Foreign-key joins, salary metrics & department groupings
│   │
│   ├── 04_Ecommerce_Orders_Task/                  # E-Commerce Transactional Analysis
│   │   ├── customers.csv                          # Customer demographic records
│   │   ├── orders.csv                             # Transactional order records
│   │   └── ecommerce_orders_analysis_task.ipynb   # Revenue computation, top spenders & category breakdown
│   │
│   ├── 05_Relational_Joins_Sample/                # Relational Merges & Joins Practice
│   │   ├── custom_windows.csv                     # Customer profile records
│   │   ├── order_windows.csv                      # Transactional order records
│   │   └── pandas_relational_merges_practice.ipynb# Inner, Left, Right, and Outer joins with pd.merge
│   │
│   ├── 06_Iris_Classification_EDA/                # Botanical Dataset Exploratory Analysis
│   │   ├── Iris.csv                               # Fisher's Iris flower dataset
│   │   └── iris_eda_and_classification.ipynb      # Pair plots, correlation heatmaps & feature distributions
│   │
│   ├── 07_Health_Dataset_EDA/                     # Clinical & Healthcare Data Analysis
│   │   ├── Health.csv                             # Patient diagnostic & clinical records
│   │   └── health_records_eda.ipynb               # Outlier auditing, null imputation & statistical summaries
│   │
│   ├── 08_Loan_Prediction_EDA/                    # Financial Credit & Loan Assessment
│   │   ├── loan.csv                               # Applicant financial & credit risk dataset
│   │   └── loan_eligibility_eda.ipynb             # Income distributions, approval ratios & bivariate charts
│   │
│   ├── 09_Weather_Data_EDA/                       # Meteorological Time & Atmosphere Analysis
│   │   ├── weather.csv                            # Atmospheric observation dataset
│   │   └── weather_data_eda.ipynb                 # Temperature, humidity, and weather condition trends
│   │
│   └── 10_Student_Performance_EDA/                # Academic Attendance & Performance Analysis
│       └── student_performance_eda.ipynb          # Study hours, attendance correlation & grade distributions
│
├── generated_figures/                              # Visual Figures Created During EDA Workflows
│   ├── eda_bar_chart.png                          # Categorical distribution bar chart
│   ├── eda_horizontal_bar.png                     # Horizontal ranking bar chart
│   ├── eda_histogram.png                          # Continuous frequency distribution histogram
│   ├── eda_pie_chart.png                          # Proportional composition chart
│   ├── eda_scatterplot.png                        # Pairwise feature scatter plot
│   └── eda_heatmap.png                            # Multivariate correlation matrix heatmap
│
└── README.md                                       # Master repository documentation
```

---

## 📖 Module Breakdown

### 01. NumPy Core Practice
Contains 17 standalone, fully annotated Python scripts exploring numerical linear algebra and array computations:
- **Array Architecture**: 1D, 2D, and 3D ndarray creation, memory inspection (`.ndim`, `.shape`, `.size`, `.dtype`).
- **Matrix Generation**: Special initializers (`zeros`, `ones`, `full`, `eye`, `identity`, `arange`, `linspace`).
- **Shape Transformations**: Dimension reshaping (`reshape`), flattening (`flatten`), and multi-axis transposition.
- **Vectorized Mathematics**: Element-wise arithmetic operators and scalar broadcasting across differing dimensions.
- **Universal Functions (ufuncs)**: Optimized C-level mathematical functions (`add`, `subtract`, `multiply`, `sqrt`, `power`).
- **Statistical Reductions**: Axis-wise aggregation (`sum`, `mean`, `std`, `var`, `min`, `max`, `argmin`, `argmax`).
- **Subgrid Slicing & Indexing**: Coordinate-based 2D matrix slicing, boolean masking, and conditional substitution with `np.where`.
- **Sorting Routines**: In-place and out-of-place 1D sorting, 2D row/column sorting, and descending multi-axis reversals.

### 02. Pandas Basics
Contains 3 foundational scripts covering tabular data wrangling primitives:
- **Pandas Series**: 1D labeled array creation from lists and dictionaries, custom index alignment, and vector operations.
- **DataFrame Primitives**: 2D tabular data structures, column selection, index positioning, and schema introspection (`.info()`, `.describe()`, `.dtypes`).
- **Data Filtering & Subsetting**: Label-based indexing (`loc`), integer position indexing (`iloc`), and conditional boolean querying.

### 03. Data Analysis Tasks & Projects
Ten self-contained projects featuring real-world datasets and production-style Jupyter Notebooks:
1. **01_Employee_Analysis**: Complete workforce demographic analysis on `sample.csv`. Covers salary statistics, location-based age aggregation, and Matplotlib figure creation (`avg_age_by_location.png`).
2. **02_Customer_Filtering_Task**: Intensive querying on `customer5_windows.csv` utilizing chained boolean logic, substring matching, regex pattern searches, and quantile segmentations.
3. **03_Department_Employee_Relational**: Enterprise relational query tasks merging `employees.csv` and `departments.csv`. Evaluates department salary expenditures, staff counts, and unassigned department audits.
4. **04_Ecommerce_Orders_Task**: Retail transaction analysis joining `customers.csv` and `orders.csv`. Calculates total basket values (`Quantity * UnitPrice`), customer lifetime values, and category revenue rankings.
5. **05_Relational_Joins_Sample**: Comprehensive relational join guide on `custom_windows.csv` and `order_windows.csv`. Explores `inner`, `left`, `right`, and `outer` joins using `pd.merge()`, clarifying join cardinality and null generation.
6. **06_Iris_Classification_EDA**: Fisher's classic botanical dataset analysis. Features sepal and petal dimension distributions, pairwise scatter plots with hue differentiation, and correlation matrix heatmaps.
7. **07_Health_Dataset_EDA**: Healthcare records analysis on `Health.csv`. Focuses on missing data diagnostics, continuous biomarker distribution spreads, and demographic stratification.
8. **08_Loan_Prediction_EDA**: Financial credit risk exploration on `loan.csv`. Evaluates applicant income distributions, credit history impacts, co-borrower dependencies, and loan status approval rates.
9. **09_Weather_Data_EDA**: Meteorological observations analysis on `weather.csv`. Correlates temperature, humidity, wind speed, and precipitation patterns across climatic conditions.
10. **10_Student_Performance_EDA**: Academic dataset exploration evaluating the statistical correlation between study hours, attendance percentages, and exam passing outcomes.

### 04. Generated Figures & Visualizations
High-resolution charts exported during exploratory workflows illustrating best practices in visual data storytelling:
- **Bar Charts (`eda_bar_chart.png` & `eda_horizontal_bar.png`)**: Comparing discrete categorical quantities and ranked metrics.
- **Histogram (`eda_histogram.png`)**: Evaluating distribution skewness, central tendency, and spread.
- **Pie Chart (`eda_pie_chart.png`)**: Representing compositional shares and proportions.
- **Scatter Plot (`eda_scatterplot.png`)**: Displaying pairwise feature relationships and category clustering.
- **Correlation Heatmap (`eda_heatmap.png`)**: Revealing multi-feature linear associations via color-coded correlation coefficients.

---

## 🔍 EDA Workflow & Analytical Techniques

Every exploratory analysis in this repository follows a disciplined 5-stage lifecycle:

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  1. Inspection  │ ──> │   2. Cleaning   │ ──> │ 3. Transformation│ ──> │4. Visualization │ ──> │   5. Insights   │
│                 │     │                 │     │                 │     │                 │     │                 │
│ .head(), .shape │     │ .isna().sum()   │     │ Type casting    │     │ Histograms      │     │ Summary tables  │
│ .info(), dtypes │     │ Imputation      │     │ Feature creation│     │ Heatmaps        │     │ Business KPIs   │
│ .describe()     │     │ Deduplication   │     │ GroupBy / Aggs  │     │ Scatter plots   │     │ Actionable tips │
└─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘
```

1. **Structural Auditing**: Assessing dataframe dimensions (`.shape`), column names, and storage data types (`.dtypes`).
2. **Data Hygiene & Cleansing**: Detecting null values (`.isna().sum()`), handling duplicate rows (`.drop_duplicates()`), and treating anomalous outliers.
3. **Data Transformation & Aggregation**: Mutating new analytical fields, filtering target cohorts, and executing split-apply-combine aggregations (`.groupby()`).
4. **Visual Exploration**: Mapping distributions, pairwise correlations, and categorical breakdowns through graphical plots.
5. **Synthesis & KPI Reporting**: Formulating business insights and analytical findings.

---

## 🚀 How to Run the Code

### Prerequisites
Ensure Python 3.9+ is installed along with the core data science libraries:
```bash
pip install numpy pandas matplotlib seaborn jupyter
```

### Running NumPy & Pandas Scripts
Execute any script directly from the root repository:
```bash
# Run a NumPy script
python 01_NumPy/01_eda_intro.py
python 01_NumPy/08_sum_and_axis.py

# Run a Pandas script
python 02_Pandas_Basics/01_pandas_intro.py
```

### Launching Jupyter Notebooks
To interact with any of the analysis notebooks in `03_Data_Analysis_Tasks/`:
```bash
jupyter notebook
```
Navigate to any project folder (e.g., `03_Data_Analysis_Tasks/01_Employee_Analysis/`) and open the respective `.ipynb` file.
