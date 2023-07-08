# Pandas Panel

import pandas as pd

df=pd.read_csv('house_price.csv',parse_dates=True)
print(df.head())

# Output::Id  MSSubClass MSZoning  ...  YrSold  SaleType SaleCondition
		# 0  1461          20       RH  ...    2010        WD        Normal
		# 1  1462          20       RL  ...    2010        WD        Normal
		# 2  1463          60       RL  ...    2010        WD        Normal
		# 3  1464          60       RL  ...    2010        WD        Normal
		# 4  1465         120       RL  ...    2010        WD        Normal

		# [5 rows x 80 columns]

df.set_index(['Street', 'LotArea'], inplace=True)
print(df.index)

# Output::MultiIndex([('Pave', 11622),
           #  ('Pave', 14267),
           #  ('Pave', 13830),
           #  ('Pave',  9978),
           #  ('Pave',  5005),
           #  ('Pave', 10000),
           #  ('Pave',  7980),
           #  ('Pave',  8402),
           #  ('Pave', 10176),
           #  ('Pave',  8400),
           #  ...
           #  ('Pave',  1470),
           #  ('Pave',  1484),
           #  ('Pave', 13384),
           #  ('Pave',  1533),
           #  ('Pave',  1526),
           #  ('Pave',  1936),
           #  ('Pave',  1894),
           #  ('Pave', 20000),
           #  ('Pave', 10441),
           #  ('Pave',  9627)],
           # names=['Street', 'LotArea'], length=1459)


print(df.loc['Pave'])

# Output::Id  MSSubClass MSZoning  ...  YrSold SaleType SaleCondition LotArea                             ...                               
	# 11622    1461          20       RH  ...    2010       WD        Normal
	# 14267    1462          20       RL  ...    2010       WD        Normal
	# 13830    1463          60       RL  ...    2010       WD        Normal
	# 9978     1464          60       RL  ...    2010       WD        Normal
	# 5005     1465         120       RL  ...    2010       WD        Normal
	# ...       ...         ...      ...  ...     ...      ...           ...
	# 1936     2915         160       RM  ...    2006       WD        Normal
	# 1894     2916         160       RM  ...    2006       WD       Abnorml
	# 20000    2917          20       RL  ...    2006       WD       Abnorml
	# 10441    2918          85       RL  ...    2006       WD        Normal
	# 9627     2919          60       RL  ...    2006       WD        Normal

	# [1453 rows x 78 columns]







