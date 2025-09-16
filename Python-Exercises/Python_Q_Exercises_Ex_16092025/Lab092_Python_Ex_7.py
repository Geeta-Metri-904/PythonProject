# Check Even or Odd
# is_even(n) returns True if n is even, otherwise False

num = int(input("Enter a number : "))


def is_even(n):
    return True if n % 2 == 0 else False

# def is_even(n):
#     return n % 2 == 0

Even_or_Odd = is_even(num)
print(Even_or_Odd)
