import pandas as pd
df=pd.read_csv("deliveries.csv")

df1=df[df["batsman_runs"]==6]

print(df1)