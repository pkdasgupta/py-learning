# Program to implement Operator Overloading in Python

class MyNum:
    def __init__(self, num):
        self.num = str(num)

    def __add__(self, other):
        s = 0
        for k in list(self.num + other.num):
            s += int(k)
        return s

    def __str__(self):
        return self.num

    def __len__(self):
        return len(self.num)


n1 = MyNum(200)
n2 = MyNum(700)

print(f"\n In Current Context : {n1} + {n2} = {n1 + n2} \n(Sum of each digit in both numbers)")

print(f"\n{n1} is a {len(n1)} digit number.")

