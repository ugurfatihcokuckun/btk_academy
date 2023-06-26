def sayHello(name = "user"):
    print("Hello " + name)

sayHello("Fatih")
sayHello()



def sayHello(name = "user"):
    return "Hello " + name

msg = sayHello("Fatih")
print(msg)



def total(num1, num2):
    return num1 + num2

result = total(10,20)

print(result)



def yasHesapla(dogumYili):
    return 2023 - dogumYili

ageCinar = yasHesapla(2017)
ageFatih = yasHesapla(1996)

print(ageCinar, ageFatih)



def EmekliligeKacYilKaldi(dogumYili, isim):
    """
    DOCSTRING: Doğum yolınıza göre emekliliğnize kaç yıl kaldı.
    INPUT: Doğum yılı.
    OUTPUT: Hesaplanan yıl bilgisi.
    """
    yas = yasHesapla(dogumYili)    
    emeklilik = 65 - yas
    if emeklilik > 0:
        print(f"Emekliliğinize {emeklilik} yıl kaldı.")
    else:
        print("Zaten emekli oldunuz.")

EmekliligeKacYilKaldi(1983, "Fatih")

print(help(EmekliligeKacYilKaldi))