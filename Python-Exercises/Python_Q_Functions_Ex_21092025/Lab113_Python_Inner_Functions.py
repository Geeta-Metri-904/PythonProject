def outer_function():
    var1 = 30 # local

    def inner_function():
        var2 = 90
        print(var1) # this can use var1 value

    def inner_function2():
        print(var1) # this can use var1 value

    inner_function()
    inner_function2()
    # print(var2) --> not allowed/cannot call

outer_function()
# inner_function() --> we cannot call inner function outside outer

# o/p
# 30
# 30