set1 = set(["Geeta", "Google", "Geeta"]) # Conversion from list to set
print(len(set1)) # 2

set1 = set(["Geeta", "Google", "Geeta."])
print(len(set1)) # 3

for i in set1:
    print(i)

set1.add("Geetas")
set1.add("Geetas")
print(set1) # {'Geeta', 'Geeta.', 'Geetas', 'Google'}
















