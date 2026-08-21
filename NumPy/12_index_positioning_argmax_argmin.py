"""
===============================================================================
Program 12: Index Positioning (argsort, argmax, argmin)
===============================================================================
This program demonstrates retrieving index positions that would sort an array (argsort)
and finding index positions of maximum (argmax) and minimum (argmin) elements.
===============================================================================
"""

import numpy as np

# Sample 1D Array
a = np.array([20, 10, 30, 25, 40])
print("=== 1D Array ===")
print("Values:", a)
print()

# Process 1: Return index positions that would sort the array in descending order
print("=== Descending Sorted Indices (np.argsort(a)[::-1]) ===")
print(np.argsort(a)[::-1])
print()

# Process 2: Return index of largest element in 1D array
print("=== Index of Maximum Value (np.argmax(a)) ===")
print("Index:", np.argmax(a))  # Returns 4 (for value 40)
print()

# Process 3: Return index of smallest element in 1D array
print("=== Index of Minimum Value (np.argmin(a)) ===")
print("Index:", np.argmin(a))  # Returns 1 (for value 10)
print()

# Sample 2D Matrix
b = np.array([
    [3, 10, 11],
    [2,  5,  1],
    [6, 10,  4]
])

print("=== 2D Matrix B ===")
print(b)
print()

# Process 4: Return argmax on flattened 2D matrix
print("=== Overall argmax (flattened matrix) ===")
print("Index:", np.argmax(b))  # Returns 2 (for value 11)
print()

# Process 5: Return column-wise argmax (axis = 0)
print("=== Column-wise argmax (axis=0) ===")
print("Indices:", np.argmax(b, axis=0))  # Returns row indices containing max element for each column
