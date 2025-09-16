# Power of 2 Table
# Print powers of 2 up to 2¹⁰ (1, 2, 4, 8…).

N = int(input("Enter a number : "))

for i in range(0,N+1):
    print(2**i)


for i in range(0,11):
    print(f"2 ** {i} = {2**i}")