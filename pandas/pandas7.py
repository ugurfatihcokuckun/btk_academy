import pandas as pd
import numpy as np

data = pd.read_csv("all_seasons.csv")
'''
data["player_name"] = data["player_name"].str.lower()
data["index"] = data["player_name"].str.find("a")
print(data[["player_name","index"]])
'''
# data = data[data.player_name.str.contains("Jordan")]
# data = data.player_name.str.replace(" ","-")
data[["first_name","last_name"]] = data["player_name"].loc[data["player_name"].str.split().str.len()==2].str.split(expand=True)

print(data)