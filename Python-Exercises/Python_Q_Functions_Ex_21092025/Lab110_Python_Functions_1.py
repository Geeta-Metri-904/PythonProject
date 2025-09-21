global_variable_a = 12

def my_function():
    local_variable_a = 10 # local variable, within the function
    print(local_variable_a)
    print(global_variable_a)

# print(local_variable_a) # NameError: name 'local_variable_a' is not defined. Did you mean: 'global_variable_a'?
print(global_variable_a)
my_function()