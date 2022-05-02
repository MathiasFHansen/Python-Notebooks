import matplotlib.pyplot as plt
import pandas as pd
iris = pd.read_csv('iris_data.csv')
df = iris[['Sepal length','Sepal width','Species']]
unique_labels = df['Species'].unique()

fig, ax = plt.subplots()
for flower in df:
    x = df['Sepal length']
    y = df['Sepal width']
    colors = unique_labels
    color = ['blue','red','green']
    ax.scatter(x, y, c=color, label=colors,
               alpha=0.3, edgecolors='none')

ax.legend()
ax.grid(True)

plt.show()
#print(unique)
#print(df)