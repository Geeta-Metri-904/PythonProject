# Program - if age > 18 - allowed to vote
# else -> not allowed too

user_input = int(input("Enter your age: "))

print("Allowed to Vote" if user_input > 18 else "Not allowed to Vote")

print(" ------------------------------------- ")

user_input_1 = int(input("Enter your age: "))

if user_input_1 > 18:
    print("You are allowed to vote")
else:
    print("You are not allowed to vote")