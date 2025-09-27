my_list = [1,2,3]

# Indexing

print("element at the index 0 - ", my_list[0])
print("element at the index 1 - ", my_list[1])
print("element at the index 2 - ", my_list[2])

# append()  --> Append object to the end of the list
my_list.append(4)
my_list.append(5)
print(my_list)

# extend()  --> Append a new list
my_list.extend([7,2,8,10])
print(my_list)

# insert()
my_list.insert(1,"Geeta")
print(my_list)
print(len(my_list)) # 9


my_list.insert(0,0)
print(my_list)
print(len(my_list)) # 10

# [1, 'Geeta', 2, 3, 4, 5, 7, 8, 9]
# 9
# [0, 1, 'Geeta', 2, 3, 4, 5, 7, 8, 9]
# 10
# Index 0 currently has the value 1.
# insert(0, 0) will put 0 at index 0.
# The previous element (1) and all others move one position to the right.
# Notice the list grows by 1 element, because insert adds a new element,
# it doesn’t overwrite.
# ✅ So the length increases from 9 → 10.

my_list[1] = "Amit"
print(my_list)

# remove()
my_list.remove("Amit")
print(my_list) # ValueError: list.remove(x): x not in list - Amit is not there in my list


print("---------------------------------------------------------------")

my_copy_list = my_list.copy()
print(my_list)
print(my_copy_list)

print("---------------------------------------------------------------")

my_copy_list.remove("Geeta")
my_list.remove("Geeta")

my_copy_list.sort()

print(my_list)
print(my_copy_list)
