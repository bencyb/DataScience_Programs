# Visualise Pie Chart

import matplotlib.pyplot as plt

causes = ['Heart disease', 'Stroke', 'Tuberculosis', 'Malaria', 'Influenza', 'Cancer', 'Diabetes']
percentages = [62, 23, 2, 3, 4, 5, 6]

plt.figure(figsize=(10, 10))
explode = (0.1, 0, 0, 0, 0, 0, 0)  

plt.pie(percentages, labels=causes, explode=explode, autopct='%1.1f%%', startangle=70)
plt.axis('equal')
plt.title('Causes of Diseases')

plt.show()
