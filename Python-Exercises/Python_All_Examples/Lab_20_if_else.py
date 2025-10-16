# Find Max between 3 numbers

num1 = int(input("Enter a first number : "))
num2 = int(input("Enter a second number : "))
num3 = int(input("Enter a third number : "))

if num1 >= num2 and num1 >= num3:
    print("Max", num1)
elif num2 >= num1 and num2 >= num3:
    print("Max", num2)
else:
    print("Max", num3)
