"""
===============================================================================
Program 04: Sequence Generation, Array Reshaping & Flattening
===============================================================================
This program demonstrates generating range sequences (np.arange), changing array
dimensions (reshape), and flattening multi-dimensional arrays into 1D (flatten).
===============================================================================
"""

import numpy as np

# Process 1: Sequence generation using np.arange
# Generates numbers from 1 to 8 in a 1D array
arr_seq = np.arange(1, 9)
print("=== Original Sequential 1D Array ===")
print("Array:", arr_seq)
print("Shape:", arr_seq.shape)
print()

# Process 2: Reshaping 1D array to 2D matrix (4 rows, 2 columns)
print("=== Reshaped to 4x2 Matrix ===")
reshaped_4x2 = arr_seq.reshape((4, 2))
print(reshaped_4x2)
print()

# Process 3: Reshaping 1D array to 2D matrix (2 rows, 4 columns)
print("=== Reshaped to 2x4 Matrix ===")
reshaped_2x4 = arr_seq.reshape((2, 4))
print(reshaped_2x4)
print("Dimension:", reshaped_2x4.ndim)
print()

# Process 4: Flattening multi-dimensional array back to 1D
print("=== Flattening Matrix back to 1D Array ===")
flattened_arr = reshaped_2x4.flatten()
print("Flattened Array:", flattened_arr)
print("Dimension:", flattened_arr.ndim)
