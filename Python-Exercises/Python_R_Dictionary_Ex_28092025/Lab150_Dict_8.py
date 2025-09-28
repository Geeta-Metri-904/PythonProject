# function that returns the maximum value from dictionary

# {"a" : 10, "b": 20, "c": 30 }

dictionary = {"a" : 10, "b": 20, "c": 30 }

def max_value_dict(dictionary):
    return max(dictionary.values())

print(max_value_dict({"a" : 10, "b": 20, "c": 30 }))



def min_value_dict(dictionary):
    return min(dictionary.values())

print(min_value_dict({"a" : 10, "b": 20, "c": 30 }))
print(dictionary.values())   # dict_values([10, 20, 30])