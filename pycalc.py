# Write a class calculator capable of finding square, cube and the square root of a number.

class Calculator:

    def __init__(self, numval):
        self.numval = int(numval)

    def sq(self):
        return self.numval ** 2

    def cb(self):
        return self.numval * self.sq()

    def sqt(self):
        return self.numval ** 0.5


n = Calculator(9)

print(f"\n Square of {n.numval} = {n.sq()}"
      f"\n Cube of {n.numval} = {n.cb()}"
      f"\n Square Root of {n.numval} = {n.sqt()}")
