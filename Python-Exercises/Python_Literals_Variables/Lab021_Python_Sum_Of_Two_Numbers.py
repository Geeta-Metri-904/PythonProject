# Write a Program to take the 2 user input
# then sum the number
# mul, div

# Logic Building
# Step 1
# I/P -> num1, num2 -> int
# O/P -> sum -> int, sub -> int, div -> float
num1 = int(input("Enter the num 1"))
num2 = int(input("Enter the num 2"))

print(type(num1)) # str
print(type(num2)) # str

# Step 2 / Rough Logic
# Sum +, -, *, /

# str -> int
# int(num1)

#num1 = int(num1)- It will not add/sub/mul/div if you don't convert it to int/float because input will return str
#num2 = int(num2)

# Step 3
sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

print("Sum is -> ", sum)
print("Sub is -> ", sub)
print("Mul is -> ", mul)
print("Div is -> ", div)

"""
print("Sum is -> ", num1 + num2)
print("Sub is -> ", num1 - num2)
print("Mul is -> ", num1 * num2)
print("Div is -> ", num1 / num2)
"""

"""
output : 
Enter the num 1155
Enter the num 25
<class 'int'>
<class 'int'>
Sum is ->  160
Sub is ->  150
Mul is ->  775
Div is ->  31.0

"""