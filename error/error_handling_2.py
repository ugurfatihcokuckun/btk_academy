list = ["1", "2", "5a", "10b", "abc", "10", "50"]
"""
for x in list:
    try:
        result = int(x)
        print(result) 
    except ValueError:
        continue
"""
"""
while True:
    sayi = input("sayı: ")
    if sayi == "q":
        break

    try:
        result = float(sayi)
        print("girdiğiniz sayı: ", result)
    except ValueError:
        print("geçersiz sayı")
        continue
"""
"""
def checkPassword(parola):

    turkce_karakterler = "şçğüöıİ"

    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("Parola türkçe karakter içeremez.")
        else:
            pass
    print("geçerli parola")

parola = input("parola: ")

try:
    checkPassword(parola)
except TypeError as err:
    print(err)
"""

def faktoriyel(x):
    x = int(x)

    if x < 0:
        raise ValueError("Negatif değer")
    
    result = 1

    for i in range(1, x + 1):
        result *= i
    
    return result

for x in [5, 10, 20, -3, "10a"]:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)