"""
===============================================================================
Program 15: Comprehensive 2D Matrix Operations & Task Practice
===============================================================================
This program demonstrates a comprehensive set of operations on a 4x4 matrix:
1. Matrix properties & attributes (ndim, shape, size, dtype)
2. Element indexing and sub-grid slicing
3. Overall and axis-wise aggregations (sum, min, max, mean)
4. Index positioning (argmax, argmin overall and along axes)
5. 2D Row sorting and argsort indexing
===============================================================================
"""

import numpy as np

# Initializing a 4x4 matrix
arr = np.array([
    [10, 25, 30, 45],
    [15, 20, 35, 40],
    [50, 60, 55, 70],
    [80, 75, 90, 65]
])

print("=== Base 4x4 Input Matrix ===")
print(arr)
print()

# -----------------------------------------------------------------------------
# STEP 1: Matrix Properties & Attribute Inspection
# -----------------------------------------------------------------------------
print("=== Step 1: Matrix Attributes ===")
# Process 1a: Check number of dimensions
print("Dimensions (.ndim):", arr.ndim)  # Output: 2

# Process 1b: Check shape (rows, columns)
print("Shape (.shape):", arr.shape)    # Output: (4, 4)

# Process 1c: Check total number of elements
print("Total Size (.size):", arr.size)  # Output: 16

# Process 1d: Check element data type
print("Data Type (.dtype):", arr.dtype)
print()

# -----------------------------------------------------------------------------
# STEP 2: Indexing & Sub-grid Slicing
# -----------------------------------------------------------------------------
print("=== Step 2: Indexing & Slicing ===")
# Process 2a: Single element indexing (row index 1, column index 2)
print("Element at row 1, col 2 arr[1, 2]:", arr[1, 2])

# Process 2b: Extract specific entire rows
print("Row 0 arr[0]:", arr[0])
print("Row 3 arr[3]:", arr[3])

# Process 2c: Extract a specific column (column index 0)
print("Column 0 arr[:, 0]:", arr[:, 0])

# Process 2d: Sub-grid slicing (rows 0 to 1, columns 1 to 2)
print("\nSub-grid Slicing arr[0:2, 1:3]:\n", arr[0:2, 1:3])
print()

# -----------------------------------------------------------------------------
# STEP 3: Aggregations & Statistical Calculations
# -----------------------------------------------------------------------------
print("=== Step 3: Aggregation Operations ===")
# Process 3a: Overall matrix sum, max, min, mean
print("Overall Sum:", np.sum(arr))
print("Maximum Value:", np.max(arr))
print("Minimum Value:", np.min(arr))
print("Mean Value:", np.mean(arr))

# Process 3b: Row-wise sum (axis=1) and Column-wise sum (axis=0)
print("Row-wise Sums (axis=1):", np.sum(arr, axis=1))
print("Column-wise Sums (axis=0):", np.sum(arr, axis=0))
print()

# -----------------------------------------------------------------------------
# STEP 4: Argmax & Argmin Index Positioning
# -----------------------------------------------------------------------------
print("=== Step 4: Index Positioning (argmax & argmin) ===")
# Process 4a: Flattened matrix max & min indices
print("Overall argmax (flattened index of max value 90):", np.argmax(arr))
print("Overall argmin (flattened index of min value 10):", np.argmin(arr))

# Process 4b: Row-wise argmax (axis=1) and Column-wise argmin (axis=0)
print("Row-wise argmax (axis=1 - col index of max per row):", np.argmax(arr, axis=1))
print("Column-wise argmin (axis=0 - row index of min per col):", np.argmin(arr, axis=0))
print()

# -----------------------------------------------------------------------------
# STEP 5: Row-wise Sorting & Argsort Indexing
# -----------------------------------------------------------------------------
print("=== Step 5: Sorting & Argsort ===")
# Process 5a: Sort matrix rows horizontally (axis=1)
print("Sorted Row-wise (np.sort(arr, axis=1)):\n", np.sort(arr, axis=1))

# Process 5b: Indices that would sort each row horizontally (axis=1)
print("\nRow-wise Argsort Indices (np.argsort(arr, axis=1)):\n", np.argsort(arr, axis=1))
