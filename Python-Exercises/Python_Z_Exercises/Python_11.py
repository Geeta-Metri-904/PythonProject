s = "Python"
print(s[:])
print(s[0:])
print(s[1:])
print(s[2:])
print(s[:4]) # 0 to n-1

print("----------------------------")
# Strings are immutable
s = "hello"
# s[0] = 'H' # ❌ (error: strings are immutable)
s = 'H' + s[1:]  # ✅ create a new string
print(s)  # "Hello"

a = "Hello"
b = "World"
print(a + " " + b)  # "Hello World"

print("Hi! " * 3)

print(len(a))

text = "I love Python"
print("love" in text)    # True
print("hate" not in text)  # True


name = "Geeta test "
print(name.lower())
print(name.upper())
print(name.title())
print(name.strip())
print(name.replace("t", "e"))
print(name.split())
print(" ".join(["Geeta", "Test"]))
print(name)
print(name.count('t'))
print(name.find('s'))
print(name.startswith("Gee"))

print(name.isalpha())




