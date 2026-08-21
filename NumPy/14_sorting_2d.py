"""
===============================================================================
Program 14: 2D Matrix Sorting Across Axes
===============================================================================
This program demonstrates sorting 2D matrices along axis 0 (columns vertically)
and axis 1 (rows horizontally).
===============================================================================
"""

import numpy as np

# Sample 2D Matrix
a = np.array([
    [10, 20, 45],
    [12,  4, 15],
    [24,  8, 30],
    [10, 20, 45]
])

print("=== Original 2D Matrix ===")
print(a)
print()

# Process 1: Sort matrix column-wise (axis = 0)
# Sorts each column independently vertically from top to bottom
print("=== Sorted Column-wise (axis=0) ===")
print(np.sort(a, axis=0))
print()

# Process 2: Sort matrix row-wise (axis = 1)
# Sorts each row independently horizontally from left to right
print("=== Sorted Row-wise (axis=1) ===")
print(np.sort(a, axis=1))
