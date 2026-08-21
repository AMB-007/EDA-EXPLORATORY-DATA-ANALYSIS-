"""
===============================================================================
Program 13: Conditional Searching & Filtering (np.where)
===============================================================================
This program demonstrates conditional searching using np.where:
1. Extracting matching indices based on a boolean condition.
2. Replacing elements conditionally (e.g., 'pass' if > 5, else 'fail').
===============================================================================
"""

import numpy as np

# Process 1: Conditional index search on a 1D array
# Syntax: np.where(condition)
arr = np.array([10, 13, 15, 20, 17])
print("=== 1D Condition Search (arr >= 15) ===")
print("Array:", arr)
matching_indices = np.where(arr >= 15)
print("Indices where element >= 15:", matching_indices[0])
print()

# Process 2: Conditional position search on a 2D matrix
b = np.array([
    [3, 10, 11],
    [2,  5,  1],
    [6, 10,  4]
])

print("=== 2D Matrix B ===")
print(b)
print()

print("=== Positions where b > 5 ===")
print("Row and Column Indices:", np.where(b > 5))
print()

# Process 3: Conditional element substitution
# Syntax: np.where(condition, value_if_true, value_if_false)
print("=== Conditional Replacement ('pass' if > 5 else 'fail') ===")
result = np.where(b > 5, "pass", "fail")
print(result)
