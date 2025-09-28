student_inform = {
    "name": "Geeta",
    "age": 23,
    "address": "KA"
}

print(student_inform["name"])
print(student_inform["age"])
print(student_inform["address"])

student_inform["age"] = 100
print(student_inform)

student_inform_1 = dict(name = "Geeta", age = 23, address = "KA")
print(student_inform_1)


student_inform_2 = {
    "name": "Geeta",
    "age": 23,
    "address": {
        "Home-address": "ND",
        "Office-address": "KA"
    }
}