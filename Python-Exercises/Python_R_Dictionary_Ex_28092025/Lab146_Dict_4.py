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

student_inform_3 = {
    "name": "Murthy",
    "age": 231,
    "address": {
        "Home-address": "Kerala",
        "Office-address": "Vizag"
    }
}

student_list = [student_inform_1,student_inform_2,student_inform_3]
# print(student_list)

# Print Murthys Office Address

print(student_list[2]["address"]["Office-address"])
# or
print(student_inform_3["address"]["Office-address"])













