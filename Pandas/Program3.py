# Pandas Dataframes

import pandas as pd
df=pd.DataFrame()
print("Type = ",type(df))

# Output::Type =  <class 'pandas.core.frame.DataFrame'>

df=pd.read_csv('student.csv')
print(df.head())

# Output::    id        name  class  mark  gender
			# 0   1    John Deo   Four    75  female
			# 1   2    Max Ruin  Three    85    male
			# 2   3      Arnold  Three    55    male
			# 3   4  Krish Star   Four    60  female
			# 4   5   John Mike   Four    60  female

print(df.tail())

# Output::   id         name  class  mark  gender
			# 30  31  Marry Toeey   Four    88    male
			# 31  32    Binn Rott  Seven    90  female
			# 32  33    Kenn Rein    Six    96  female
			# 33  34     Gain Toe  Seven    69    male
			# 34  35   Rows Noump    Six    88  female

print(df.head(2))

# Output::	 id      name  class  mark  gender
			# 0   1  John Deo   Four    75  female
			# 1   2  Max Ruin  Three    85    male

print(df.tail(2))

# Output::id        name  class  mark  gender
		# 33  34    Gain Toe  Seven    69    male
		# 34  35  Rows Noump    Six    88  female

# Accessing a specific row using iloc
print(df.iloc[0])

# Output::
		# id               1
		# name      John Deo
		# class         Four
		# mark            75
		# gender      female
		# Name: 0, dtype: object

print(df.iloc[3])

# Output::id                 4
		# name      Krish Star
		# class           Four
		# mark              60
		# gender        female
		# Name: 3, dtype: object

#Accessing all values in the DataFrame
print(df.values)

# Output::[[1 'John Deo' 'Four' 75 'female']
		 # [2 'Max Ruin' 'Three' 85 'male']
		 # [3 'Arnold' 'Three' 55 'male']
		 # [4 'Krish Star' 'Four' 60 'female']
		 # [5 'John Mike' 'Four' 60 'female']
		 # [6 'Alex John' 'Four' 55 'male']
		 # [7 'My John Rob' 'Fifth' 78 'male']
		 # [8 'Asruid' 'Five' 85 'male']
		 # [9 'Tes Qry' 'Six' 78 'male']
		 # [10 'Big John' 'Four' 55 'female']
		 # [11 'Ronald' 'Six' 89 'female']
		 # [12 'Recky' 'Six' 94 'female']
		 # [13 'Kty' 'Seven' 88 'female']
		 # [14 'Bigy' 'Seven' 88 'female']
		 # [15 'Tade Row' 'Four' 88 'male']
		 # [16 'Gimmy' 'Four' 88 'male']
		 # [17 'Tumyu' 'Six' 54 'male']
		 # [18 'Honny' 'Five' 75 'male']
		 # [19 'Tinny' 'Nine' 18 'male']
		 # [20 'Jackly' 'Nine' 65 'female']
		 # [21 'Babby John' 'Four' 69 'female']
		 # [22 'Reggid' 'Seven' 55 'female']
		 # [23 'Herod' 'Eight' 79 'male']
		 # [24 'Tiddy Now' 'Seven' 78 'male']
		 # [25 'Giff Tow' 'Seven' 88 'male']
		 # [26 'Crelea' 'Seven' 79 'male']
		 # [27 'Big Nose' 'Three' 81 'female']
		 # [28 'Rojj Base' 'Seven' 86 'female']
		 # [29 'Tess Played' 'Seven' 55 'male']
		 # [30 'Reppy Red' 'Six' 79 'female']
		 # [31 'Marry Toeey' 'Four' 88 'male']
		 # [32 'Binn Rott' 'Seven' 90 'female']
		 # [33 'Kenn Rein' 'Six' 96 'female']
		 # [34 'Gain Toe' 'Seven' 69 'male']
		 # [35 'Rows Noump' 'Six' 88 'female']]