import math

# Area of Circle
# I/P - float
# O/P - Str

radius = float(input("Enter radius : "))

# area = 3.14 * (radius ** 2)
area = math.pi * (pow(radius,2))
print("Area of Circle is : ", area)
print(f"Area of Circle is : {area:.2f}")

# Area of Circle is :  314.98699999999997
# Area of Circle is : 314.99
