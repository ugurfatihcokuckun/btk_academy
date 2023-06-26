"""
numbers = [1,3,5,7,9,12,19,21]

a = 0
while a < len(numbers):
    print(numbers[a])
    a += 1
"""


"""
a = int(input("ilk sayıyı girin: "))
b = int(input("son sayıyı girin: "))

while b > a:
    if a % 3 == 0:
        print(a)
    a += 1
"""

"""
a = 100

while a > 0:
    a -= 1
    print(a)
"""


"""
a = 0
b = []

while a < 5:
    b.append(input("sayı girin: "))
    a += 1
b.sort()
print(b)
"""


"""
urunler = []
adet = int(input("kaç adet ürün eklemek istiyorsunuz: "))
i = 0

while i<adet:
    name = input("ürün ismi: ")
    fiyat = input("ürün fiyatı: ")
    urunler.append({
        "name": name,
        "fiyat": fiyat
    })
    i +=1

for urun in urunler:
    print(f"ürün adı: {urun['name']}, ürün fiyatı: {urun['fiyat']} ")
"""