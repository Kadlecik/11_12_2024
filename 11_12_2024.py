
import json



data = {"name": "John",
        "age": 25,
        "kids": [],
        "married": False}

j_data = json.dumps(data)
print(j_data)
print(data)
