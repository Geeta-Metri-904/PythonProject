# A year is a leap year if it's divisible by 4,
# but years divisible by 100 are not leap years
# unless they are also divisible by 400

# user input - year -int
# o/p - str or int

# The year is multiple of 400
# The year is a multiple of 4 and not a multiple of 100

def check_leap_year(year):
    if ( year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 ):
        return True
    else:
        return False

year = 2024

if check_leap_year(year):
    print("Yes")
else:
    print("No")