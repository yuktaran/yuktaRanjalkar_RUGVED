import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("matches.csv",index_col="id")

figure, axes=plt.subplots(1,2)

t1=df["team1"].value_counts()
t2=df["team2"].value_counts()
t3=df["winner"].value_counts()
total=t1.add(t2)
total=total.sort_values(ascending=False)
axes[0].bar(total.index, total.values, label="Total matches played", )
axes[0].bar(t3.index, t3.values, label="Matches won")
axes[0].legend()

w=total/t3

axes[1].bar(w.index, w.values)

plt.show()


