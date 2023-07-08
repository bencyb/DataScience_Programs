# Demonstrates data preprocessing using scikit-learn

from sklearn.preprocessing import StandardScaler
import numpy as np

# data
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

# Create a StandardScaler object
scaler = StandardScaler()

# Fit and transform the data
scaled_data = scaler.fit_transform(data)

# Output the transformed data
print("Original Data:")
print(data)

# Output::Original Data:
		# [[1 2 3]
		#  [4 5 6]
		#  [7 8 9]]

print("\nScaled Data:")
print(scaled_data)

# Output::Scaled Data:
		# [[-1.22474487 -1.22474487 -1.22474487]
		#  [ 0.          0.          0.        ]
		#  [ 1.22474487  1.22474487  1.22474487]]
