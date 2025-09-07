from Python_Keywords_identifier_variables_Ex_06092025.Lab015_Python_Exercises_1 import firstname

name = "This is my name"
print(type(name))
#name = name+1 # TypeError: can only concatenate str (not "int") to str
name = name + str(1) # output is name1
print(name)

first_name = "Geeta"
last_name = "Doe"
full_name = first_name+last_name
print(full_name)