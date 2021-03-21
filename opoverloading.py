# Program to implement Operator Overloading in Python

class MyNum:
    def __init__(self, num):
        self.num = str(num)

    def __add__(self, other):
        s = 0
        for k in list(self.num + other.num):
            s += int(k)
        return s

    def __mul__(self, other):
        m = 1
        for x in list(self.num + other.num):
            m *= int(x)

        return m

    def __str__(self):
        return self.num

    def __len__(self):
        return len(self.num)


n1 = MyNum(111)
n2 = MyNum(111)

print(f"\n In Current Context : {n1} + {n2} = {n1 + n2} \n(Sum of digits in both numbers)")

try:
    print(f"\n In Current Context : {n1} * {n2} = {n1 * n2} \n(Product digits in both numbers)")
except Exception as e:
    print(e)

print(f"\n{n1} is a {len(n1)} digit number.")
