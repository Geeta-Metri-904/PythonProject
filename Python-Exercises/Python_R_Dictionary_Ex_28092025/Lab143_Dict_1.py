my_dict = {
    "Name": "Geeta",
    "Age": 24,
    "Role": "QA",
    "Experience": 6
}

print(my_dict)
print(my_dict["Role"])

my_dict["Role"] = "Manual Tester"
print(my_dict)

del my_dict["Age"]
print(my_dict)

for key, value in my_dict.items():
    print(key, "---->", value)

print("Age" in my_dict)
print("Role" in my_dict)