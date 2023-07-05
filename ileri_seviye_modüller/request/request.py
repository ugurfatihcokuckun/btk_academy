import requests
import json

result = requests.get("https://jsonplaceholder.typicode.com/todos")
# result = result.text
result = json.loads(result.text)

for i in result:
    print(i)

for i in result:
    print(i["title"])

for i in result:
    if i["userId"] == 1:
        print(i["title"])

# print(result)
# print(result[0]["title"])
# print(result[0])
# print(type(result))