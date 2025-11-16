# get(key, default) — Access value by key, safe if the key is missing.
my_dict = {"a": 1, "b": 2}
print(my_dict.get("a"))  # Output: 1
print(my_dict.get("c", 0))  # Output: 0


# keys() — Get all keys in the dictionary.
my_dict = {"a": 1, "b": 2}
print(list(my_dict.keys()))  # Output: ['a', 'b']


# values() — Get all values in the dictionary.
my_dict = {"a": 1, "b": 2}
print(list(my_dict.values()))  # Output: [1, 2]


# items() — Get all key-value pairs as tuples.
my_dict = {"a": 1, "b": 2}
print(list(my_dict.items()))  # Output: [('a', 1), ('b', 2)]
