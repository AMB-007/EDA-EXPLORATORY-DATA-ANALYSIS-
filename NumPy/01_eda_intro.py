"""
===============================================================================
Program 01: Detailed Introduction to Exploratory Data Analysis (EDA)
===============================================================================
Exploratory Data Analysis (EDA) is a critical preliminary step in any data science
or machine learning project. It involves analyzing datasets to summarize their 
main statistical characteristics, discover patterns, detect anomalies/outliers, 
and test underlying assumptions using summary statistics and graphical visualizations.

-------------------------------------------------------------------------------
THE 5 CORE STAGES OF THE EDA LIFECYCLE:
-------------------------------------------------------------------------------
1. Data Understanding & Inspection:
   - Inspect dataset shape (rows x columns), column names, and data types.
   - Differentiate between categorical (nominal, ordinal) and numerical (discrete, continuous) variables.

2. Data Quality Audit & Cleaning:
   - Identify missing values (NaNs/Nulls) and duplicate records.
   - Detect extreme outliers and anomalies that could skew data analysis.

3. Univariate Analysis:
   - Analyze each feature individually.
   - Numerical: Measures of central tendency (Mean, Median), dispersion (Std, Variance, IQR), and distribution shape (Skewness).
   - Categorical: Frequency distributions and value counts.

4. Bivariate & Multivariate Analysis:
   - Examine relationships between two or more features.
   - Calculate correlation matrices (Pearson/Spearman) and group statistics.

5. Data Preparation for Modeling:
   - Feature engineering, scaling, encoding categorical variables, and data transformation.

-------------------------------------------------------------------------------
THE CORE PYTHON DATA SCIENCE STACK FOR EDA:
-------------------------------------------------------------------------------
- NumPy      : High-performance N-dimensional array processing and mathematical computations.
- Pandas     : Tabular data handling (DataFrames/Series), data cleaning, and filtering.
- Matplotlib : Low-level, customizable plot generation (bar charts, scatter plots, line graphs).
- Seaborn    : High-level statistical visualization (heatmaps, box plots, pair plots, KDEs).
===============================================================================
"""

import numpy as np

# -----------------------------------------------------------------------------
# Process 1: Displaying EDA Lifecycle & Stack Summary
# -----------------------------------------------------------------------------
print("=" * 70)
print("              EXPLORATORY DATA ANALYSIS (EDA) OVERVIEW               ")
print("=" * 70)
print("Goal: Extract insights, detect anomalies, and prepare data for modeling.\n")

print("Primary Python Tools:")
print("  - NumPy      : Numerical calculation & matrix vectorization")
print("  - Pandas     : DataFrames, tabular data manipulation & cleaning")
print("  - Matplotlib : Foundation plotting library")
print("  - Seaborn    : Statistical visualizations & correlation heatmaps\n")


# -----------------------------------------------------------------------------
# Process 2: Simulating Dataset Structure using NumPy
# -----------------------------------------------------------------------------
# Creating a dummy numerical dataset (5 samples, 3 features: Age, Income, Score)
print("=== Process 2: Simulated Feature Matrix Inspection ===")
data = np.array([
    [25, 45000, 78],
    [30, 54000, 85],
    [35, 62000, 91],
    [22, 38000, 65],
    [40, 75000, 95]
])

print("Sample Feature Matrix (Rows = Observations, Cols = Features):\n", data)
print("Dataset Shape (Rows, Columns):", data.shape)  # 5 rows, 3 columns
print("Data Type:", data.dtype)
print()


# -----------------------------------------------------------------------------
# Process 3: Univariate Statistical Analysis (Numerical Features)
# -----------------------------------------------------------------------------
# Extracting feature columns: Column 0 = Age, Column 1 = Income, Column 2 = Score
print("=== Process 3: Univariate Summary Statistics ===")

ages = data[:, 0]
incomes = data[:, 1]
scores = data[:, 2]

print("Age    -> Mean: {:.1f} | Min: {} | Max: {} | Std Dev: {:.2f}".format(
    np.mean(ages), np.min(ages), np.max(ages), np.std(ages)
))

print("Income -> Mean: ${:.1f} | Min: ${} | Max: ${} | Std Dev: ${:.2f}".format(
    np.mean(incomes), np.min(incomes), np.max(incomes), np.std(incomes)
))

print("Score  -> Mean: {:.1f} | Min: {} | Max: {} | Std Dev: {:.2f}".format(
    np.mean(scores), np.min(scores), np.max(scores), np.std(scores)
))
print()


# -----------------------------------------------------------------------------
# Process 4: Bivariate Relationship (Correlation Concept)
# -----------------------------------------------------------------------------
# Checking how Income correlates with Score using NumPy corrcoef
print("=== Process 4: Bivariate Analysis Concept (Correlation) ===")
corr_matrix = np.corrcoef(incomes, scores)
print("Correlation Matrix between Income and Score:\n", corr_matrix)
print("Correlation Coefficient (Income vs Score): {:.4f}".format(corr_matrix[0, 1]))
print("Interpretation: Strong positive correlation between Income and Score.")
print("=" * 70)
