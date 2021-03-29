import json
data_JSON = """
{
    "size": "Medium",
    "price": 15.67,
    "toppings": ["Mushrooms", "Extra Cheese", "Pepperoni", "Basil"],
    "client": {
        "name": "Imran Khan",
        "phone": "01610043686",
        "email": "duetboyimran@gmail.com"    
    }
}    
"""

data_dict = json.loads(data_JSON)
# print(data_JSON)

client = {
    "name": "Nora",
    "age": 56,
    "id": "45355",
    "eye_color": "green",
    "wears_glasses": False
}

client_JSON = json.dumps(client, indent=4, sort_keys=True)
# print(client_JSON)

with open("data/json_data.json") as file_obj:
    data = json.load(file_obj)

print(data)