# Escape Sequence

# '' or ""

c = 'C'
c1 = "C"

# Where this r concept will be used ?
# r is raw

#dir_3 = 'C:\Geeta\n.txt'
#print(dir_3)
# output :
#C:\Geeta
# .txt

dir = r'C:\Geeta\n.txt'
dir_1 = r"C:\Geeta\n.txt"
dir_2 = "C:\Geeta\t.txt"
print(dir) # C:\Geeta\n.txt
print(dir_1) # C:\Geeta\n.txt
print(dir_2) # C:\Geeta	.txt

print("Geeta'Test") #Geeta'Test
print("Geeta'u\t\ta") # Geeta'u		a
print(r"Geeta'u\t\ta") # Geeta'u\t\ta