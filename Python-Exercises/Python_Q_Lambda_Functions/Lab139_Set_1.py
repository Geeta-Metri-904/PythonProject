# SET
# Collection of Unique Elements
# {}  --> Parenthesis

list_of_unique_items = {1, 2, 3, 4, 4, 5, 5} # It will remove duplicate elements
print(list_of_unique_items)  # {1, 2, 3, 4, 5}

list1 = [45.2, 33, 33, 45, 21]
set1 = set(list1)
print(set1) # {33, 21, 45, 45.2} No Order

t = ("Google", "Youtube", "Google")
print(t) # ('Google', 'Youtube', 'Google')
set2 = set(t)
print(set2) # {'Google', 'Youtube'}
