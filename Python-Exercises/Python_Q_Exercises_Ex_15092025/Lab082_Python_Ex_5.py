# Multiplication Table
# Ask the user for a number.
# Print its multiplication table from 1 × num to 10 × num

num = int(input("Enter a number : "))

for i in range(1, 11):
    print(f"{i} * {num} = {i * num}")
