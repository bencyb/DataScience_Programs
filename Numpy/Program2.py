# Numpy Array -Shape and Dimensions

import numpy as np

# One-dimensional array
np_array_1d = np.array([1, 2, 3, 4])
print("One-dimensional array:")
print(np_array_1d)
print("Shape:", np_array_1d.shape)
print("Number of dimensions:", np_array_1d.ndim)

# Output::One-dimensional array:
								# [1 2 3 4]
								# Shape: (4,)
								# Number of dimensions: 1


# Two-dimensional array
np_array_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 9, 0], [1, 2, 3, 5]])
print("Two-dimensional array:")
print(np_array_2d)
print("Shape:", np_array_2d.shape)
print("Number of dimensions:", np_array_2d.ndim)

# Output::Two-dimensional array:
							# [[1 2 3 4]
							#  [5 6 7 8]
							#  [9 8 9 0]
							#  [1 2 3 5]]
							# Shape: (4, 4)
							# Number of dimensions: 2

# Three-dimensional array
np_array_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("Three-dimensional array:")
print(np_array_3d)
print("Shape:", np_array_3d.shape)
print("Number of dimensions:", np_array_3d.ndim)


# Output::Three-dimensional array:
							# [[[ 1  2  3]
							#   [ 4  5  6]]

							#  [[ 7  8  9]
							#   [10 11 12]]]
							# Shape: (2, 2, 3)
							# Number of dimensions: 3
