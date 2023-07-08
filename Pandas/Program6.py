# Ploating with Pandas 

import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame (replace with your actual data)
data = {'price': [10, 20, 30, 40, 50],
        'place': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)

# Line plot
df.plot()
plt.show()

#Line plot with legend
df['price'].plot(legend=True)
plt.show()

#Scatter plot
df.plot(x='price', y='place', kind='scatter', legend=True)
plt.show()

#Line plot with title and figure size
df.plot(title='Sample Plot', figsize=(15, 10))
plt.show()

#Box plot
df['price'].plot(kind='box', title='Box Plot')
plt.show()

#Histogram
df['price'].plot(kind='hist', title='Histogram')
plt.show()
