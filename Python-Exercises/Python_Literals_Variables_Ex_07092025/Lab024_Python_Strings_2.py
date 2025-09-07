name = "This is my name"
print(type(name))
#name = name+1 # TypeError: can only concatenate str (not "int") to str
name = name + str(1) # output is name1
print(name)

first_name = "Geeta"
last_name = "Doe"
full_name = first_name+last_name
print(full_name) # GeetaDoe
print(type(full_name)) # <class 'str'>

full_name_1 = first_name+" "+last_name
print(full_name_1) # Geeta Doe
print(type(full_name_1)) # <class 'str'>
