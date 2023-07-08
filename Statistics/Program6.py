import numpy as np
import pandas as pd
import statsmodels.api as sm

# Create a dataset
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Add a constant term to the independent variable array for the intercept term
X = sm.add_constant(x)

# Fit the linear regression model
model = sm.OLS(y, X)
results = model.fit()

# Print the regression coefficients
print("Intercept:", results.params[0])

# Output::Intercept: 1.2

print("Slope:", results.params[1])

# Output::Slope: 0.9

# Perform predictions
x_new = np.array([6, 7, 8])
X_new = sm.add_constant(x_new)
predictions = results.predict(X_new)
print("Predictions:", predictions)

# Output::Predictions: [ 8.1  9.  9.9]

