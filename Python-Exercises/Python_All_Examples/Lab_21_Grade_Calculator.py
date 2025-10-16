# Grade Calculator

# A : 90-100
# B : 80-89
# C : 70-79
# D : 60-69
# F : 0-59

# User Inputs - score - int
# O/p - str

score = int(input("Enter the score : ").strip())

# if score >= 0 and score =< 100: # 0 < score < 100
#     print("Enter a valid score")

if score > 100 or score <= -1:
    print(" You can't get a grade !!! ")
else:
    if score >= 90 and score <= 100:
        print("Your Grade is A")
    elif score >= 80 and score <= 89:
        print("Your Grade is B")
    elif score >= 70 and score <= 79:
        print("Your Grade is C")
    elif score >= 60 and score <= 69:
        print("Your Grade is D")
    else:
        print("Your Grade is F")

# float, str - try catch