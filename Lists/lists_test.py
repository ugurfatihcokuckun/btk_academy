cars = ["Bmw", "Mercedes", "Opel", "Mazda"]

lenght_of_cars = len(cars)

first_component = cars[0]
last_component = cars[lenght_of_cars - 1]
last_component = cars[-1]

# cars[-1] = "Toyota"

result = "Mercedes" in cars

result = cars[-2]

result = cars[0:3]
result = cars[:3]
result = cars[-2:]

cars[-2:] = ["Toyota", "Renault"]

result = cars + ["Audi", "Nissan"]

del cars[-1]
result = cars

result = cars[::-1]

studentA = ["Yiğit", "Bilgi", 2010, [70,60,70]]
studentB = ["Sena", "Turan", 1999, [80,80,70]]
studentC = ["Ahmet", "Turan", 1998, [80,70,90]]

result = studentA[0]
result = studentC[3]
result = studentB[3][1]

result = f"{studentA[0]} {studentA[1]} {2023 - studentA[2]} Yaşinda ve not ortalamasi {round((studentA[3][0] + studentA[3][1] + studentA[3][2]) / 3)}"




print(result)