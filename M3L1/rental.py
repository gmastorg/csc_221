# CSC221
# M3L1_CanjuraHylton
# Goal: [Gold]

"""
class that deals with rental aspects
"""

from datetime import timedelta, date,time


class Rental():
    
    def __init__(self,startDate,rate,Format):
        self.startDate=startDate
        self.rate=rate
        self.Format = Format

    def getStartDate(self):
        """gets date from computer"""
        self.startDate=date.today()
        return self.startDate
    
    def __str__(self):
        text=("Start Date: "+str(self.startDate))+("\nDueDate: "+str(self.dueDate))
        text+=("\nRental Rate: $"+str(self.getRentalRate()))
        return text+("\nLate Fee will be: $"+str(self.getLateRate())+" per additional day.")