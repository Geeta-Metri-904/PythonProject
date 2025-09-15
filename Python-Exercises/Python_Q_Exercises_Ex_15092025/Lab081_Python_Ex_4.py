# Even Numbers up to 50
# Print all even numbers from 1 to 50.
# Use a loop and an if condition.

for i in range(1, 51):
    if i % 2 == 0:
        print(i)

for i in range(2,51,2):
    print(i)

i = 1
while i <= 50:
    if i % 2 == 0:
        print(i)
    i += 1
