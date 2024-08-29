import json

# Original object
user_profile = {
    "name": "John Doe",
    "age": 30,
    "email": "johndoe@example.com"
}

# Serialization (object to JSON string)
serialized_profile = json.dumps(user_profile)

# Deserialization (JSON string back to object)
deserialized_profile = json.loads(serialized_profile)

