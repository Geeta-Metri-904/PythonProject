# Remove duplicate values from dictionary

# {"a" : 10, "c":30, "b": 20, "c": 30 }

my_dict = {"a": 10, "c": 30, "b": 20, "c": 30}

unique_value = set()
result = {}

for key, value in my_dict.items():
    if value not in unique_value:
        result[key] = value
        unique_value.add(value)

print(result) # {'a': 10, 'c': 30, 'b': 20}