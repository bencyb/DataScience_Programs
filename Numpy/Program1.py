#Import library into python program

import math
a=16
print("Square root of a = ",math.sqrt(a))

# Output::Square root of a =  4.0

# Import specified method in the math module 

from math import sqrt,sin
b=12
c=32
print("Square root of b = ",sqrt(b))
print("Sin of c =  ",sin(c))

# Output::Square root of b =  3.4641016151377544
		# Sin of c =   0.5514266812416906


# Create a one-dimensional array with aliases as np and perform the following methods
	# 1)np.zeros()
	# 2)np.ones()
	# 3)np.empty()
	# 4)np.arange()
	# 5)np.reshape()


import numpy as np
first_numpy_array=np.array([1,2,3,4])
print("First_numpy_array = ",first_numpy_array)

# Output::First_numpy_array =  [1 2 3 4]

array_with_zeros=np.zeros((3,3))
print("Array_with_zeros = ",array_with_zeros)

# Output::Array_with_zeros =  [[0. 0. 0.]
							# [0. 0. 0.]
						    # [0. 0. 0.]]

array_with_ones=np.ones((2,3))
print("Array_with_ones = ",array_with_ones)

# Output::Array_with_ones =  [[1. 1. 1.]
 						#   [1. 1. 1.]]

array_with_empty=np.empty((2,3))
print("Array_with_empty = ",array_with_empty)

# Output::Array_with_empty =  [[1. 1. 1.]
 							# [1. 1. 1.]]

np_arange=np.arange(12)
print("Np_arange = ",np_arange)

# Output::Np_arange =  [ 0  1  2  3  4  5  6  7  8  9 10 11]

np_arange = np.arange(1, 13)
np_reshape = np_arange.reshape(3, 4)
print("Np_reshaped = ", np_reshape)

# Output::Np_reshaped =  [[ 1  2  3  4]
					 #   [ 5  6  7  8]
					 #   [ 9 10 11 12]]

np_linespace=np.linspace(1,6,5)
print("Np_linespace = ",np_linespace)

# Output::Np_linespace =  [1.   2.25 3.5  4.75 6.  ]

one_d_array = np.arange(15)
print("One_D_Array = ",one_d_array)

# Output::One_D_Array =  [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

two_d_array = one_d_array.reshape(3,5)
print("Two_D_Array = ",two_d_array)

# Output::Two_D_Array =  [[ 0  1  2  3  4]
					    # [ 5  6  7  8  9]
					    # [10 11 12 13 14]]

three_d_array=np.arange(27).reshape(3,3,3)
print("Three_d_array = ",three_d_array)

# Output::Three_d_array =  [[[ 0  1  2]
						 #  [ 3  4  5]
						 #  [ 6  7  8]]

						 # [[ 9 10 11]
						 #  [12 13 14]
						 #  [15 16 17]]

						 # [[18 19 20]
						 #  [21 22 23]
						 #  [24 25 26]]]




