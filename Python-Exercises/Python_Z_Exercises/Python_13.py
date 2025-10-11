text = "Python"
print(text[0])   # P
print(text[-1])  # n


s = "  hello world  "
print(s.upper())      # HELLO WORLD
print(s.lower())      # hello world
print(s.strip())      # hello world
print(s.replace("world", "Python"))  # hello Python
print(s.title())      # Hello World


sentence = "apple,banana,orange"
fruits = sentence.split(",")
print(fruits)           # ['apple', 'banana', 'orange']

joined = "-".join(fruits)
print(joined)           # apple-banana-orange
