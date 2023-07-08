# Imputation of missing values using scikit-learn

import numpy as np
from sklearn.impute import SimpleImputer

# Create a sample dataset with missing values
X = np.array([[1, 2, np.nan],
              [3, np.nan, 4],
              [np.nan, 5, 6],
              [8, 9, 10]])

# Create an instance of SimpleImputer
imputer = SimpleImputer(strategy='mean')

# Fit the imputer on the dataset
imputer.fit(X)

# Transform the dataset by imputing missing values
X_imputed = imputer.transform(X)

# Print the original dataset
print("Original dataset:")
print(X)

# Output::Original dataset:
	# [[ 1.  2. nan]
	#  [ 3. nan  4.]
	#  [nan  5.  6.]
	#  [ 8.  9. 10.]]

# Print the imputed dataset
print("\nImputed dataset:")
print(X_imputed)

# Output::Imputed dataset:
	# [[ 1.          2.          6.66666667]
	#  [ 3.          5.33333333  4.        ]
	#  [ 4.          5.          6.        ]
	#  [ 8.          9.         10.        ]]
