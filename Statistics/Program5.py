# Normal Distribution

import numpy as np
import matplotlib.pyplot as plt

mu = 0     
sigma = 1  
size = 1000
data = np.random.normal(mu, sigma, size)
plt.hist(data, bins=30, density=True, alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Normal Distribution')
plt.show()


# Uniform Distribution

import numpy as np
import matplotlib.pyplot as plt
low = 0     
high = 10   
size = 1000
data = np.random.uniform(low, high, size)
plt.hist(data, bins=30, density=True, alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Uniform Distribution')
plt.show()


# Exponential Distribution

import numpy as np
import matplotlib.pyplot as plt
scale = 1.0  
size = 1000
data = np.random.exponential(scale, size)
plt.hist(data, bins=30, density=True, alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Exponential Distribution')
plt.show()



