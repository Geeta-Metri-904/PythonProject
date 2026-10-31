class Calculator:
    num = 100

    def getdata(self):
        print("I am now executing as method in class")

obj = Calculator()
obj.getdata()
print(obj.num)