# Count how many numbers between 1 and 100 are divisible by 7.
count = 0
for i in range(1, 101):
    if i % 7 == 0:
        print(i)
        count = count + 1
print(count)
