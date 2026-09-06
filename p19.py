import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("matches.csv")

df1=df[df["toss_decision"]=="bat"]
df2=df[df["toss_decision"]=="field"]
group1=df1.groupby(["season"]).size()
group2=df2.groupby(["season"]).size()

plt.xlabel("Season")
plt.ylabel("Number of decisions")
plt.grid()
plt.plot(group1.index,group1.values, label="Bat")
plt.plot(group2.index,group2.values, label="Field")
plt.legend()
plt.show()