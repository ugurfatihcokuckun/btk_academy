'''
numbers = [1,3,5,7,9,12,19,21]

# for num in numbers:
#     if num % 3 == 0:
#         print(num)

# toplam = 0
# for num in numbers:
#     toplam += num
# print(toplam)

# for num in numbers:
#     if num % 2 ==1:
#         num **= 2
#         print(num)
'''



"""
cities = ["kocaeli", "istanbul", "ankara", "izmir", "rize"]

for city in cities:
    if len(city) <= 5:
        print(city)
"""


urunler = [
    {"name":"samsung S6", "price": "3000"},
    {"name":"samsung S7", "price": "4000"},
    {"name":"samsung S8", "price": "5000"},
    {"name":"samsung S9", "price": "6000"},
    {"name":"samsung S10", "price": "7000"}
]

# toplam = 0

# for urun in urunler:
#     toplam += int(urun["price"])

# print(toplam)

for urun in urunler:
    if int(urun["price"]) >= 5000:
        print(urun["name"]) 
