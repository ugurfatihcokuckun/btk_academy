names = ["Ali", "Yağmur", "Hakan", "Deniz"]
years = [1998, 2000, 1998, 1987]


names.append("Cenk")

names.insert(0, "Sena")

# names.remove("Deniz")

index = names.index("Deniz")

result = "Ali" in names

names.reverse()
years.reverse()

names.sort()
years.sort()

str = "Chevrolet,Dacia".split(",")

a = min(years)
b = max(years)

c = years.count(1998)

years.clear()


print(names)
print(years)
print(str)
print(a)
print(b)
print(c)


brands = []

brand = input("Marka: ")
brands.append(brand)

brand = input("Marka: ")
brands.append(brand)

brand = input("Marka: ")
brands.append(brand)

print(brands)