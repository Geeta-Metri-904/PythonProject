# Find the first non-repeating character in a string using sets

# swiss --> s - no, w - answer

def first_non_repeating(string):
    for char in string:
        if string.count(char) == 1:
            return char
    return None

print(first_non_repeating("swiss")) # w
print(first_non_repeating("pepper")) # r
print(first_non_repeating("DADA")) # None