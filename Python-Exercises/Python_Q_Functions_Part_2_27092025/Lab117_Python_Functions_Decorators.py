def add_extra_security(func):   # function name can change it to anything

    def wrapper():
        print("Before calling the function")
        print("Take all necessary Helmet,Belt,Hand Gloves,Goggles")
        print("-------------------------------")
        func() # driving_scooty or ola_driving
        print("-------------------------------")
        print("After calling the function")
        print("Driving Completed")

    return wrapper() # need to return

@add_extra_security
def ola_driving():
    print("I am driving OLA")

@add_extra_security
def driving_scooty():
    print("Normal Function !!")
    print("I am driving the scooty")

