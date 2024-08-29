import json

# Reading from a JSON file
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# Accessing values
print(data['name'])  # Output: Alice
print(data['age'])   # Output: 25

