# Querying Series

import pandas as pd
s=pd.Series([x for x in range(1,11)])
print("s = ",s)

# Output::s =     0     1
				# 1     2
				# 2     3
				# 3     4
				# 4     5
				# 5     6
				# 6     7
				# 7     8
				# 8     9
				# 9    10
				# dtype: int64

s1=s.iloc[0]
print("s1 = ",s1)

# Output::s1 =  1

s2=s.iloc[5]
print("s2 = ",s2)

# Output::s2 =  6

s3=s.iat[0]
print("s3 = ",s3)

# Output::s3 =  1

s4=s.iat[0]
print("s4 = ",s4)

# Output::s4 =  1

s5=s[5:9]
print("s5 = ",s5)

# Output::s5 =  5    6
				# 6    7
				# 7    8
				# 8    9
				# dtype: int64

s6=s[-4:-1]
print("s6 = ",s6)

# Output::s6 =  6    7
			# 7    8
			# 8    9
			# dtype: int64

l=s.where(s%2==0)
print("l = ",l)

# Output::l =  0     NaN
			# 1     2.0
			# 2     NaN
			# 3     4.0
			# 4     NaN
			# 5     6.0
			# 6     NaN
			# 7     8.0
			# 8     NaN
			# 9    10.0
			# dtype: float64

l1=s.where(s%2==0,'Odd Number')
print("l1 = ",l1)

# Output::l1 =  0    Odd Number
				# 1             2
				# 2    Odd Number
				# 3             4
				# 4    Odd Number
				# 5             6
				# 6    Odd Number
				# 7             8
				# 8    Odd Number
				# 9            10
				# dtype: object


l2=s.where(s%2==0,s**2)
print("l2 = ",l2)

# Output::l2 =  0     1
		# 1     2
		# 2     9
		# 3     4
		# 4    25
		# 5     6
		# 6    49
		# 7     8
		# 8    81
		# 9    10
		# dtype: int64


l3=s.where(s%2==0,inplace=True)
print("l3 = ",l3)

# Output::l3 =  None

l4=s.fillna("Filled Data Value")
print("l4 = ",l4)

# Output::l4 =  0    Filled Data Value
				# 1                  2.0
				# 2    Filled Data Value
				# 3                  4.0
				# 4    Filled Data Value
				# 5                  6.0
				# 6    Filled Data Value
				# 7                  8.0
				# 8    Filled Data Value
				# 9                 10.0
				# dtype: object










