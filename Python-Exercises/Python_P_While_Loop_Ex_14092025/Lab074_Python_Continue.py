# pass - can be used in the statement, functions, class and objects
# continue -  skip

for number in range(10): # number - 0 to 9 - 10 times
    if number%2 == 0:
        continue
    else:
        print(number)

# | i | Condition | O/P
# | 0 | 0%2 == 0 - True | O/P - continue - skip No O/P
# | 1 | 1%2 == 0 - False | O/P - 1
# | 2 | 2%2 == 0 - True | O/P - continue - skip No O/P
# | 3 | 3%2 == 0 - False | O/P - 3
# | 4 | 4%2 == 0 - True | O/P - continue - skip No O/P
# | 5 | 5%2 == 0 - False | O/P - 5
# | 6 | 6%2 == 0 - True | O/P - continue - skip No O/P
# | 7 | 7%2 == 0 - False | O/P - 7

# output : Odd Numbers
# 1
# 3
# 5
# 7
# 9