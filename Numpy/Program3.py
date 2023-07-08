import numpy as np

numpy_arr = np.array([x for x in range(1, 10)])
print("Numpy_arr =", numpy_arr)

# Output::Numpy_arr = [1 2 3 4 5 6 7 8 9]

numpy_arr = numpy_arr.reshape(3, 3)
print("Numpy_arr =", numpy_arr)

# # Output::Numpy_arr = [[1 2 3]
					  # [4 5 6]
					  # [7 8 9]]

numpy_arr = np.array([x for x in range(1, 13)])
print("Numpy_arr =", numpy_arr)

# # Output::Numpy_arr = [ 1  2  3  4  5  6  7  8  9 10 11 12]


numpy_arr = numpy_arr.reshape(3, 2, 2)
print("Numpy_arr =", numpy_arr)

# #Output::Numpy_arr = [[[ 1  2]
				 #  	[ 3  4]]
				 # 		[[ 5  6]
				 #  	[ 7  8]]
				 # 		[[ 9 10]
				 #  	[11 12]]]


numpy_arr = numpy_arr.reshape(2, 2, -1)
print("Numpy_arr =", numpy_arr)

# # Output::Numpy_arr = [[[ 1  2  3]
					 #  [ 4  5  6]]
					 # [[ 7  8  9]
					 #  [10 11 12]]]


numpy_arr = numpy_arr.reshape(3, 2, 2)
print("Numpy_arr =", numpy_arr)

# # Output::Numpy_arr = [[[ 1  2]
					 #  [ 3  4]]
					 # [[ 5  6]
					 #  [ 7  8]]
					 # [[ 9 10]
					 #  [11 12]]]


numpy_arr = numpy_arr.flatten()
print("Flattened Numpy_arr =", numpy_arr)

# # Output::Flattened Numpy_arr = [ 1  2  3  4  5  6  7  8  9 10 11 12]
