# 2️⃣ Add Two Numbers
#
# Define add_numbers(a, b) that returns the sum of two integers.

a = int(input("Enter a number : "))
b = int(input("Enter a number : "))

def add_numbers(a, b):
    return a+b

sum_total = add_numbers(a,b)
print(f"sum of a and b is {sum_total}")