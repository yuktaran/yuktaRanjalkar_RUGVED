import pandas as pd

df=pd.read_csv("matches.csv", index_col="id")

count=df["city"].value_counts()
print("most played city-"+ count.idxmax())
print("least played city-"+ count.idxmin())