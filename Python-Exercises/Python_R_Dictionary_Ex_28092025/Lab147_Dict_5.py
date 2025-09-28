# Dictionary from 2 lists

keys = ["name", "role", "experience"]
values = ["Geeta", "SDET"]

my_dict = dict(zip(keys,values))
print(my_dict) # {'name': 'Geeta', 'role': 'SDET'}


keys = ["name", "role", "experience"]
values = ["Geeta", "SDET", 3]

my_dict = dict(zip(keys,values))
print(my_dict) # {'name': 'Geeta', 'role': 'SDET', 'experience': 3}

# Merge Two Dictionaries

dict1 = {"a":1, "b":2}
dict2 = {"c":3, "d":4}

merge_dict = dict1 | dict2
print(merge_dict) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(merge_dict.get("a"))



