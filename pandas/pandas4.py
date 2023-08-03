import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data, columns=["Column1","Column2","Column3","Column4","Column5"])
result = df

result1 = df.columns
result1 = df.head()
result1 = df.tail(10)
result1 = df["Column1"].head()
result1 = df.Column1.head()
result1 = df[["Column1","Column2"]].head()
result1 = df[5:15][["Column1","Column2"]].head()
result1 = df[5:15][["Column1","Column2"]].tail()
result1 = df > 50
result1 = df[df > 50]
result1 = df[df % 2 == 0]
result1 = df["Column1"] > 50
result1 = df["Column1"].head() > 50
result1 = df[df["Column1"] > 50]
result1 = df[df["Column1"] > 50]["Column1"]
result1 = df[(df["Column1"] > 50) & (df["Column1"] <= 70)]
result1 = df[(df["Column1"] > 50) & (df["Column3"] <= 70)]
result1 = df[(df["Column1"] > 50) | (df["Column2"] <= 70)][["Column1","Column2"]]
result1 = df.query("Column1 >= 50 & Column1 %2 == 0")
result1 = df.query("Column1 >= 50 | Column1 %2 == 0")[["Column1","Column2"]]

print(result)
print((result1))