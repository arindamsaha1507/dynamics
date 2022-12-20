import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('out.csv')

df = df[['x']]

plt.plot(df)
plt.show()