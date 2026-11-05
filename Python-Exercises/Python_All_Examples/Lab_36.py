# Largest of Three Numbers – Find the largest among three numbers.

number1 = int(input("Enter First Number"))
number2 = int(input("Enter Second Number"))
number3 = int(input("Enter Third Number"))

if number1 > number2 and number1 > number3:
    print(f"{number1} is largest among three numbers")
elif number2 > number1 and number2>number3:
    print(f"{number2} is largest among three numbers")
else:
    print(f"{number3} is largest among three numbers")

