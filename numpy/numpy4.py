import numpy as np

number1 = np.random.randint(10, 100, 6)
number2 = np.random.randint(10, 100, 6)

# print(number1)
# print(number2)

result = number1 + number2
result = number1 + 10
result = number1 * number2
result = np.sin(number1)
result = np.cos(number2)
result = np.sqrt(number1)
result = np.log(number1)

multi_numbers1 = number1.reshape(2, 3)
multi_numbers2 = number2.reshape(2, 3)
result = np.vstack((multi_numbers1, multi_numbers2))
result = np.hstack((multi_numbers1, multi_numbers2))

result = number1 >= 50
result = number1 % 2 == 0
print(number1[result])

print(result)