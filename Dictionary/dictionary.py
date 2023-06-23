# key => value

# cities = ["Kocaeli", "Istanbul"]
# plakalar = [41, 34]

# print(plakalar[cities.index("Kocaeli")])

# plakalar = {"Kocaeli": 41, "Istanbul": 34}

# print(plakalar["Kocaeli"])

# plakalar["Ankara"] = 6

# print(plakalar)

# plakalar["Kocaeli"] = "new value"

# print(plakalar)

users = {
    "sadikturan": {
        "age": 36,
        "roles":["user"],
        "email": "sadikturan@gmail.com",
        "address": "Kocaeli",
        "phone": "123231312"
    },
    "cinarturan": {
        "age": 2,
        "roles":["admin", "user"],
        "email": "cinarturan@gmail.com",
        "address": "Kocaeli",
        "phone": "323232232"
    }

}

# print(users["cinarturan"]["age"])
# print(users["cinarturan"]["address"])
# print(users["cinarturan"]["email"])
print(users["cinarturan"]["roles"][0])

