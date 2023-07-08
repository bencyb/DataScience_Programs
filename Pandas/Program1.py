# Panda Series

import pandas as pd

# Series from a list
l = list(range(5))
s = pd.Series(l)
print("s = ",s)

# Output::s =  0    0
			# 1    1
			# 2    2
			# 3    3
			# 4    4
			# dtype: int64

# Series with specified index
q = pd.Series(1, index=['a', 'b', 'c', 'd'])
print("\nq = ",q)

# Output::q =  a    1
		# b    1
		# c    1
		# d    1
		# dtype: int64



# Series from a dictionary
r = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
r1 = pd.Series(r)
print("\nr1 = ",r1)

# Output::r1 =  a    1
				# b    2
				# c    3
				# d    4
				# dtype: int64

# Series with specified index from a dictionary
s1 = pd.Series(r, index=['a', 'b'])
print("\ns1 = ",s1)

# Output::s1 =  a    1
				# b    2
				# dtype: int64

s2 = pd.Series(r, index=['a', 'b', 'c', 'd'])
print("\ns2 = ",s2)

# Output::s2 =  a    1
				# b    2
				# c    3
				# d    4
				# dtype: int64