import pandas as pd

df=pd.read_csv("matches.csv", index_col="id")

df1=df[df["result"]=="tie"]
print(df1[["team1", "team2"]])