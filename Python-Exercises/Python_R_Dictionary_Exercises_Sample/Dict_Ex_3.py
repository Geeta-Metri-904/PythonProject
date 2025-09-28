# 1. Create a dictionary with 5 of your favorite fruits and their prices.

my_dict = {"Mango": 60, "Apple": 200, "Guava": 40, "Orange": 150, "Banana": 20}

# 2. Access and print the price of one fruit from your dictionary.

print(my_dict["Mango"])

# 3. Add a new fruit with its price to the dictionary.

my_dict["Pineapple"] = 300
print(my_dict)

my_dict.update({"Chickoo": 30})
print(my_dict)

# 4. Update the price of an existing fruit.

my_dict.update({"Chickoo": 1000})
print(my_dict)

# 5. Remove a fruit from the dictionary.

my_dict.pop("Chickoo")
print(my_dict)

# 6. Print all the keys of your dictionary.

print(my_dict.keys())

# 7. Print all the values of your dictionary.

print(my_dict.values())

# 8. Print all key-value pairs using a loop.

for key,value in my_dict.items():
    print(key,value)

# 9. Check if a certain fruit exists in the dictionary.

# fruit = "Orange"
#
# for key,value in my_dict.items():
#     if key == fruit :
#         print(f"{key} Fruit Exists in dictionary")
#     else:
#         print(f"{key} Not Present")

# alternative

fruit = "Orange"

if fruit in my_dict:
    print(f"{fruit} Fruit Exists in dictionary")
else:
    print(f"{fruit} Not Present")
