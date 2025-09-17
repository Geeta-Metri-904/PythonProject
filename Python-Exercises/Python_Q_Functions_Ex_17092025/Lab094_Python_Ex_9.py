# Maximum of Three

def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c

print(max_of_three(3, 9, 5))  # ➜ 9