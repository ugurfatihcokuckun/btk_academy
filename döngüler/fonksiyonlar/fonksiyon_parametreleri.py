# def changeName(n):
#     n = "ada"

# name = "yiğit"

# changeName(name)

# print(name)


# def change(n):
#     n[0] = "istanbul"

# sehirler = ["ankara","izmir"]

# change(sehirler[:])

# print(sehirler)


# def add(a,b,c=0,d=0,e=0):
#     return sum((a,b,c,d,e))

# print(add(10,20))
# print(add(10,20,30))
# print(add(10,20,30,40,50))



# def add(*params):
#     return sum((params))

# print(add(10,20))
# print(add(10,20,30))
# print(add(10,20,30,40,50,60,70,80))



def add(*params):
    print(params)
    print(params[1])
    return sum((params))

print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40,50,60,70,80))



# def add(*params):
#     sum = 0
#     for n in params:
#         sum = sum + n
#     return sum

# print(add(10,20))
# print(add(10,20,30))
# print(add(10,20,30,40,50,60,70,80))

"""
def displayUser(**params):
    for key,value in params.items():
        print("{} is {}".format(key,value))



displayUser(name = "Fatih", age = 27, city = "Istanbul")
displayUser(name = "Nana", age = 22, city = "Kocaeli", phone = "123456")
displayUser(name = "Yiğit", age = 14, city = "Ankara", phone = "545679", email = "email@gmail.com")
"""


"""
def myFunc(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,key1 = "value1", key2 = "value2")
"""