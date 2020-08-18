import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Practice4.csv', names=['time','temperature','humidity'])

fig, ax1 = plt.subplots()
ax1.plot(df['temperature'],color='red')
ax2 = ax1.twinx()
ax2.plot(df['humidity'])
plt.show()