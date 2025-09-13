# Find the maximum between two numbers (3,4) -> 4

# Logic Building Formula

# 1. User Inputs -> two integers
# 2. o/p -> int 1 which ever is greater max number it will return
# 3. 31.54 or 45.67 - float

num1 = float(input("Enter a first number: "))
num2 = float(input("Enter a second number: "))

if num1 >= num2:
    print(f"Max is {num1}")
else:
    print(f"Max is {num1}")

# Edge Cases :
# Numbers are Equal num1 == num2 - Handled
# String --> ABC, ten -> try and except
# Negative Values


