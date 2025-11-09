a = {1, 2, 3}
b = {3, 4, 5}

# Union ( | )
print(a.union(b))  # {1, 2, 3, 4, 5}
print(a | b)

# Intersection ( & )
print(a.intersection(b))
print(a & b)  # {3}

# Difference between two elements
# elements of a not in b
print(a - b)  # {1, 2}

# Symmetric Difference
print(a ^ b)  # {1, 2, 4, 5}
