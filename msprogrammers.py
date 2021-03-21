# Create a class programmer for storing information of a few programmers working at Microsoft.

import random as r


class Programmer:
    # class attributes
    company = "Microsoft"
    office = "MsBldg"

    def __init__(self, name="YTF", location="TBD", division="TBD"):  # constructor
        self.name = name  # instance attributes
        self.location = location
        self.division = division
        self.salary = r.randint(10000, 100000)

    def get_details(self):
        return self.name, self.location, self.office, self.division, self.salary

    @staticmethod
    def greetuser():
        return "\n Welcome to MS !\n"


e1, e2 = Programmer("pkd", "Hyderabad", "DataVerse"), \
         Programmer("chirag", "Noida", "Xbox")

e2.office = "HomeOffice"

print(e1.greetuser())
print(e1.get_details())
print(e2.get_details())

print(Programmer().get_details())
