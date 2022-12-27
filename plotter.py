import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('timeseries.csv')

df = df[['x', 'y']]

plt.plot(df)
plt.show()

df = pd.read_csv('eigenvalues.csv')

df = df[['real_0', 'real_1', 'imag_0', 'imag_1']]

plt.plot(df)
plt.show()