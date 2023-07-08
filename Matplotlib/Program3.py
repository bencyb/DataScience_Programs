# 3D graph visualization using matplotlib

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate data points
t = np.linspace(0, 2 * np.pi, 100)
x = np.sin(t)
y = np.cos(t)
z = t

# Create a figure and an Axes3D object
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot a 3D line
ax.plot(x, y, z, label='3D Line')

# Add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Line Plot')

# Add a legend
ax.legend()

# Show the 3D plot
plt.show()
