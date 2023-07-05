import json

person_string = '{"name": "Fatih", "languages": ["python", "C#"]}'   #json modülünü kullanmak için dict string olarak tanımlanır

# result = person["languages"]
# result = person["languages"][0]

"""
# Json string to Dictionary
result = json.loads(person_string)
print(type(result))
print(result)
print(result["languages"])
"""

"""   
with open("person.json") as f:
    data = json.load(f)    # sayfayı projeye getirir
    print(data["name"])
"""

"""
person_dict = {
    "name": "Fatih",
    "languages": ["Python", "C#"]
}
"""

"""
# Dict to Json string
result = json.dumps(person_dict)
print(result)
print(type(result))
# print(result["name"])   # error verir stringe dönüştüğü için
"""

"""
with open("person2.json", "w") as f:
    json.dump(person_dict, f)   # dosya üzerine yazar
"""

"""
person_dict = json.loads(person_string)
result = json.dumps(person_dict, indent= 4, sort_keys= True)
print(person_dict)
print(result)
"""