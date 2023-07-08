# Scikit-learn to predict sales figures for different channels using linear regression

import numpy as np
from sklearn.linear_model import LinearRegression

# Channel 1 data
X1 = np.array([[10, 8], [8, 6], [9, 7], [7, 5]])
y1 = np.array([200, 150, 180, 160])

# Channel 2 data
X2 = np.array([[5, 4], [4, 3], [6, 5], [3, 2]])
y2 = np.array([100, 80, 90, 70])

# Create a linear regression model
model = LinearRegression()

# Fit the model for Channel 1
model.fit(X1, y1)

# Predict sales figures for Channel 1
X1_test = np.array([[12, 9], [9, 7]])
predicted_sales1 = model.predict(X1_test)
print("Predicted sales figures for Channel 1:", predicted_sales1)

# Output::Predicted sales figures for Channel 1: [217.5 180. ]

# Fit the model for Channel 2
model.fit(X2, y2)

# Predict sales figures for Channel 2
X2_test = np.array([[5, 4], [6, 5]])
predicted_sales2 = model.predict(X2_test)
print("Predicted sales figures for Channel 2:", predicted_sales2)

# Output::Predicted sales figures for Channel 2: [89. 97.]
