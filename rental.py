from datetime import timedelta, datetime


class Rental(object):
    def __init__(self, startDate,returnDate, rate=0.0):
        self.rate=rate
        self.startDate=startDate #can this equal datetime.now()
        self.returnDate=returnDate

    def getStartDate(self):
        return datetime.now()

    def getDueDate(self):
        return self.startDate+timeDelta(days=3)

    def getReturnDate(self):#redundant
        return self.returnDate

    def getRentalRate(self):
        return self.rate*self.returnDate
