# Count Digits

def count_digits(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

print(count_digits(7890))  # 4
