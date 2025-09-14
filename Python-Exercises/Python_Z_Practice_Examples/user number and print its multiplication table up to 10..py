# Ask the user for a number and print its multiplication table up to 10.

# num = int(input("Enter a number: "))
#
# for i in range(1, num*10 + 1):   # 1 to 10th multiple
#     if i % num == 0:
#         multiplier = i // num
#         print(f"{num} * {multiplier} = {i}")

num = int(input("Enter a number : "))

for i in range(1,11):
        print(f"{num} * {i} = {num*i}")
