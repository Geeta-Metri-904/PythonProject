cities = ("London","Paris", "Tokyo", "Los Angeles")
print("Paris" in cities) # True
print("New Delhi" in cities) # False

t = (12,34,56)
# t.append(12) # AttributeError: 'tuple' object has no attribute 'append'
my_list = list(t)
my_list.append(4)
t = tuple(my_list)
print(t)  # (12, 34, 56, 4)

ENV_API_URLs= tuple(["abc.com/get", "xyz.com/post", "qwe.com/put"])
print(ENV_API_URLs)  # ('abc.com/get', 'xyz.com/post', 'qwe.com/put')