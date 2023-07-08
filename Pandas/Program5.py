# Plotting with Pandas

import pandas as pd
df=pd.read_csv("student.csv")
print(df.head())

# Output::   id        name  class  mark  gender
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


print(df.columns)

# Output::Index(['id', 'name', 'class', 'mark', 'gender'], dtype='object')

import matplotlib.pyplot as plt
df.plot()
plt.show()




