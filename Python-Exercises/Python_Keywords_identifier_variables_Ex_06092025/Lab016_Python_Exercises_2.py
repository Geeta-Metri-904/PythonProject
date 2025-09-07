# 21. What will be the output of the following code?
x = 10
y = "10"
print(x == y)
print(x == int(y))
# Output: False
# True

# 22. Which of the following are valid identifiers in Python?
# myVar, _count, class, total_sum, 1number
# Valid: myVar, _count, total_sum
# Invalid: class (keyword), 1number (cannot start with digit)

# 23. What happens if you assign a value to the same variable multiple times?
x = 5
x = 10
print(x)
# Output: 10 (latest value overrides old one)

# 24. Predict the output:
x = "Python"
y = "Programming"
print(x + y)
# Output: PythonProgramming (no space added)

# 25. Predict the output:
a = 5
b = 2
print(a / b)
print(a // b)
# Output:
# 2.5
# 2

# 26. Which keyword in Python is used to define a function? Can you use it as a variable name?
# Keyword: def
# Cannot use 'def' as variable name → SyntaxError
# Example: def_ = 10 (valid workaround)

# 27. Python is case-sensitive. Prove it by creating two variables Var and var.
Var = 100
var = 200
print(Var, var)
# Output: 100 200

# 28. Predict the output:
x = True
y = False
print(x + y)
print(x * 10)
# Output:
# 1
# 10

# 29. What is the type of the result when you multiply an integer with a float?
print(type(10 * 2.5))
# Output: float

# 30. Is None the same as 0 in Python? Try comparing them.
print(None == 0)
# Output: False

# 31. Create a variable pi with value 3.14159. Round it to 2 decimal places.
pi = 3.14159
print(round(pi, 2))
# Output: 3.14

# 32. Which of the following are Python keywords?
# try, Test, global, lambda, None
# Valid keywords: try, global, lambda, None
# Invalid: Test

# 33. Write a program to check if a given variable is of type list.
my_list = [1, 2, 3]
print(isinstance(my_list, list))
# Output: True

# 34. What happens if you use an uninitialized variable in Python?
# print(my_value)
# Output: NameError: name 'my_value' is not defined

# 35. What is the output?
a = "10"
b = 10
print(a + str(b))
print(int(a) + b)
# Output:
# 1010
# 20

# 36. Can you reassign a variable from one datatype to another?
x = 100
x = "Hundred"
print(x)
# Output: Hundred
# Explanation: Python is dynamically typed

# 37. What is the output?
x = None
print(x == False)
print(x == None)
print(x is None)
# Output:
# False
# True
# True (preferred way to compare with None)

# 38. Which datatype is mutable and which is immutable among these?
# list → mutable
# tuple → immutable
# string → immutable

# 39. What is the difference between 'is' and '==' in Python?
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b) # True (values equal)
print(a is b) # False (different objects)
# Note: 'is' checks identity, '==' checks values

# 40. What happens if you declare a variable inside quotes, like 'x = 10'?
# It is just a string, not code execution.
# Example: 'x = 10'
# print(x) → NameError
# Only works if executed with exec(), which is rarely used.