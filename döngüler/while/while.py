# x = 0

# while x <= 100:
#     if x % 2 == 1:
#         print(f"sayi tek {x}")
#     if x % 2 == 0:
#         print(f"sayi çift {x}")
#     x += 1
# print("bitti...")


name = ""

while not name.strip():
    name = input("isminizi girin: ")

print(f"Merhaba, {name}")