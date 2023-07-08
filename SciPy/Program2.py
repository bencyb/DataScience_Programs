import numpy as np
from scipy import linalg

# Define the coefficients of the linear equations
A = np.array([[2, 3], [4, 1]])
b = np.array([8, 10])

# Solve the linear equations
x, y = linalg.solve(A, b)

# Print the results
print("x =", x)
print("y =", y)

# Output::x = 2.2
# 		  y = 1.2
