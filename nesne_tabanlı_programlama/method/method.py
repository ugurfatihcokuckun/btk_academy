"""
class Person:
    # class attiributes
    address = "no information"
    
    # constructor (yapıcı metod)
    def __init__(self, name, year):
         
        # object attiributes
        self.name = name
        self.birthyear = year
        
    # methods
    # instance method
    def intro(self):
        print("Hello There I am " + self.name)
    # instance method
    def calculateAge(self):
        return 2023 - self.birthyear

# object, instance
p1 = Person(name = "Fatih",year = 1996)
p2 = Person("Yağmur", 1995)


p1.intro()
p2.intro()
print(f"adım : {p1.name} ve yaşım: {p1.calculateAge()}")
print(f"adım : {p2.name} ve yaşım: {p2.calculateAge()}")
"""


class Circle:
    # Class Object attribute
    pi = 3.14

    def __init__(self, yaricap = 1):
        self.yaricap = yaricap

    # Methods
    def cevre_hesapla(self):
        return 2*self.pi*self.yaricap

    def alan_hesapla(self):
        return self.pi * (self.yaricap ** 2) 

c1 = Circle()
c2 = Circle(5)

print(f"c1: alan = {c1.alan_hesapla()}  çevre : {c1.cevre_hesapla()}")
print(f"c2: alan = {c2.alan_hesapla()}  çevre : {c2.cevre_hesapla()}")
