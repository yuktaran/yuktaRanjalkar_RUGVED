import pandas as pd
df=pd.read_csv("matches.csv", index_col="id")

matches_2008=df[df["season"]==2008]

print(str(len(matches_2008))+" matches were played in 2008")