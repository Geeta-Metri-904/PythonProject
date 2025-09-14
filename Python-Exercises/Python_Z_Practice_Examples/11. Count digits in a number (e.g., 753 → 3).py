# Count how many digits are in a number (e.g., 753 → 3).

# num = 753
# print(len(str(num)))

num = 753
count = 0

while num > 0:
    num = num // 10
    count = count + 1
print(count)


# | Iteration | num | num // 10 | count |
# | --------- | --- | --------- | ----- |
# | 1         | 753 | 75        | 1     |
# | 2         | 75  | 7         | 2     |
# | 3         | 7   | 0         | 3     |
# | 4         | 0   | -         | stop  |
