# Example 1: Simple dictionary
person = {"name": "Geeta", "age": 25, "city": "Hyderabad"}

# Loop through keys
for key in person:
    print(key)
    print(person[key])
    print(key, person[key])


print("-----------------------------------------------")


# Loop through key-value pairs
for key, value in person.items():
    print(key, "->", value)


'''
Summary of dictionary operations

Operation    	Method/Example

Create	        my_dict = {"a": 1, "b": 2}
Access      	my_dict["a"] or my_dict.get("a")
Add/Update	    my_dict["c"] = 3 or my_dict.update({"a": 10, "d": 4})
Remove	        pop("a"), popitem(), del my_dict["a"]
Loop	        for k,v in my_dict.items():
Keys/Values	    my_dict.keys(), my_dict.values(), my_dict.items()


'''