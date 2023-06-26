number = int(input("sayı girin: "))
asalmi= True

if number == 1:
    asalmi = False

for i in range(2,number):
    if number % i == 0:
        asalmi = False
        break

if asalmi:
    print("sayı asaldır.")
else:
    print("sayı asal değildir.")