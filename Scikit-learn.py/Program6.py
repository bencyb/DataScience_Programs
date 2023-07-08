# One hot encoding using scikit-learn

from sklearn.preprocessing import OneHotEncoder
import numpy as np

# categorical data
categories = np.array(['A', 'B', 'C', 'A', 'B']).reshape(-1, 1)

# Create an instance of the OneHotEncoder class
encoder = OneHotEncoder()

# Fit the encoder to the categorical data
encoder.fit(categories)

# Perform one-hot encoding
one_hot_encoded = encoder.transform(categories)

# Convert the encoded data to an array
one_hot_array = one_hot_encoded.toarray()

# Print the encoded array
print(one_hot_array)

# Output::[[1. 0. 0.]
		 # [0. 1. 0.]
		 # [0. 0. 1.]
		 # [1. 0. 0.]
		 # [0. 1. 0.]]
