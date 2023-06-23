
# studenst = {
#     "120": {
#         "ad": "Ali",
#         "soyad": "Yilmaz",
#         "telefon": "532 000 00 01"
#     },
#     "125": {
#         "ad": "Can",
#         "soyad": "Korkmaz",
#         "telefon": "532 000 00 02"
#     },
#     "128": {
#         "ad": "Can",
#         "soyad": "Korkmaz",
#         "telefon": "532 000 00 03"
#     }
# }



# students[number] = {
#     "ad" : name,
#     "soyad": surname,
#     "telefon": phone
# }

students = {}

number = input("student number: ")
name = input("student name: ")
surname = input("student surname: ")
phone = input("phone number: ")


students.update({
    number: {
        "ad": name,
        "soyad": surname,
        "telefon": phone
    }
})


number = input("student number: ")
name = input("student name: ")
surname = input("student surname: ")
phone = input("phone number: ")

students.update({
    number: {
        "ad": name,
        "soyad": surname,
        "telefon": phone
    }
})


number = input("student number: ")
name = input("student name: ")
surname = input("student surname: ")
phone = input("phone number: ")

students.update({
    number: {
        "ad": name,
        "soyad": surname,
        "telefon": phone
    }
})


print(students)


# a = input("student number: ")

# print(studenst[a])