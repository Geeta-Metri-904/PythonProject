#1. Write a Python program to store your name in a variable and print it.
name = "John"
print(name)
# Output: John

#2. Declare two variables x = 10 and y = 20, then print their sum.
x = 10
y = 20
z = x + y
print(z)
# Output: 30

#3. What will be the datatype of the variable a = 10.5?
a = 10.5
print(type(a))
# Output:

#4. Create a variable to store your age and check its type using type().
age = 24
print(type(age))
# Output:

#5. Assign a string '100' to a variable and convert it into an integer.
x = "100"
y = int(x)
print(y)
# Output: 100

#6. Write a program that swaps the values of two variables without using a third variable.
x = 5
y = 10
x, y = y, x
print(x, y)
# Output: 10 5

#7. What will happen if you use a reserved keyword like 'for' as a variable name?
for = 7 # SyntaxError: invalid syntax

#8. Create three variables in one line to store 10, 20, and 30.
x, y, z = 10, 20, 30
print(x, y, z)
# Output: 10 20 30

#9. Take two variables: one integer and one float. Add them and print the result with its datatype.
x = 3
y = 4.5
z = x + y
print(z)
print(type(z))
# Output: 7.5

#10. Assign the same value 50 to three different variables in a single line.
x = y = z = 50
print(x, y, z)
# Output: 50 50 50

#11. What is the output of the following code?
x = "5"
y = 5
print(x * y)
# Output: 55555

#12. Check if 'True' (string) and True (boolean) are the same datatype.
print(type("True")) #
print(type(True)) #

#13. Write a program to take user input for a name and print 'Hello, '.
x = input("Please Enter your Name: ")
print("Hello,", x)

#14. Create a variable with value None. What will be its datatype?
x = None
print(type(x))
# Output:

#15. What is the difference between '=' and '==' in Python?
#= is used for assignment.
#== is used for comparison.

#16. Which one of these is a valid variable name?
#Valid: my_var, value2
#Invalid: my-var, 2value

#17. Create a variable with a float value and convert it into an integer.
x = 5.6
y = int(x)
print(y)
# Output: 5

#18. What happens if you divide an integer by zero in Python?
x = 3/0
# ZeroDivisionError: division by zero

#19. Store your first name and last name in two variables, then print them together with a space.
firstname = "Geeta"
lastname = "Test"
print(firstname, lastname)
# Output: Geeta Test

#20. Write a program that prints the datatype of multiple values.
print(type("Hello")) #
print(type(100)) #
print(type(100.5)) #
print(type(True)) #
print(type([1,2,3])) #
print(type((1,2,3))) #
print(type({1,2,3})) #
print(type({"a":1,"b":2})) #