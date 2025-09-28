# Creating dictionaries

# Example 1: Simple dictionary
person = {"name": "Geeta", "age": 25, "city": "Hyderabad"}

# Example 2: Dictionary with different data types
data = {
    "id": 101,
    "scores": [90, 85, 78],
    "is_active": True
}

print(person)
print(data)

print("-----------------------------------------------")

# Accessing/fetching values
# Using key

print(person["name"])  # Output: Geeta

print("-----------------------------------------------")

# Using get() method (safer if key might not exist)

print(person.get("age"))      # Output: 25
print(person.get("salary"))   # Output: None (doesn’t throw error)
print(person.get("salary", 0)) # Output: 0 (default value)

print("-----------------------------------------------")

# Updating dictionaries
# a) Adding new key-value

person["profession"] = "Tester"
print(person)  # Output: {'name': 'Geeta', 'age': 25, 'city': 'Hyderabad', 'profession': 'Tester'}

print("-----------------------------------------------")

# Updating existing key
person["age"] = 26
print(person)  # Output: {'name': 'Geeta', 'age': 26, 'city': 'Hyderabad', 'profession': 'Tester'}

print("-----------------------------------------------")

# Remove by key
person.pop("profession")
print(person)

# Remove last inserted item (Python 3.7+)
person.popitem()
print(person)

# Delete entire dictionary
# del person

print("-----------------------------------------------")

# Fetching all keys, values, or items
print(person.keys())   # dict_keys(['name', 'age', 'city', 'hobby'])
print(person.values()) # dict_values(['Geeta', 27, 'Bangalore', 'Reading'])
print(person.items())  # dict_items([('name', 'Geeta'), ('age', 27), ('city', 'Bangalore'), ('hobby', 'Reading')])
