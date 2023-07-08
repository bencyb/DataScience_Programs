# Conditional Statement in Python using Numpy

import numpy as np
x=np.array([i for i in range(10)])
print("x = ",x)

# Output::x =  [0 1 2 3 4 5 6 7 8 9]

y=np.where(x%2==0,'Even Number','Odd Number')
print("y = ",y)

# Output::y =  ['Even Number' 'Odd Number' 'Even Number' 'Odd Number' 'Even Number'
             # 'Odd Number' 'Even Number' 'Odd Number' 'Even Number' 'Odd Number']


condlist = [x<5, x>5, x==5]
print("condlist = ", condlist)

# Output::condlist =  [array([ True,  True,  True,  True,  True, False, False, False, False,
                     # False]), array([False, False, False, False, False, False,  True,  True,  True,
                     # True]), array([False, False, False, False, False,  True, False, False, False,
                     # False])]

choicelist = [x**2, x**3, -1]  
print("choicelist = ", choicelist)

# Output::choicelist =  [array([ 0,  1,  4,  9, 16, 25, 36, 49, 64, 81]), 
					#   array([  0,   1,   8,  27,  64, 125, 216, 343, 512, 729], dtype=int32), -1]

ex = np.select(condlist, choicelist, default=x)
print("ex = ", ex)

# Output::ex =  [  0   1   4   9  16  -1 216 343 512 729]

