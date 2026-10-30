def reverse_string(s):
    empty_str = ""
    for char in s:
        empty_str= char + empty_str
    return empty_str

print(reverse_string("playwright"))