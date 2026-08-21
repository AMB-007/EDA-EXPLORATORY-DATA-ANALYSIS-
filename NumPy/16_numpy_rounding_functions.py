"""
===============================================================================
Program 16: NumPy Rounding & Floating-Point Functions
===============================================================================
This program demonstrates how to round floating-point numbers in NumPy arrays
using np.round(), np.floor(), and np.ceil().
===============================================================================
"""

import numpy as np

# Sample floating-point array
arr = np.array([1.67, 2.5, 3.75, 4.65])

print("=== Base Floating-Point Array ===")
print(arr)
print()

# -----------------------------------------------------------------------------
# Process 1: Rounding to Specific Decimal Places (np.round)
# -----------------------------------------------------------------------------
# Rounds each element to the specified number of decimal places (decimals=1)
print("=== Round to 1 Decimal Place (np.round(arr, decimals=1)) ===")
print(np.round(arr, decimals=1))  # Output: [1.7 2.5 3.8 4.7]
print()

# -----------------------------------------------------------------------------
# Process 2: Lower Integer Bound (np.floor)
# -----------------------------------------------------------------------------
# Floors each decimal number down to the largest integer less than or equal to the value
print("=== Floor Values (np.floor(arr)) ===")
print(np.floor(arr))  # Output: [1. 2. 3. 4.]
print()

# -----------------------------------------------------------------------------
# Process 3: Upper Integer Bound (np.ceil)
# -----------------------------------------------------------------------------
# Ceils each decimal number up to the smallest integer greater than or equal to the value
print("=== Ceiling Values (np.ceil(arr)) ===")
print(np.ceil(arr))   # Output: [2. 3. 4. 5.]
