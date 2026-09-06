import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("matches.csv")

figure, axes=plt.subplots(1,2)

df1=df[df["team1"]==df["toss_winner"]]["team1"].value_counts()
df2=df[df["team2"]==df["toss_winner"]]["team2"].value_counts()
totalw=df1.add(df2)

axes[0].bar(totalw.index, totalw.values)

df3=df[df["team1"]!=df["toss_winner"]]["team1"].value_counts()
df4=df[df["team2"]!=df["toss_winner"]]["team2"].value_counts()
totall=df3.add(df4)

axes[1].bar(totall.index, totall.values)

plt.show()

