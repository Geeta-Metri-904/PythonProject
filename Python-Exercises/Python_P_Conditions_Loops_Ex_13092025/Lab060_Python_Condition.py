# Program to find the Max between 3 Numbers

# User Inputs --> num1,num2,num3 -> int
# o/p -> int or sting with max number

# Syntax
"""
if condition_1:
   print("do 1")
elif condition_2:
   print("do 2")
elif condition_3:
   print("do 3")
else:
   print("do for else")
"""
# When we have multiple condition then only we use else-if or elif

num1 = int(input("Enter a first number: "))   # 5, # 10
num2 = int(input("Enter a second number: "))  # 3, # 12
num3 = int(input("Enter a third number: "))   # 2, # 11

# 5 > 3 and 5 > 2 --> 5
# num1 > num2 and num1 > num3 --> num1

# 12 > 10 and 12 > 11 --> 12
# num2 > num1 and num2 > num3 --> num2

# num3

if num1 > num2 and num1 > num3:
    print("Max is", num1)
elif num2 > num1 and num2 > num3:
    print("Max is", num2)
else:
    print("Max is", num3)




