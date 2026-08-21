"""
===============================================================================
Program 09: Statistical Metrics & Summaries
===============================================================================
This program demonstrates computing key statistical metrics: mean, min, max,
and standard deviation across arrays and specified axes.
===============================================================================
"""

import numpy as np

# Sample Matrix (2 rows x 4 columns)
a = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

print("Input Matrix A:\n", a)
print()

# Process 1: Calculating Mean (Average) value
print("=== Mean Value ===")
print("Overall Mean:", np.mean(a))
print("Column-wise Mean (axis=0):", np.mean(a, axis=0))
print("Row-wise Mean (axis=1):", np.mean(a, axis=1))
print()

# Process 2: Finding Minimum and Maximum elements
print("=== Min and Max Values ===")
print("Minimum element:", np.min(a))
print("Maximum element:", np.max(a))
print()

# Process 3: Calculating Standard Deviation
print("=== Standard Deviation ===")
print("Standard Deviation:", np.std(a))
