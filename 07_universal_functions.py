"""
===============================================================================
Program 07: NumPy Universal Mathematical Functions (ufuncs)
===============================================================================
This program demonstrates built-in NumPy universal math functions:
np.add, np.subtract, np.multiply, np.divide, and np.sqrt.
===============================================================================
"""

import numpy as np

# Initializing sample arrays
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
b = np.array([[4, 3, 2, 1], [8, 7, 6, 5]])

print("Matrix A:\n", a)
print("\nMatrix B:\n", b)
print()

# Process 1: Explicit NumPy Addition Function (np.add)
print("=== np.add(a, b) ===")
print(np.add(a, b))

# Process 2: Explicit NumPy Subtraction Function (np.subtract)
print("\n=== np.subtract(a, b) ===")
print(np.subtract(a, b))

# Process 3: Explicit NumPy Multiplication Function (np.multiply)
print("\n=== np.multiply(a, b) ===")
print(np.multiply(a, b))

# Process 4: Explicit NumPy Division Function (np.divide)
print("\n=== np.divide(a, b) ===")
print(np.divide(a, b))

# Process 5: Element-wise Square Root Function (np.sqrt)
print("\n=== np.sqrt(a) ===")
print(np.sqrt(a))
