import json

dict_ex = {'brand': 'Volvo', 'Price':1.5, 'Vol':2.0}

# dump
dict_to_json = json.dumps(dict_ex)
print(type(dict_to_json), dict_to_json)

with open('dict_to_json.txt', 'w') as f:
    json.dump(dict_ex, f)

# load, loads
with open('dict_to_json.txt', 'r') as f:
    data = json.load(f)

print(data)

data_1 = json.loads(dict_to_json)
print(data_1)

import requests
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
print(todos)