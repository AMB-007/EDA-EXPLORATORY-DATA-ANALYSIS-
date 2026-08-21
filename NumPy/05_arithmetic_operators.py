"""
===============================================================================
Program 05: Element-wise Arithmetic Operators
===============================================================================
This program demonstrates basic arithmetic operations between two NumPy arrays
using element-by-element operators (+, -, *, /, %).
===============================================================================
"""

import numpy as np

# Initializing sample arrays (2x4)
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
b = np.array([[4, 3, 2, 1], [8, 7, 6, 5]])

print("Matrix A:\n", a)
print("\nMatrix B:\n", b)
print()

# Process 1: Element-wise addition
print("=== Addition (a + b) ===")
print(a + b)

# Process 2: Element-wise subtraction
print("\n=== Subtraction (a - b) ===")
print(a - b)

# Process 3: Element-wise multiplication
print("\n=== Multiplication (a * b) ===")
print(a * b)

# Process 4: Element-wise division
print("\n=== Division (a / b) ===")
print(a / b)

# Process 5: Element-wise modulus (remainder)
print("\n=== Modulus / Remainder (a % 2) ===")
print(a % 2)
