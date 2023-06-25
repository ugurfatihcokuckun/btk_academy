# a = int(input("Sayi girin: "))
# result = (a < 0) and (a < 100)
# print(result)


# b = int(input("Sayi girin: "))
# result = (b > 0) and (b % 2 == 0)
# print(result)


# email = input("email girin: ")
# password = int(input("Password girin: "))
# result = (email == "fatih@gmail.com")  and (password == 12345)
# print(result)


# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
# result = [a, b, c]
# result.sort()
# print(result)

# vize1 = int(input("Vize1: "))
# vize2 = int(input("Vize2: "))
# final = int(input("Final: "))
# result = ((vize1 + vize2) / 2 * 0.6) + (final * 0.4)
# gecti = ((result >= 50) and (final >= 50)) or (final >= 70)
# print(f"öğrenci geçti {result}, {gecti}")


ad = input("ad: ")
kilo = float(input("kilo: "))
boy = float(input("boy: "))

formül = kilo / boy ** 2

result = (formül > 0) and (formül < 18.4)
print(f"Oran {formül}, Zayif", {result})

result = (formül > 18.5) and (formül < 24.9)
print(f"Oran {formül}, Normal", {result})

result = (formül > 25) and (formül < 29.9)
print(f"Oran {formül}, Kilolu", {result})

result = (formül > 30) and (formül < 34.9)
print(f"Oran {formül}, obez", {result})