import random as r


class Employee:
    company = "Microsoft"
    office = "MsBldg"

    def __init__(self, name, location, division):
        self.name = name
        self.location = location
        self.division = division
        self.salary = r.randint(10000, 100000)

    def get_details(self):
        return self.name, self.location, self.office, self.division, self.salary

    @staticmethod
    def greetuser():
        return "\n Raam Raam Ji..\n"


e1, e2 = Employee("pkd", "Hyderabad", "DataVerse"), \
         Employee("chirag", "Noida", "Xbox")

e2.office = "HomeOffice"

print(e1.greetuser())
print(e1.get_details())
print(e2.get_details())
