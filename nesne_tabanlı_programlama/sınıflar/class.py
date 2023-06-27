"""
# class

class Person:
    pass
    # class attiributes

    # object attiributes

    # methods



# object, instance

p1 = Person()
p2 = Person()

print(p1)
print(p2)
print(type(p1))
print(type(p2))
print(p1 == p2)
"""

class Person:
    # class attiributes
    address = "no information"
    # constructor (yapıcı metod)
    def __init__(self, name, year):
        # object attiributes
        self.name = name
        self.birthyear = year
        print("init metodu çalıştı.")
        # methods

# object, instance
p1 = Person(name = "Fatih",year = 1996)
p2 = Person("Yağmur", 1995)

# updating
p1.name = "Ahmet"
p1.address ="Istanbul"
# accessing object attributes
print(f"p1 => name: {p1.name} year: {p1.birthyear} address: {p1.address}")
print(f"p2 => name: {p2.name} year: {p2.birthyear} address: {p2.address}")