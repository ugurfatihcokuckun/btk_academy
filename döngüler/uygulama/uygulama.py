import random

number = random.randint(1,100)

print(number)

guest = 0
hak = 8

while guest != number:
    guest = int(input("Tahmin et bakalım: "))
    if hak == 0:
        print("yandın")
        break
    if number < guest:
        print("aşağıt git")
    elif number > guest:
        print("yukarı git")
    elif number == guest:
        print("bildin")
    hak -= 1


