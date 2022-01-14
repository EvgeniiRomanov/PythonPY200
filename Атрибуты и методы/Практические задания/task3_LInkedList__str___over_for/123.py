class Calculator:
    value1 = 11

    def __init__(self, value = int):
        self.value = value

    #@staticmethod
    def add(self, a, b):
        return a + b

    @staticmethod
    def mul(a, b):
        return a * b


print(Calculator.add(5, 6, 7))
print(Calculator.value1)

x = Calculator(8)
print(x.value)
print(x.add(7, 7))
#x.value1 = "red"
print(x.value1)
print(Calculator.value1)
y = Calculator(100)
print(y.value, y.value1)
y.value1 = "Yellow"
z = Calculator(600)
Calculator.value1 = "Black"


print(y.value, y.value1)
print(x.value, x.value1)
print(z.value, z.value1)
print(z.mul(50, 30))

print(Calculator.mul(60, 20))
