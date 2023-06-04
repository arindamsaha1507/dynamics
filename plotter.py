import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('timeseries.csv')

df = df[['x', 'y']]

plt.plot(df)
plt.show()

