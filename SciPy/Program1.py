import numpy as np
from scipy import optimize

# Define the function to be minimized
def rosenbrock(x):
    return 100 * (x[1] - x[0]**2)**2 + (1 - x[0])**2

# Minimize the function using the Nelder-Mead method
result = optimize.minimize(rosenbrock, [0, 0], method='Nelder-Mead')

# Print the optimization result
print("Optimization Result:")
print(result)
print()

# Output::Optimization Result:
 # final_simplex: (array([[1.00000439, 1.00001064],
 #       [0.99996163, 0.99992454],
 #       [1.00002803, 1.00005254]]), array([3.68617692e-10, 1.63627702e-09, 2.02249112e-09]))
 #           fun: 3.6861769151759075e-10
 #       message: 'Optimization terminated successfully.'
 #          nfev: 146
 #           nit: 79
 #        status: 0
 #       success: True
 #             x: array([1.00000439, 1.00001064])

# Find the roots of a polynomial equation
coefficients = [1, -6, 11, -6]
roots = np.roots(coefficients)

# Print the roots
print("Roots of the Polynomial Equation:")
print(roots)
print()

# Output::Roots of the Polynomial Equation:
#           [3. 2. 1.]

# Solve a system of linear equations
a = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
solution = np.linalg.solve(a, b)

# Print the solution
print("Solution of the Linear System:")
print(solution)

# Output::Solution of the Linear System:
#           [2. 3.]
