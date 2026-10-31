class Calculator:
    num = 100 # Class Variables

    # Default Constructor

    def __init__(self,a,b):
        self.firstnumber = a # instance variables
        self.secondnumber = b
        print("I have called automatically when object is created")

    def getdata(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstnumber+self.secondnumber

obj = Calculator(2,3)
print(obj.Summation())

obj1 = Calculator(4,5)
print(obj1.Summation())