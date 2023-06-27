# def square(num): return num ** 2

# result = square(2)

# print(result)


"""
def square(num): return num ** 2

numbers = [1,3,5,9]

result = list(map(square, numbers))

print(result)

for item in map(square, numbers):
    print(item)
"""
"""
def square(num): return num ** 2

numbers = [1,3,5,9]

result = list(map(square, numbers))

print(result)

for item in map(square, numbers):
    print(item)
"""
"""
numbers = [1,3,5,9]
result = list(map(lambda num: num ** 2, numbers))
print(result)
"""
"""
square = lambda num: num ** 2

numbers = [1,3,5,9]

result = list(map(square,numbers))
print(result)
"""
"""
numbers = [1,3,5,9,10,4]

def check_even(num): return num % 2 == 0

result = list(filter(check_even, numbers))
result = list(filter(lambda num: num % 2 == 0, numbers))

print(result)
"""