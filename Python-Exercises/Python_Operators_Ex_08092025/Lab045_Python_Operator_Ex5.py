a = 10
b = 5
c = 2

result = (a + b) * c // b - (a % b)
print(result)

# BODMAS
# Brackets, Orders (powers and roots), Division, Multiplication, Addition, and Subtraction
# *   /   //   %
# have the same precedence.
# 👉 They are evaluated from left to right (this is called associativity).

# (a+b) --> (10+5) --> 15
# (a%b) --> (10%5) --> 0
# (a + b) * c // b - (a % b) --> 15*c//b-0 --> 15*2//5 --> 30//5 --> 6