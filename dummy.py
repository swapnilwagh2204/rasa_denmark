import json

with open('data.json') as f:
    data = json.load(f)

print(data[0])
