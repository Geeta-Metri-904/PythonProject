# Write a Python program to calculate the
# area of a circle given its radius using the formula
# ``` area=π×r^2``` ( Take pie as 3.14)

# Logic Building Formula

# step1 - Figure out the inputs and output
# input -> r -> data type - float
# pi = 3.14
# power -> pow or ** - any
# o/p - float - area, print area

# step2
# rough logic = area= 3.14 * pow(r,2)

# step3
radius = float(input("Enter the radius of the circle\n "))
print(radius)
area = 3.14 * radius * radius
# area = 3.14 * (radius**2)
print("The area of the circle is:", area)
print(f"The area of the circle is: {area}")

print( "---------------------")

area1 = 3.14034729875237 * radius * radius
# area1 = 3.14 * (radius**2)
print("The area of the circle is:", area1)
print(f"The area of the circle is: {area1}") # 314.034729875237
print(f"The area of the circle is: {area1:.2f}") # 314.03 - Two decimal formatting - 2f


print( "---------------------")

import math
print(math.pi)
print(math.pow(radius, 2))
area = math.pi * math.pow(radius, 2)
print("The area of the circle is:", area)

print(" ---------------------- ")

print(3.14 * radius **2 )
print(3.14 * float(input("Enter the radius of the circle\n ")) ** 2)

print(math.sin(90))
print(math.cos(90))
print(math.tan(90))