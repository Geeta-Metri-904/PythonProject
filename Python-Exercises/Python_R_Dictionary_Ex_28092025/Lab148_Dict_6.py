# Write a program to find a Frequency of a char in a string

string = "automation"
# string = input("Enter a input e.g automation")

# answer : {a = 2, u = 1, t = 2, o = 2, m = 1, i =1 , n=1}

char_count = {}

# Logic Building
# I/p - string
# o/p - dict

for char in string:
    char_count[char] = char_count.get(char,0) + 1
    #print(char_count[char])

print(char_count) # {'a': 2, 'u': 1, 't': 2, 'o': 2, 'm': 1, 'i': 1, 'n': 1}


