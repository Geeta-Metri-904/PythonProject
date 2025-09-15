# Sum of Even Numbers
# Ask the user for a number N.
# Find and print the sum of all even numbers from 1 to N.

N = int(input("Enter a number : "))
total = 0
for i in range(1, N + 1):
    if i % 2 == 0:
        total += i
print(total)

N = int(input("Enter a number : "))
total = 0
for i in range(2, N + 1, 2):
    total = total + i
print(total)

N = int(input("Enter a number : "))
i = 1
total = 0
while i <= N:
    if i % 2 == 0:
        total += i
    i = i + 1
print(total)