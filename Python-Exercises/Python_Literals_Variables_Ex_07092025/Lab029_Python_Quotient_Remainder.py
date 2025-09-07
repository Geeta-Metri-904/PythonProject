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

# python built in function divmod
# In Python, there is a built-in function called divmod(a, b)
# It takes two numbers and returns a tuple → (quotient, remainder)
# divmod() only takes two numbers.
# It’s different from / (division) because it gives you both quotient and remainder in one go

result = divmod(15, 2)
print(result)

# output is Because 15 ÷ 2 = 7 (quotient), remainder 1
# (7, 1)

result_f = divmod(15.5, 2.5)
print(result_f) # (6.0, 0.5)