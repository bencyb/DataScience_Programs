# Common Mathematical and statistical function in Numpy

import numpy as np
arr=np.array([[4,3,2],[10,1,0],[5,0,24]])
print("Array = ",arr)

# Output::Array =  [[ 4  3  2]
				 # [10  1  0]
				 # [ 5  0 24]]

a=np.amin(arr)
print("Minimum = ",a)

# Output::Minimum =  0

b=np.amin(arr,axis=0)
print("Minimum = ",b)

# Output::Minimum =  [4 0 0]

c=np.amin(arr,axis=1)
print("Minimum = ",c)

# Output::Minimum =  [2 0 0]

d=np.max(arr)
print("Maximum = ",d)

# Output::Maximum =  24

e=np.amax(arr,axis=0)
print("Maximum = ",e)

# Output::Maximum =  [10  3 24] 

f=np.amax(arr,axis=1)
print("Maximum = ",f)

# Output::Maximum =  [ 4 10 24]

g=np.median(arr)
print("Median = ",g)

# Output::Median =  3.0

h=np.mean(arr)
print("Mean = ",h)

# Output::Mean =  5.444444444444445

i=np.std(arr)
print("Standard Deviation = ",i)

# Output::Standard Deviation =  7.181938938307694

j=np.var(arr)
print("Variance = ",j)

# Output::Variance =  51.580246913580254

k=np.percentile(arr,50)
print("Percentile = ",k)

# Output::Percentile =  3.0

deg = np.array([0, 30, 45, 60, 90])
rad = np.deg2rad(deg)

sin_values = np.sin(rad)
print("sin_values = ",sin_values)

# Output::sin_values =  [0.         0.5        0.70710678 0.8660254  1.        ]

cos_values = np.cos(rad)
print("cos_values = ",cos_values)

# Output::cos_values =  [1.00000000e+00 8.66025404e-01 7.07106781e-01 5.00000000e-01
				      # 6.12323400e-17]

tan_values = np.tan(rad)
print("tan_values = ",tan_values)

# Output::tan_values =  [0.00000000e+00 5.77350269e-01 1.00000000e+00 1.73205081e+00
 					#   1.63312394e+16]


t=np.floor(arr)
print("Floor Value = ",t)

# Output::Floor Value =  [[ 4.  3.  2.]
					 #   [10.  1.  0.]
					 #   [ 5.  0. 24.]]

m=np.ceil(arr)
print("Ceil Value = ",m)

# Output::Ceil Value =     [[ 4.  3.  2.]
						 # [10.  1.  0.]
						 # [ 5.  0. 24.]]





