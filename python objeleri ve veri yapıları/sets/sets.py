furuits = { "orange", "apple", "banana"}

# print(furuits[0]) setler indekslenemez

print(furuits)

for x in furuits:
    print(x)


furuits.add("cherry")
furuits.update(["mango","grape"])

furuits.remove("mango")
furuits.discard("apple")
print(furuits)

furuits.pop()
furuits.clear()

print(furuits)

furuits.clear()

print(furuits)


# myList = [1,2,5,4,4,2,1]

# print(set(myList))