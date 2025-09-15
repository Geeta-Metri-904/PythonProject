# Sum of 1 to N
# Take an integer N from the user.
# Find and print the sum of all numbers from 1 to N.

# N = int(input("Enter a number : "))
#
# sum = 0
# for i in range(1,N+1):
#     sum = sum + i
# print(sum)

N = int(input("Enter a number : "))

i = 1
total = 0
while i <= N:
    total += i
    i += 1
print(total)
