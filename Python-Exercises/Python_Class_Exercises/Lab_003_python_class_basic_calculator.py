class BasicCalculator:

    def __init__(self, a, b):
        self.number1 = a
        self.number2 = b

    def Addition(self):
        print(f"Addition: {self.number1} + {self.number2} = {self.number1 + self.number2}")
        return self.number1 + self.number2

    def Subtraction(self):
        print(f"Subtraction: {self.number1} - {self.number2} = {self.number1 - self.number2}")
        return self.number1 - self.number2

    def Multiplication(self):
        print(f"Multiplication: {self.number1} * {self.number2} = {self.number1 * self.number2}")
        return self.number1 * self.number2

    def Division(self):
        print(f"Division: {self.number1} / {self.number2} = {self.number1 / self.number2}")
        return self.number1 / self.number2

obj = BasicCalculator(10, 5)
obj.Addition()
obj.Subtraction()
obj.Multiplication()
obj.Division()










