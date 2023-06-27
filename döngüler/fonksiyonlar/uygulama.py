"""
# def name():
#     a = input("isim yazın: ")
#     b = int(input("kaç kere yazılsın: "))
#     while b > 0:
#         print(a)
#         b -=1

# name()
"""
"""
# def yazdir(kelime,adet):
#     print(kelime * adet)

# yazdir("Mrhb\n", 10)
"""
"""
def listeyeCevir(*args):
    list = []

    for arg in args:
        list.append(arg)
    return list

result = listeyeCevir(10,20,30,"Merhaba")
print(result)
"""


"""
def asalSayilariBul(sayi,sayi2):
    for sayi in range(sayi1, sayi2 + 1):
        if sayi > 1:
            for i in range(2,sayi):
                if sayi % i == 0:
                    break
            else:
                print(sayi)

sayi1 = int(input("sayı 1: "))
sayi2 = int(input("sayı 2: "))

asalSayilariBul(sayi1, sayi2)
"""

"""
def tamBolenleriBul(sayi):
    tamBolenler = []
    for i in range(2,sayi):
        if sayi % i == 0:
            tamBolenler.append(i)
    return tamBolenler

print(tamBolenleriBul(20))
"""