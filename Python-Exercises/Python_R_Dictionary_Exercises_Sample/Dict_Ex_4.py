my_dict = {"Mango": 60, "Apple": 200, "Guava": 40, "Orange": 150, "Banana": 20}

# 10. Count the frequency of each character in a given string using a dictionary.

string = "Geeta"
my_dict = {}

for char in string:
    my_dict[char] = my_dict.get(char, 0) + 1

print(my_dict)

'''

Step-by-step example
string = "Geeta"
my_dict = {}

# First iteration: char = 'G'
# 'G' not in my_dict → get('G', 0) returns 0
# 0 + 1 → my_dict['G'] = 1

# Second iteration: char = 'e'
# 'e' not in my_dict → get('e', 0) returns 0
# 0 + 1 → my_dict['e'] = 1

# Third iteration: char = 'e'
# 'e' exists in my_dict with value 1 → get('e', 0) returns 1
# 1 + 1 → my_dict['e'] = 2


✅ So 0 is returned only when the key does not exist yet in the dictionary.

'''


