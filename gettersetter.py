# Create a class Employee and add salary and increment properties to it.
# Write a method SalaryAfterIncrement method with a @property decorator
# with a setter which changes the value of increment based on the salary.

class Employee:
    sal = 10000
    inc = 800

    @property
    def salAfterInc(self):
        return self.sal + self.inc

    @salAfterInc.setter
    def salAfterInc(self, ival):
        self.inc = ival - self.sal


e = Employee()
print(f"\n Current Salary : {e.sal}")
print(f"\n Salary after initial increment : {e.salAfterInc}")
e.salAfterInc = 12800
print(f"\n Revised Increment : {e.inc}, Revised Salary : {e.salAfterInc}")
