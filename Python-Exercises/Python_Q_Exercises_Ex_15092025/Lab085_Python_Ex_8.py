# Factorial
# Take an integer N from the user and calculate N! (factorial)
# (e.g., 5! = 1 × 2 × 3 × 4 × 5).

N = int(input("Enter a number : "))
mul = 1
for i in range(N,0,-1):
    mul = mul * i
print(mul)

N = int(input("Enter a number : "))
mul = 1
for i in range(1,N+1):
    mul = mul * i
print(mul)