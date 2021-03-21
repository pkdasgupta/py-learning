# Write a class Train which has methods to book a ticket,
# get status(no of seats), and get fare information of trains running under Indian Railways.

class Train:

    def __init__(self, tnum, tscount, ascount, fare):
        self.tnum = int(tnum)
        self.tscount = int(tscount)
        self.ascount = int(ascount)
        self.fare = float(fare)

    def getstatus(slf):
        return slf.tscount, slf.ascount

    def getfare(self):
        return self.fare

    def booktkt(self):
        if self.ascount > 0:
            self.ascount -= 1
            return True
        else:
            return False


T = Train(18626, 500, 440, 640)

print(f"\n **************** Welcome to Indian Railways ***********"
      f"\n\n The booking status of Train - {T.tnum} is :"
      f"\n\n Total Seats : {T.getstatus()[0]}"
      f"\n Available Seats : {T.getstatus()[1]}"
      f"\n Booking Fare is : INR {T.getfare()}"
      f"\n Your Booking Status is : {T.booktkt()} - Now Avaialble : {T.getstatus()[1]} Seats.")
