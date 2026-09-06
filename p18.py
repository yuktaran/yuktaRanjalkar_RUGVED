import pandas as pd

df=pd.read_csv("deliveries.csv")

totalruns=df.groupby("batsman")["batsman_runs"].sum()
totalballs=df.groupby("batsman").size()

print(totalruns/totalballs)