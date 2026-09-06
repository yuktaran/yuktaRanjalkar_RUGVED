import pandas as pd

df1=pd.read_csv("matches.csv")
df2=pd.read_csv("deliveries.csv")
merged=pd.merge(df1,df2,left_on="id", right_on="match_id")

totalruns=merged.groupby("venue")["total_runs"].sum()
totalmatches=merged.groupby("venue")["match_id"].nunique()
print(totalruns/totalmatches)
