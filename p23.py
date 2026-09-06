import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("matches.csv")

group=(df.groupby("winner")).size().nlargest(5)

plt.bar(group.index,group.values)
plt.show()