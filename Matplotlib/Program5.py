# 3D visualization using matplotlib and pandas with external dataset.


import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the data from the CSV file
data = pd.read_csv('student.csv')

# Extract the required columns
names = data['name']
classes = data['class']
marks = data['mark']

# Convert categorical values to numerical labels
name_labels = pd.Categorical(names).codes
class_labels = pd.Categorical(classes).codes

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the data points
ax.scatter(name_labels, class_labels, marks, c='r', marker='o')

# Set labels and title
ax.set_xlabel('Name')
ax.set_ylabel('Class')
ax.set_zlabel('Mark')
ax.set_title('3D Visualization')

# Set tick labels
ax.set_xticklabels(names.unique())
ax.set_yticklabels(classes.unique())

# Show the plot
plt.show()
