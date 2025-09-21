def say_hello():
    print("Hello")

say_hello()


# functions with argument, parameters

def greet_by_name(name):
    print("Hello,", name)
    print(f"Hello, {name}")

greet_by_name("Geeta")  # Hello Geeta
greet_by_name(123)  # Hello 123
greet_by_name(3.14)  # Hello 3.14

