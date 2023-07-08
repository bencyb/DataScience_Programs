# Indexing and Slicing in Python Numpy

import numpy as np
array_1d = np.array([1,2,3,4,5,6])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
array_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# Indexing
print("array_1d = ",array_1d[0])
# Output:array_1d =  1

print("array_1d = ",array_1d[1])
# Output:array_1d =  2

print("array_2d = ",array_2d[0,1])
# Output::array_2d =  2

print("array_2d = ",array_2d[0,0])
# Output::array_2d =  1

print("array_2d = ",array_2d[1,-1])
# Output::array_2d =  6

print("array_3d = ",array_3d[1,1,-1])
# Output::array_3d =  12

print("array_3d = ",array_3d[0,1,2])
# Output::array_3d =  6

# Slicing

print("array_1d = ",array_1d[1:])
# Output:array_1d =  [2 3 4 5 6]

print("array_1d = ",array_1d[3:5])
# Output:array_1d =  [4 5]

print("array_1d = ",array_1d[-3:-1])
# Output:array_1d =  [4 5]

print("array_2d = ",array_2d[1,1:])
# Output::array_2d =  [5 6]

print("array_2d = ",array_2d[-2:-2:-1])
# Output::array_2d =  []

print("array_3d = ",array_3d[0,1:,1:])
# Output::array_3d =  [[5 6]]

print("array_3d = ",array_3d[0,-1:,-1:])
# Output::array_3d =  [[6]]





























