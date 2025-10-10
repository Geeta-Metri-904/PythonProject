prog = str(input("Enter a string including digits : "))
# Input :  a1b2
# Output : a2b1

string = []
digit = []

for char in prog:
    if char.isalpha() == True:
        string.append(char)
    else:
        digit.append(char)

print(string)
#print(digit)
digit.reverse()
print(digit)

z = []
for s,d in zip(string, digit):
    z.append(s+d)
    #print(z)

s = "".join(z)
print(s)
