# Plotting 3D graph for multiple column using seaborn

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

# data
data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [6, 7, 8, 9, 10],
    'z': [11, 12, 13, 14, 15],
})

# Set the style of the plot
sns.set(style="darkgrid")

# Create the figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create the scatter plot
ax.scatter(data['x'], data['y'], data['z'])

# Set labels for each axis
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set the title
ax.set_title('3D Scatter Plot')

# Display the plot
plt.show()
