student_inform_1 = {
    "name": "Geeta",
    "age": 23,
    "address": {
        "Home-address": "ND",
        "Office-address": "KA"
    }
}

student_inform_2 = {
    "name": "Pooja",
    "age": 23,
    "address": {
        "Home-address": "ND",
        "Office-address": "KA"
    }
}


student_list = [student_inform_1,student_inform_2]
print(student_list)
print(student_list[0])
print(student_list[1])
# print(student_list[2]) # IndexError: list index out of range
print("--------------------------------------")
print(student_list[0]["name"])
print(student_list[0]["age"])
print(student_list[0]["address"])
print(student_list[0]["address"]["Home-address"])
print(student_list[0]["address"]["Office-address"])





