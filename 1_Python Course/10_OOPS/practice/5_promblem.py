# Write a class Train which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.


from random import randint

class Train:
    def __init__(self, passenger_name, trainNo):
        self.passenger_name = passenger_name
        self.trainNo = trainNo

    def book(self, from_, to_):
        print(f"Ticket is booked in train no: {self.trainNo} from {from_} to {to_}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time.")

    def getFare(self, from_, to_):
        print(f"Ticket fare in train no: {self.trainNo} from {from_} to {to_} is {randint(222, 2433)}")



t = Train("CGM", 12345)
t.book("dullahapur", "prayagraj")
t.getStatus()
t.getFare("dullahapur", "prayagraj")