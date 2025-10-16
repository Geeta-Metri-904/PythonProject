# Check if the user can log in based on correct username and password.

# I/p
# username = "admin"
# password = "1234"

# O/p
# ✅ Login Successful
# For the Fail condition Other O/P = ❌ Invalid Credentials

username = "admin"
password = "1234"

name = input("Enter a username : ")
pswrd = input("Enter a password : ")

if name == username and pswrd == password :
    print("✅ Login Successful")
else:
    print("❌ Invalid Credentials")