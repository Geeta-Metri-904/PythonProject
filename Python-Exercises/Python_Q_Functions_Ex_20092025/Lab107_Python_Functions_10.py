def sum_three(a=1,b=1,c=1):
    return a+b+c

result_1 = sum_three()
print(result_1)

result_2 = sum_three(1)
print(result_2)

result_3 = sum_three(1,2)
print(result_3)

result_4 = sum_three(1,2,3)
print(result_4)

result_5 = sum_three(1,2,3,4)
print(result_5)  # TypeError: sum_three() takes from 0 to 3 positional arguments but 4 were given
