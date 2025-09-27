t = tuple()
print(t)

# Conversion List to Tuple
t1 = tuple(["Geeta", "John", "Test"])
print(t1)

hero1 = ("Batman", "Bruce")
hero2 = ("Wonder Woman", "Diana")
new_tuple = (hero1,hero2)
print(new_tuple) # (('Batman', 'Bruce'), ('Wonder Woman', 'Diana'))
print(new_tuple[0]) # ('Batman', 'Bruce')
print(new_tuple[0][0]) # Batman
print(new_tuple[1][1]) # Diana