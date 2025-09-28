dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"a": 1, "b": 2}

missing_keys = set(dict1.keys()) - set(dict2.keys())
print(missing_keys)  # {'c'}

# Sort a dictionary by it's values in descending order

my_dict = {"a": 3, "b": 1, "c": 2}

# {b:1,c:2,a:3}

# sort by values descending
my_dict = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
print(my_dict)

'''
data = {'apple': 3, 'banana': 5, 'cherry': 2}

# sort by values descending
data = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))

print(data)
Step-by-step
data = {'apple': 3, 'banana': 5, 'cherry': 2}

You create a dictionary named data. Keys are fruits, values are numbers.

data.items()

This produces an iterable view of key–value pairs as tuples: dict_items([('apple', 3), ('banana', 5), ('cherry', 2)]).

If you convert to a list: list(data.items()) → [('apple', 3), ('banana', 5), ('cherry', 2)].

sorted(data.items(), key=lambda x: x[1], reverse=True)

sorted(...) takes that iterable and returns a new list sorted according to the key function.

key=lambda x: x[1] means: for each item (a tuple like ('apple', 3)), use x[1] (the value 3) as the sort key.

reverse=True makes the order descending (largest value first).

So the result becomes: [('banana', 5), ('apple', 3), ('cherry', 2)].

dict(...)

dict() converts an iterable of (key, value) tuples back into a dictionary.

dict([('banana',5), ('apple',3), ('cherry',2)]) → {'banana': 5, 'apple': 3, 'cherry': 2}.

Note: In Python 3.7+ dictionaries preserve insertion order, so the printed dictionary appears in the sorted (descending) order.

data = dict(...) and print(data)

We reassign the sorted dictionary back to the name data and print it.

Final printed output: {'banana': 5, 'apple': 3, 'cherry': 2}

'''