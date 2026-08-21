"""
===============================================================================
Program 03: Special Matrix Creation Routines
===============================================================================
This program demonstrates generating pre-filled matrices: Zero matrix, Ones matrix,
Constant filled matrix, and Identity matrices.
===============================================================================
"""

import numpy as np

# Process 1: Creating a Zero Matrix (np.zeros)
# Matrix filled entirely with 0s
print("=== Zero Matrix (3x4) ===")
matrix_zero = np.zeros((3, 4), dtype=int)
print(matrix_zero)
print()

# Process 2: Creating a Matrix of Ones (np.ones)
# Matrix filled entirely with 1s
print("=== Ones Matrix (3x4) ===")
matrix_ones = np.ones((3, 4), dtype=int)
print(matrix_ones)
print()

# Process 3: Creating a Constant Matrix (np.full)
# Matrix filled entirely with a specific constant value (5)
print("=== Constant Full Matrix (3x4 filled with 5) ===")
matrix_full = np.full(shape=(3, 4), fill_value=5, dtype=int)
print(matrix_full)
print()

# Process 4: Creating Identity Matrices (np.identity & np.eye)
# Square matrix with 1s on main diagonal and 0s elsewhere
print("=== Identity Matrix (5x5 using np.identity) ===")
print(np.identity(5, dtype=int))
print()

print("=== Identity Matrix (3x3 using np.eye) ===")
print(np.eye(N=3, dtype=int))
