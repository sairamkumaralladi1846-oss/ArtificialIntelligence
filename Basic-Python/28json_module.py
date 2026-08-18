import json

#converting python dictionary to json string
data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "is_student": None
}
json_string = json.dumps(data)
print(type(json_string), json_string) 

#converting json string to python dictionary
json_string = '{"name": "John", "age": 30, "city": "New York", "is_student": null}'
python_dict = json.loads(json_string)
print(type(python_dict), python_dict)


#reading json data from a file
with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)


#writing json data to a file
data = {
    "name": "Alice",
    "age": 25,
    "city": "Los Angeles",
    "is_student": True
}
with open('output.json', 'w') as file:
    json.dump(data, file, indent=4, sort_keys=True)  # Writing with indentation for better readability
