# CSC221
# M3L1_CanjuraHylton
# Goal: [Gold]

"""
class that deals with rental aspects
"""

from datetime import timedelta, datetime, date


class Rental(object):
    def __init__(self,logTime='',startDate='',dueDate='',rate=0.0, lateFee=.2,days=3):
        self.startDate=date.today()#startDate
        self.dueDate=self.startDate+(timedelta(days=3))
        self.rate=rate
        self.lateFee=lateFee
        self.days=days
        self.logTime=datetime.now()
        
    def getTimeStamp(self):
        return self.logTime
    
    def getLateRate(self):
        """calculates rate if items returned late"""
        return '{0:.2f}'.format(self.rate*self.lateFee)
         
    def getRentalRate(self):#add total to the def name
        """gets total cost for days rented for each movie"""
        return self.rate*self.days
    
    def __str__(self):
        text=("Start Date: "+str(self.startDate))+("\nDueDate: "+str(self.dueDate))
        text+=("\nRental Rate: $"+str(self.getRentalRate()))
        return text+("\nLate Fee will be: $"+str(self.getLateRate())+" per additional day.")
