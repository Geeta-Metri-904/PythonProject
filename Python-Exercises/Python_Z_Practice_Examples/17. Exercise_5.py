a, b = 36, 60
while b:
    a, b = b, a % b
print("GCD:", a)
