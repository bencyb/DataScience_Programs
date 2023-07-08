# Linear Regression

import numpy as np
from sklearn.linear_model import LinearRegression

# Input data
X = np.array([1, 2, 3, 4, 5]).reshape((-1, 1))
y = np.array([2, 4, 6, 8, 10])

# Create and fit the model
model = LinearRegression()
model.fit(X, y)

# Get the slope and intercept
slope = model.coef_[0]
intercept = model.intercept_

print("Input X:", X.flatten())

# Output::Input X: [1 2 3 4 5]

print("Input y:", y)

# Output::Input y: [ 2  4  6  8 10]

print("Slope:", slope)

# Output::Slope: 2.0

print("Intercept:", intercept)

# Output::Intercept: 0.0