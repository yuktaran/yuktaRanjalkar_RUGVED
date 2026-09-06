import pandas as pd

df=pd.read_csv("deliveries.csv")

df1=df[df["player_dismissed"].notna()]

group=df1.groupby("bowler")["player_dismissed"].count()
print(group.to_string())