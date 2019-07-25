# Q1
class Bike:

    def __init__(self, initX, initY):
        self.color = initX
        self.price = initY


testOne = Bike("blue", 89.99)
testTwo = Bike("purple", 25.0)

# Q2
class AppleBasket:
    def __init__(self, initX, initY):
        self.apple_color = initX
        self.apple_quantity = initY

    def increase(self):
        self.apple_quantity = self.apple_quantity + 1
        return self

    def __str__(self):
        return "A basket of " + str(self.apple_quantity) + " " + self.apple_color + " apples."

# Q3
class BankAccount:

    def __init__(self, initX, initY):
        self.name = initX
        self.amt = initY

    def __str__(self):
        return "Your account, " + self.name + ", has " + str(self.amt) + " dollars."


t1 = BankAccount("Bob", 100)
