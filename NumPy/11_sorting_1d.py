"""
===============================================================================
Program 11: 1D Array Sorting (Ascending & Descending)
===============================================================================
This program demonstrates sorting 1D arrays in ascending order using np.sort()
and in descending order using step slicing [::-1].
===============================================================================
"""

import numpy as np

# Sample 1D Array
a = np.array([5, 3, 6, 1, 2, 10])

print("=== Original 1D Array ===")
print(a)
print()

# Process 1: Sort array in ascending order using np.sort()
print("=== Sorted in Ascending Order ===")
sorted_asc = np.sort(a)
print(sorted_asc)  # [ 1  2  3  5  6 10]
print()

# Process 2: Sort array in descending order using step slicing [::-1]
print("=== Sorted in Descending Order ===")
sorted_desc = np.sort(a)[::-1]
print(sorted_desc)  # [10  6  5  3  2  1]
