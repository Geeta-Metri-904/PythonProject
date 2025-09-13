# Write a program to take a user age and let him know if he can go the club
# 21

# Logic Building Formula

# Step1
# User input i/p -> data type -> int
# o/p -> string -> user if he can go or not.

# Step2 : Rough Logic ( brute force )
# age > 21 -> print can go
# age < 21 -> print can't go

# Step3 : write the logic

age = int(input("Enter your age\n "))
print(age)

if age >= 21:
    print("Yes you can go to Club!")
else:
    print("No you can't go to Club!")

print("You can go to the club" if age >= 21 else "No you can't go to club")
print("You can go to the club" if int(input("Enter your age ")) >= 21 else "No you can't go to club")

# Step4 : Check for the edge cases

# we should consider edge cases such as :
# Negative ages or extremely high values -> program will break
# Non-numeric input -ABC
# Age which is valid in nature > 130

# Step 5 : Optimize the code
# Handle all the edge cases
