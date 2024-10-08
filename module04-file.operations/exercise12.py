import pandas as pd

df1 = pd.read_csv("countries_pandas.csv")
print(df1.index)
print(df1.columns)
print(df1)
df1.info()

df2 = pd.read_json("countries.json")
print(df2.index)
print(df2.columns)
print(df2)
df2.info()
