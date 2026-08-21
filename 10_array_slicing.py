"""
===============================================================================
Program 10: Array Slicing & Sub-grid Extraction
===============================================================================
This program demonstrates 2D array slicing to extract sub-matrices, specific rows,
specific columns, and reverse row ordering.
===============================================================================
"""

import numpy as np

# Base 5x4 matrix
array = np.arange(1, 21).reshape(5, 4)

print("=== Base 5x4 Matrix ===")
print(array)
print()

# Process 1: Extracting sub-grid (rows 1 to 3, columns 1 to 2)
# Syntax: array[row_start:row_stop, col_start:col_stop]
print("=== Sub-grid: array[1:4, 1:3] ===")
print(array[1:4, 1:3])
print()

# Process 2: Extracting sub-grid (rows 2 to 3, columns 1 to end)
print("=== Sub-grid: array[2:4, 1:] ===")
print(array[2:4, 1:])
print()

# Process 3: Extracting a single row (row index 2)
print("=== Single Row (Row Index 2) ===")
print(array[2, :])
print()

# Process 4: Extracting a single column (column index 1)
print("=== Single Column (Column Index 1) ===")
print(array[:, 1])
print()

# Process 5: Reversing row order using negative step slicing [::-1]
print("=== Reversing Row Order: array[::-1, :] ===")
print(array[::-1, :])
