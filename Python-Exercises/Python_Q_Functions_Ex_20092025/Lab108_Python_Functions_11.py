# *args --> multiple arguments

def print_mul_arguments(*args):
    # args --> List
    for i in args:
        print(i)

print_mul_arguments("Geeta")
print_mul_arguments("Geeta","Test")
print_mul_arguments(10,True,False,"Geeta")
print("--------------------------")
print_mul_arguments()