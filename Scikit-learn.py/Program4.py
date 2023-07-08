# Normalization using scikit-learn 

from sklearn.preprocessing import MinMaxScaler
import numpy as np

# data
data = np.array([[2, 4, 6],
                 [1, 3, 5],
                 [7, 9, 11]])

# Create a MinMaxScaler object
scaler = MinMaxScaler()

# Fit the scaler to the data and transform it
normalized_data = scaler.fit_transform(data)

print("Original Data:")
print(data)

# Output::Original Data:
		# [[ 2  4  6]
		#  [ 1  3  5]
		#  [ 7  9 11]]

print("\nNormalized Data:")
print(normalized_data)

# Output::Normalized Data:
		# [[0.16666667 0.16666667 0.16666667]
		#  [0.         0.         0.        ]
		#  [1.         1.         1.        ]]
