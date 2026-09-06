import pandas as pd

df=pd.read_csv("matches.csv", index_col="id")

count=df["season"].value_counts()

print(count)
