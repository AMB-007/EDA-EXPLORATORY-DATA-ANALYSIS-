"""
===============================================================================
Program 17: Advanced 2D Matrix Slicing & Descending Axis Sorting
===============================================================================
This program demonstrates advanced 2D array operations:
1. Column-wise aggregations and sub-grid slicing
2. Sorting 2D matrices in descending row order using np.sort() and column flipping [:, ::-1]
3. Reversing matrix rows and columns simultaneously
===============================================================================
"""

import numpy as np

# Initializing a 3x3 matrix
arr = np.array([
    [30, 10, 20],
    [60, 40, 50],
    [90, 70, 80]
])

print("=== Base 3x3 Input Matrix ===")
print(arr)
print()

# -----------------------------------------------------------------------------
# STEP 1: Column Aggregation & Matrix Slicing Practice
# -----------------------------------------------------------------------------
print("=== Step 1: Aggregation & Slicing ===")
# Process 1a: Column-wise sum (axis=0)
print("Column-wise Sums (np.sum(arr, axis=0)):", np.sum(arr, axis=0))

# Process 1b: Extract first two columns (cols 0 and 1)
print("\nFirst Two Columns arr[:, 0:2]:\n", arr[:, 0:2])

# Process 1c: Extract first two rows (rows 0 and 1)
print("\nFirst Two Rows arr[0:2, :]:\n", arr[0:2, :])
print()

# -----------------------------------------------------------------------------
# STEP 2: Advanced 2D Descending Sorting & Matrix Reversals
# -----------------------------------------------------------------------------
print("=== Step 2: Descending Row Sorting & Reversals ===")

# Process 2a: Sort each row horizontally in DESCENDING order
# Explanation: np.sort(arr) sorts rows in ascending order, then [:, ::-1] reverses columns horizontally
print("Row-wise Descending Order (np.sort(arr)[:, ::-1]):\n", np.sort(arr)[:, ::-1])

# Process 2b: Reverse row order of sorted matrix and pick last column
print("\nReversed Row Order & Last Column (np.sort(arr)[::-1, -1]):\n", np.sort(arr)[::-1, -1])

# Process 2c: Reverse both row order and column order of sorted matrix
print("\nFully Reversed Matrix Rows & Cols (np.sort(arr)[::-1, ::-1]):\n", np.sort(arr)[::-1, ::-1])
