# Create a program to sum of three numbers from the user input
# if user doesn't enter any number, use default as 100, 200, 300

# Logic Building
# input

num1 = int(input("Enter a first number : "))
num2 = int(input("Enter a second number : "))
num3 = int(input("Enter a third number : "))

def sum_of_three_numbers(a=100, b=200, c=300):
    return a + b + c

result = sum_of_three_numbers(num1, num2, num3)
print("user sum : ", result)
result_1 = sum_of_three_numbers()
print("default : ", result_1)
