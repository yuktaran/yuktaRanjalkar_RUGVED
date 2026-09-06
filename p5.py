import pandas as pd

df=pd.read_csv("matches.csv", index_col="id")

df1=df[df["result"]!="no result"]
count=df1["result"].value_counts()
print(count)