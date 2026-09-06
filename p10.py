import pandas as pd

df=pd.read_csv("matches.csv", index_col="city")

count=df["player_of_match"].value_counts()
count=count[count>3]

print(count.to_string())