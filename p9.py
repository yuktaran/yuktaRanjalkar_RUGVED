import pandas as pd

df=pd.read_csv("matches.csv", index_col="city")


print(df["win_by_runs"].idxmax()+" "+str(df["win_by_runs"].max()))
print(df["win_by_runs"].idxmin()+" "+str(df["win_by_runs"].min()))