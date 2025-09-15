# Create a program to sum of three numbers from the user input
# if user doesn't enter any number, use default as 100, 200, 300

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

def sum_of_three_num(num1=100,num2=200,num3=300):
    return num1+num2+num3

sum = sum_of_three_num(num1,num2,num3)
print("Sum of Three Numbers is : ", sum)

total = sum_of_three_num()
print("Sum of Three Numbers is : ", total)

result2 = sum_of_three_num()
result2 = sum_of_three_num(10)
result2 = sum_of_three_num(10,20)
result2 = sum_of_three_num(10,20,30)
print(result2)
