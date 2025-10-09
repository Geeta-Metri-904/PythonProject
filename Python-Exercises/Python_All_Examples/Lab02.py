print("Hello world")
# print(self, *args, sep = ' ', end = '\n', file=None):

# self - ignore(oops)
# *args - unlimited number of comma separated arguments
print("Geeta", 123, "Test", True, 3.14, "John")

print("Geeta", 123, "Test", True, 3.14, "John", sep = "-")
print("Geeta", 123, "Test", True, 3.14, "John", sep = "*")
print("Geeta", 123, "Test", True, 3.14, "John", sep = "_")

# seperator cannot be at the starting..
# it needs unlimited number of comma separated arguments at the first

print("Geeta", 123, "Test", True, 3.14, "John", sep = "_", end = "_____________")
print("Geeta", 123, "Test", True, 3.14, "John", sep = "*")

# IndentationError: unexpected indent
print("Geeta", 123, "Test", True, 3.14, "John", sep = "_", end = "_____________")

print("Geeta", 123, "Test", True, 3.14, "John", sep = "*", end = "_")


