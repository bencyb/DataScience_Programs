# Matrix Addition

import numpy as np
def matrix_addition(A, B):
    return A + B
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = matrix_addition(A, B)
print("Matrix C (A + B):\n", C)

# Output::Matrix C (A + B):
		 # [[ 6  8]
		 # [10 12]]


# Matrix Multiplication

import numpy as np
def matrix_multiplication(A, B):
    return np.dot(A, B)
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = matrix_multiplication(A, B)
print("Matrix C (A * B):\n", C)

# Output::Matrix C (A * B):
		 # [[19 22]
		 # [43 50]]


# Transpose of a Matrix 

import numpy as np
def matrix_transpose(A):
    return np.transpose(A)
A = np.array([[1, 2, 3], [4, 5, 6]])
A_transpose = matrix_transpose(A)
print("Transpose of Matrix A:\n", A_transpose)

# Output::Transpose of Matrix A:
		 # [[1 4]
		 # [2 5]
		 # [3 6]]


#Inverse of a Matrix

import numpy as np
def matrix_inverse(A):
    return np.linalg.inv(A)
A = np.array([[1, 2], [3, 4]])
A_inv = matrix_inverse(A)
print("Inverse of Matrix A:\n", A_inv)


# Output::Inverse of Matrix A:
		 # [[-2.   1. ]
		 # [ 1.5 -0.5]]


# Rank of a Matrix

import numpy as np
def matrix_rank(matrix):
    return np.linalg.matrix_rank(matrix)
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
rank = matrix_rank(A)
print("Rank of Matrix A:", rank)

# Output::Rank of Matrix A: 2


# Identity Matrix

import numpy as np
def create_identity_matrix(n):
    return np.eye(n)
identity_matrix = create_identity_matrix(3)
print("Identity Matrix:\n", identity_matrix)

# Output::Identity Matrix:
		 # [[1. 0. 0.]
		 # [0. 1. 0.]
		 # [0. 0. 1.]]



