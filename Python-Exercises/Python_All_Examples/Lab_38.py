# Sum of N Numbers – Find the sum of numbers from 1 to N.

N = int(input("Enter a number : "))

k = 0
for i in range(1, N+1):
    k = i + k

print(k)