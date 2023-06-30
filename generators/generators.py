"""
def cube():
    result = []

    for i in range(5):
        result.append(i**3)
    return result

print(cube())
"""

"""
def cube():

    for i in range(5):
        yield i ** 3

iterator = cube()

for i in iterator:
    print(i)
"""

"""
def cube():
    for i in range(5):
        yield i ** 3

for i in cube():
    print(i)
"""

liste = [i**3 for i in range(5)]
print(liste)

liste2 = (i**3 for i in range(5))
print(liste2)

# print(next(liste2))
# print(next(liste2))
# print(next(liste2))
for i in liste2:
    print(i)