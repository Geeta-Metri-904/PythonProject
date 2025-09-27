# def 123():    # identifier rule is failed
#     print("Hi")

def _123():   # valid
    print("Hi")

def _():    # valid
    print("Hi")

def geeta123():    # valid
    print("Hello")

def h():      # valid
    print("Hello")
    print("I am a part of the function h")

print("I am not part of the function h")
