import pandas as pd

df=pd.read_csv("matches.csv", index_col="id")

count1=df["umpire1"].value_counts()
count2=df["umpire2"].value_counts()
count3=df["umpire3"].value_counts()
print("most umpiring as umpire1- "+ str(count1.idxmax()))
print("most umpire2- "+ str(count2.idxmax()))
print("most umpire3- "+str(count3.idxmax()))
