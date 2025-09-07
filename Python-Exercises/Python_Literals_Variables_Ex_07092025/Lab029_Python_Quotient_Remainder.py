# Take a 2 input from the user
# Print the Quotient and Remainder
# 15 -> num1
# 2 -> num2
# Q-7 and R-1

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
Div = num1 / num2
print("The Division is", Div) # The Division is 7.5
Quotient = num1 // num2 # Using floor division to get the quotient
Remainder = num1 % num2 # Using modulo to get the remainder
print("The quotient is", Quotient) # The quotient is 7
print("The remainder is", Remainder) # The remainder is 1

