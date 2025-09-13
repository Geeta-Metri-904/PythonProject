# A year is a leap year if it's divisible by 4,
# but years divisible by 100 are not leap years unless they are also divisible by 400

# user input - year -int
# o/p - str or int

year = int(input("Enter a Year : "))

if ( year % 4 == 0 and year % 100 != 0 ) or ( year % 400 == 0 ):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")