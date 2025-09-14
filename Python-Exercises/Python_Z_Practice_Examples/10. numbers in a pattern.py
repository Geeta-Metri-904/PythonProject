# Print numbers in a pattern:

        # 1
        # 12
        # 123
        # 1234

# num = ""
# for i in range(1,5):
#     num = num + str(i)
#     print(num)

for i in range(1, 5):          # rows: 1 to 4
    num = 0
    for j in range(1, i + 1):  # numbers in each row
        num = num * 10 + j     # shift digits left and add new number
    print(num)
