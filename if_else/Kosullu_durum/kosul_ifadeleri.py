# user = int(input("Yaş girin: "))



# if user < 18:
#     print("Ehliyet alamaz.")
# else:
#     educate = input("Eğitim durumu: ")
#     if educate == "lise" or educate == "üniversite":
#         print("Ehliyet alabilir.")
#     else:
#         print("ehliyet alamaz.")
    

# grade1 = float(input("Birinci sınav sonucunu girin: "))
# grade2 = float(input("İkinci sınav sonucunu girin: "))
# result = (grade1 + grade2) / 2

# if result >= 0 and result <=24:
#     print("Not 0")
# elif result >= 25 and result <=44:
#     print("Not 1")
# elif result >= 45 and result <=54:
#     print("Not 2")
# elif result >= 55 and result <=69:
#     print("Not 3")
# elif result >= 70 and result <=84:
#     print("Not 4")
# elif result >= 85 and result <=100:
#     print("Not 5")

import datetime

tarih = input("aracınız hangi tarihte trafiğe çıktı (2019/8/8): ")
tarih = tarih.split("/")

trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
days = fark.days

if days <=365:
    print("1. servis aralığı")
elif days > 365 and days <= 365*2:
    print("2. servis aralığı")
elif days >365*2 and days <=365*3:
    print("3. servis aralığı")
else:
    print("hatalı süre")