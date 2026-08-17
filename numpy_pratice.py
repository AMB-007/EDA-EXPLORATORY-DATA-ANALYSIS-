import numpy as np

arr_1 = np.array([1,2,3,4])
print(arr_1)
# [1 2 3 4] one dimensional array
print(arr_1.ndim)


# an array contains a single row of elements it can be termed as one dimensional array
# we can check the dimension using the attribute ndim
# eg : print(arr.ndim)

arr_2 = np.array([[1,2,3,4],[6,7,8,9]])
print(arr_2)
print(arr_2.ndim)
# an array contains more than one rows (rows and columns) like a table format
# # can be termed as 2 - dimensional array


arr_3 = np.array([[[1,2,3,4],[6,7,8,9]],
                  [[1,2,3,4],[6,7,8,9]]])
                  
print(arr_3)
print(arr_3.ndim)

# 3-dimensional array
# An array contains multiple 2- dimensional arrays


print(arr_1.shape)
print(arr_2.shape)
print(arr_3.shape)

# (4,) this tuple indicates that it is a one dimensional array with 4 elements
# (2, 4) indicates 2d array with 2 rows and 4 columns
# (2, 2, 4) indicates 3 2-d arrays each having 2 rows and 4 columns