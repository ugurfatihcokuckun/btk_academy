import random

# result = dir(random)
# result = help(random)

result = random.random()
result = random.uniform(1,10)
result = random.randint(1,10)

names = ["Ali", "Yağmur", "Deniz", "Cenk"]
result = names[random.randint(0,len(names)-1)]
result = random.choice(names)
result = random.sample(names, 2)

greeting = "Hello There"
result = random.choice(greeting)

list = list(range(10))
random.shuffle(list)
result = list

list = range(100)
result = random.sample(list, 3)


print(result)