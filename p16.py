import pandas as pd

df=pd.read_csv("deliveries.csv")

group=(df.groupby("batsman")["batsman_runs"].sum()).nlargest(10)

print(group)