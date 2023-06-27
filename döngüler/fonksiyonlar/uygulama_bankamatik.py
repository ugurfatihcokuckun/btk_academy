hesapFatih = {
    "ad": "Fatih",
    "hesap no": "56545466",
    "bakiye": 3000,
    "ekHesap": 2000
}

hesapAli = {
    "ad": "Ali",
    "hesap no": "56545888",
    "bakiye": 2000,
    "ekHesap": 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -= miktar
        print("Paranızı alabilirsiniz.")
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]

        if toplam >= miktar:
            ekHesapKullanımı = input("ek hesap kullanılsın mı? (e/h)")

            if ekHesapKullanımı == "e":
                ekHesapKullanılacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] += ekHesapKullanılacakMiktar
                print("paranızı alabilirsiniz.")
            else:
                print(f"{hesap['hesap no']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
            print("bakiye yetersiz.")



paraCek(hesapFatih,3000)
paraCek(hesapFatih,2000)
