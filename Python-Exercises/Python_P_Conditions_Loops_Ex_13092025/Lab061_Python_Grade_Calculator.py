# Write a program that calculates and displays the
# letter grade for a given numerical score
# (e.g., A, B, C, D, or F) based on the following grading scale:

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

# Logic Building Formula
# User I/p - score or mark -> int
# o/p - str - A or B

# Rough Logic

# score >= 90 and score <= 100 --> "A"
# Score >= 80 and Score <= 89 --> "B"
# Score >= 70 and Score <= 79 --> "C"
# Score >= 60 and Score <= 69 --> "D"
# Score 0-59 --> "F"

Score = int(input("Enter a score :"))

if Score >= 90 and Score <= 100:
    print("Your Grade is A")
elif Score >= 80 and Score <= 89:
    print("You have opted Grade B")
elif Score >= 70 and Score <= 79:
    print("You have opted Grade C")
elif Score >= 60 and Score <= 69:
    print("You have opted Grade D")
elif Score >= 100 or Score <= -1:
    print("You can't get a grade!!")
else:
    print("You have opted Grade F")

# Edge Cases
# Negative Chars
# Special Characters
# Strings
# above 100
# less than 100
