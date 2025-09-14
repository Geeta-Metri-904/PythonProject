for i in range(10):
    if i == 7:
        pass # just pass
        print(i)

# output : 7 -> only 7

"""
 i = 0 -> Nothing printed
 i = 7 -> print 7
"""

for i in range(10):
    if i == 7:
        continue # skip
        print(i)

# Nothing will be executed -  it will skip go to next iteration