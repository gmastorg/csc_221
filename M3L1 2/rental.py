# CSC221
# M3L1_CanjuraHylton
# Goal: [Gold]

"""
class that deals with rental aspects
"""

from datetime import timedelta, date,time,datetime


class Rental(object):
    def __init__(self,startDate='',dueDate='',rate=0.0, lateFee=.2,days=3):
        self.startDate=startDate
        self.dueDate=dueDate
        self.rate=rate
        self.lateFee=lateFee
        self.days=days

    def getStartDate(self):
        """gets date from computer"""
        self.startDate=date.today()
        return self.startDate

    def getDueDate(self):
        """gets date from computer and adds 3"""
        self.dueDate=self.startDate+(timedelta(days=3))
        return self.dueDate

    def getLateRate(self):
        """calculates rate if items returned late"""
        self.lateRate='{0:.2f}'.format(self.rate*self.lateFee)
        return self.lateRate
         
    def getRentalRate(self):
        """gets total cost for days rented for each movie"""
        return self.rate*self.days
    
    def getRentalDates(r,Format,rate):
        startDate=r.getStartDate()
        dueDate=r.getDueDate()
        lateRate=r.getLateRate()
        rentalRate=r.getRentalRate()
        r=Rental(startDate,dueDate,rate)
        return r
    
    def __str__(self):
        text=("Start Date: "+str(self.startDate))+("\nDueDate: "+str(self.dueDate))
        text+=("\nRental Rate: $"+str(self.getRentalRate()))
        return text+("\nLate Fee will be: $"+str(self.getLateRate())+" per additional day.")
