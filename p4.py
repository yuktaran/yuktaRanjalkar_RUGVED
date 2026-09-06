import pandas as pd

df=pd.read_csv("matches.csv",index_col="id")

group=df.groupby("toss_winner")

count=group["toss_decision"].value_counts()
print(count)