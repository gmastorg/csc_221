"""
Created on Mon Oct 15 13:52:43 2018
@author: hyltonc4469
"""

from datetime import timedelta, date,time


class Rental(object):
    def __init__(self,startDate='',dueDate='',rate=0.0, lateFee=.2,days=3):
        self.startDate=startDate #can this equal datetime.now()
        self.dueDate=dueDate
        self.rate=rate
 #       self.lateRate=lateRate
        self.lateFee=lateFee
        self.days=days

    def getStartDate(self):
        self.startDate=date.today()
        return self.startDate

    def getDueDate(self):
        self.dueDate=self.startDate+(timedelta(days=3))
        return self.dueDate

    def getReturnDate(self):#redundant
        return self.returnDate

    def getLateRate(self):
         self.lateRate=(self.rate*self.lateFee)
         return self.lateRate
         

    def getRentalRate(self):
        return self.rate*self.days
    
    def getRentalDates(Format,rate):
        
        r=Rental()
        startDate=r.getStartDate()
        dueDate=r.getDueDate()
        lateRate=r.getLateRate()
        rentalRate=r.getRentalRate()
        r=Rental(startDate,dueDate,rate)
        print(str(r))

    def __str__(self):
        text=("Start Date: "+str(self.startDate))+("\nDueDate: "+str(self.dueDate))
        text+=("\nRental Rate: $"+str(self.getRentalRate()))
        return text+("\nLate Fee will be: $"+str(self.getLateRate())+" per additional day.")