"""
===============================================================================
Program 02: NumPy Array Types & Dimensionality
===============================================================================
This program demonstrates how to create 1D, 2D, and 3D arrays and inspect
array dimensions (.ndim), shapes (.shape), and data types (.dtype).
===============================================================================
"""

import numpy as np

# -----------------------------------------------------------------------------
# Process 1: Creating a 1-Dimensional Array (1D)
# -----------------------------------------------------------------------------
# An array with a single row of elements.
print("=== 1D Array ===")
arr_1d = np.array([1, 2, 3, 4])
print("Array:\n", arr_1d)
print("Dimension (.ndim):", arr_1d.ndim)  # Output: 1
print("Shape (.shape):", arr_1d.shape)    # Output: (4,)
print("Data Type (.dtype):", arr_1d.dtype)
print()

# -----------------------------------------------------------------------------
# Process 2: Creating a 2-Dimensional Array (2D)
# -----------------------------------------------------------------------------
# An array containing rows and columns (table format).
print("=== 2D Array ===")
arr_2d = np.array([
    [1, 2, 3, 4],
    [6, 7, 8, 9]
])
print("Array:\n", arr_2d)
print("Dimension (.ndim):", arr_2d.ndim)  # Output: 2
print("Shape (.shape):", arr_2d.shape)    # Output: (2, 4)
print()

# -----------------------------------------------------------------------------
# Process 3: Creating a 3-Dimensional Array (3D)
# -----------------------------------------------------------------------------
# An array containing multiple 2D matrices layered together.
print("=== 3D Array ===")
arr_3d = np.array([
    [[1, 2, 3, 4], [6, 7, 8, 9]],
    [[1, 2, 3, 4], [6, 7, 8, 9]]
])
print("Array:\n", arr_3d)
print("Dimension (.ndim):", arr_3d.ndim)  # Output: 3
print("Shape (.shape):", arr_3d.shape)    # Output: (2, 2, 4)
