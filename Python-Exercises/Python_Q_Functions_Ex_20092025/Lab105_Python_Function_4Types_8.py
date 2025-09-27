# User Defined Function Types

# 1. They Can't Return --> no return
# 2. They Can Return something
# 3. They have Parameters
# 4. Thet don't have Parameters/Arguments

# 1. They Can't Return --> no return
# No Return Type and No Parameter/Argument - NRNP

def greet():
    print("Hello")

greet()

# 2. They Can Return something
# No Return Type and with Parameter/Argument

def greet_by_name(name):
    print("Hello", name)

greet_by_name("Geeta")

# 3. They have Parameters
# No Return Type and with Default Argument/Positional Argument
# If we don't pass anything will take default value and if pass take passed argument

def say_hello_default_arg(name="Geeta"):
    print("Hello", name.upper())

say_hello_default_arg("Test")
say_hello_default_arg()


def mutliple_args(name1="A", name2 = "B"):
    print("Mul --> ", name1, name2)

mutliple_args()
mutliple_args(name1 = "Geeta")
mutliple_args("Geeta") # it will take first one automatically
mutliple_args(name1="Geeta", name2 = "Test")
mutliple_args(name2 = "Test")

# 4. Thet don't have Parameters/Arguments
# Argument + return Type

def sum_of_two_numbers(a,b):
    return a+b

result = sum_of_two_numbers(4,56)
print(result)  # 60

# function with default argument
def sum_of_two_numbers_with_default(num1 = 100,num2 = 200):
    print("Sum of Two Numbers")
    return num1+num2

result = sum_of_two_numbers_with_default(4,56)
print(result)  # 60
result = sum_of_two_numbers_with_default()
print(result)  # 300





