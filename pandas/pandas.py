import pandas as pd
import numpy as np


numbers = [20, 30, 40, 50]
letters = ["a", "b", "c", "d", 20]
scaler = 5
dict = {"a": 10, "b": 20, "c": 30, "d": 40}
random_numbers = np.random.randint(10, 100, 6)


# pandas_series = pd.Series(letters)
# pandas_series = pd.Series(scaler)
# pandas_series = pd.Series(scaler, [0, 1, 2, 3])
# pandas_series = pd.Series(numbers, ["a", "b", "c", "d"])
# pandas_series = pd.Series(dict)
# pandas_series = pd.Series(random_numbers)

# pandas_series = pd.Series([20, 30, 40, 50], ["a", "b", "c", "d"])
# result = pandas_series[0]
# result = pandas_series.ndim
# result = pandas_series.shape
# result = pandas_series.sum()
# result = pandas_series >=50

# print(pandas_series)
# print(result)


opel2018 = pd.Series([20, 30, 40, 10], ["astra", "corsa", "mokka", "insignia"])
opel2019 = pd.Series([40, 30, 20, 10], ["astra", "corsa", "grandland", "insignia"])

total = opel2018 + opel2019

print(total)