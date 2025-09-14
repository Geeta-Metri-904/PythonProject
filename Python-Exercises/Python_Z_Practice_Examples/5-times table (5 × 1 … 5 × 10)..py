# Print the 5-times table (5 × 1 … 5 × 10).

# for i in range(1,51):
#     if i % 5 == 0:
#         multiplier = i //5
#         print(f"5 * {multiplier} = {i}")

for i in range(0,51,5):
    multiplier = i // 5
    print(f"5 * {multiplier} = {i}")