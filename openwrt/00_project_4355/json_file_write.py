import json

# Data to be written to the JSON file
data = {
    "name": "Alice",
    "age": 25,
    "city": "Los Angeles"
}

# Writing to a JSON file
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)
