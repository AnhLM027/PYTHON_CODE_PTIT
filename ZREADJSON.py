# json.loads() → chuỗi JSON → Python object
# json.dumps() → Python object → chuỗi JSON
# json.load() → file JSON → Python object
# json.dump() → Python object → file JSON
# Python object tương ứng với JSON:
# dict → object
# list → array
# str → string
# int/float → number
# True/False → true/false
# None → null

import json

s = '{"name": "Alice", "age": 25, "phone": "0912345678"}'
data = json.loads(s)  # chuyển chuỗi JSON -> dict
print(data['name'], data['age'])



data = {"name": "Bob", "age": 30, "phone": "0923456789"}
s = json.dumps(data)  # dict -> chuỗi JSON
print(s)



import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)  # đọc file JSON -> dict hoặc list
print(data)



import json

data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30}
]

with open("output.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
