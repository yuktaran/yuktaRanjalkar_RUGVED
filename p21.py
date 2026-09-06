import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("matches.csv")

group=df.groupby(["winner"]).size()

plt.scatter(group.index, group.values)
plt.show()