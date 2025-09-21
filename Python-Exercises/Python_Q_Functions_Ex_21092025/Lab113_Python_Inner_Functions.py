def outer_function():
    var1 = 30 # local

    def inner_function():
        print(var1) # this can use var1 value

    def inner_function2():
        print(var1)

    inner_function()
    inner_function2()

outer_function()

# o/p
# 30
# 30