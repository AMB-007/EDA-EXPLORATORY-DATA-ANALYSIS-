"""
===============================================================================
Program 08: Array Sum Operations Across Axes
===============================================================================
This program demonstrates overall sum (axis=None), column-wise sum (axis=0),
and row-wise sum (axis=1) across multi-dimensional arrays.
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

# Process 1: Total Array Sum (axis = None)
# Adds all elements in the array and returns a single sum
print("=== Overall Sum (axis=None) ===")
print("Sum of all elements:", np.sum(a, axis=None))  # Output: 36
print()

# Process 2: Column-wise Sum (axis = 0)
# Sums elements down columns across rows
print("=== Column-wise Sum (axis=0) ===")
print("Column-wise sums:", np.sum(a, axis=0))  # Output: [ 6  8 10 12]
print()

# Process 3: Row-wise Sum (axis = 1)
# Sums elements across rows
print("=== Row-wise Sum (axis=1) ===")
print("Row-wise sums:", np.sum(a, axis=1))  # Output: [10 26]
