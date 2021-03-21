# Program to implement Operator Overloading in Python

class MyNum:
    def __init__(self, num):
        self.num = str(num)

    def __add__(self, other):
        s = 0
        for k in list(self.num + other.num):
            s += int(k)
        return s


n1 = MyNum(26)
n2 = MyNum(71)

print(n1 + n2)
