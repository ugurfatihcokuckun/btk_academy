import pandas as pd

data = {
    "Column1": [1,2,3,4,5],
    "Column2": [10,20,13,20,25],
    "Column3": ["abc","bca","ade","cba","dea"]
}

df = pd.DataFrame(data)

result = df["Column2"].unique()
result = df["Column2"].nunique()
result = df["Column2"].value_counts()
result = df["Column1"] * 2

def kare_al(x):
    return x * x
result = df["Column2"].apply(kare_al)
result = df["Column2"].apply(lambda x: x * x)
result = df["Column3"].apply(len)
df["Column4"] = df["Column3"].apply(len)
result = df.columns
result = len(df.columns)
result = df.index
result = df.info
result = df.sort_values("Column2")
result = df.sort_values("Column2", ascending=False)
result = df.pivot_table(index="Column1", columns="Column3", values="Column2")

print(df)
print(result)