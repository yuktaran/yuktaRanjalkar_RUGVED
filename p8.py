import pandas as pd

df=pd.read_csv("matches.csv", index_col="id")

print(df["win_by_runs"].mean())
print(df["win_by_runs"].median())
print(df["win_by_runs"].std())
