"""
===============================================================================
Program 06: Scalar Operations & Vector Broadcasting
===============================================================================
This program demonstrates scalar operations where a single scalar value is
broadcasted and applied to all elements in a NumPy array.
===============================================================================
"""

import numpy as np

# Initializing sample matrix
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
c = np.array([[17, 18, 19, 20], [21, 22, 23, 24]])

print("Matrix A:\n", a)
print()

# Process 1: Scalar multiplication
# All elements in array are multiplied by 2 and returned in a new array
print("=== Scalar Multiplication (a * 2) ===")
print(a * 2)
print()

# Process 2: Scalar addition
# All elements in array are incremented by 2
print("=== Scalar Addition (a + 2) ===")
print(a + 2)
print()

# Process 3: Scalar multiplication on 2D Matrix C
print("=== Scalar Multiplication on Matrix C (c * 2) ===")
print(c * 2)
