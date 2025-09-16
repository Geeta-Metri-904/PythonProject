# Count Digits
# count_digits(n) returns how many digits are in the positive integer n
# (use math/loops, not strings)

num = int(input("Enter a number: "))

def count_digits(n):
    count = 0
    while n > 0:          # repeat until n is 0
        n //= 10          # drop the last digit
        count += 1        # count each digit
    return count

print(count_digits(num))

