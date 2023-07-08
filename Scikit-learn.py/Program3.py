# Standardisation using Scikit-learn

import numpy as np
from sklearn.preprocessing import StandardScaler

# Input data
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

# Create a StandardScaler object
scaler = StandardScaler()

# Fit the scaler to the data and transform the data
scaled_data = scaler.fit_transform(data)

# Print the original data
print("Original data:\n", data)

# Output::Original data:
 # [[1 2 3]
 # [4 5 6]
 # [7 8 9]]

# Print the standardized data
print("\nStandardized data:\n", scaled_data)


# Output::Standardized data:
 # [[-1.22474487 -1.22474487 -1.22474487]
 # [ 0.          0.          0.        ]
 # [ 1.22474487  1.22474487  1.22474487]]
