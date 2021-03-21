from termcolor import colored, cprint


class Vehicle:
    def __init__(self, nwheels, nseats, ctype, clr):
        self.nwheels = int(nwheels)
        self.nseats = int(nseats)
        self.ctype = str(ctype)
        self.clr = str(clr)

    def getColor(self):
        return self.clr.capitalize()

    def run(self):
        return "Vroom..Vroom.."

class Car(Vehicle):
    def __init__(self, nwheels, nseats, ctype, clr, isauto=False):
        super().__init__(nwheels, nseats, ctype, clr)  # using super() to call the parent class(Vehicle) constructor
        self.isauto = isauto

    def getColor(self):
        return self.clr.upper()

    def getMode(self):
        return self.isauto

    def run(self):
        cprint("Car..Starting..", "cyan")
        cprint(super(Car, self).run(), "green")

v = Vehicle(14, 3, "goods", "red")
cprint(v.getColor(), v.clr)

c = Car(4, 4, "passenger", "blue")
cprint(c.getColor(), c.clr)

cprint(c.getMode(), "yellow")
c.run()
