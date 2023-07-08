# Arithemetic Operations in Python Numpy

import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=np.array([3,4,5])
print("a = ",a)

# Output::a =  [[1 2 3]
		  #      [4 5 6]]

print("b = ",b)

# Output::b =  [3 4 5]

c=np.add(a,b)
print("Add = ",c)

# Output::Add =  [[ 4  6  8]
 #               [ 7  9 11]]


d=np.subtract(b,a)
print("Subtract = ",d)

# Output::Subtract =  [[ 2  2  2]
 					# [-1 -1 -1]]

e=np.multiply(a,b)
print("Product = ",e)

# Output::Product =  [[ 3  8 15]
					# [12 20 30]]


f=np.divide(a,b)
print("Division = ",f)

# Output::Division =  [[0.33333333 0.5        0.6       ]
 					# [1.33333333 1.25       1.2       ]]

g=np.power(a,2)
print("Power of a = ",g)

# Output::Power of a =  [[ 1  4  9]
 					#   [16 25 36]]

h=np.power(a,b)
print("Power of a,b = ",h)

# Output::Power of a,b =  [[   1   16  243]
 						# [  64  625 7776]]
