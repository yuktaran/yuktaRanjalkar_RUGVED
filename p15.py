import pandas as pd

df1=pd.read_csv("matches.csv")
df2=pd.read_csv("deliveries.csv")
merged=pd.merge(df1,df2,left_on="id", right_on="match_id")

totalruns=merged.groupby("season")["total_runs"].sum()
print(totalruns)
