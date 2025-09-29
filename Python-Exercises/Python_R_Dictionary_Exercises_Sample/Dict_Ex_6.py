my_dict = {"name": "Geeta", "age": 30, "city": "Pune"}

# Remove by key
my_dict.pop("age")
print(my_dict)
# Output: {'name': 'Geeta', 'city': 'Hyderabad'}

# Remove last inserted item
my_dict.popitem()
print(my_dict)
# Output: {'name': 'Geeta'}

# Delete entire dictionary
# del my_dict
# print(my_dict)  # Error, dictionary is deleted
