# List -> collection of items
# grocery list -> butter, paneer, bread, banana
# 10th Marks --> 90, 80, 34, 12

my_list = [1,2,3]  # same type of data (int)
my_list2 = [1, True, "Geeta", 12.345]

print(my_list)
print(len(my_list))

print(my_list[0])
print(my_list[1])
print(my_list[2])
# print(my_list[3]) # index out of range

my_list[0] = "Geeta"
my_list[1] = "Test"
my_list[2] = "John"
print(my_list)

print("-------------------------------")

for item in my_list:
    print(item)

# l = range(1,11) # range(start, stop-1)
# print(l)
# range also returns list of items from 1 to 10 [ 1,2,3,4,5,6,7,8,9,10]