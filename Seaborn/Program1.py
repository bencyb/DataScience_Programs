# Using Seaborn to plot graph

import seaborn as sns
import matplotlib.pyplot as plt

# data
years = [2015, 2016, 2017, 2018, 2019, 2020, 2021]
data = [5, 10, 8, 12, 15, 11, 9]

# Set the style of the plot
sns.set(style="darkgrid")

# Create the line plot
sns.lineplot(x=years, y=data)

# Set the title and labels
plt.title("Data Trend Over Time")
plt.xlabel("Year")
plt.ylabel("Data Value")

# Display the plot
plt.show()
