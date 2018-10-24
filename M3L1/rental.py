# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 13:52:43 2018
@author: hyltonc4469
"""
from datetime import timedelta, datetime


class Rental(object):
    def __init__(self, startDate,returnDate, rate=0.0):
        self.rate=rate
        self.startDate=startDate #can this equal datetime.now()
        self.returnDate=returnDate

    def getStartDate(self):
        return datetime.now()

    def getDueDate(self):
        return self.startDate+timedelta(days=3)

    def getReturnDate(self):#redundant
        return self.returnDate

    def getLateFee(self):
        return self.rate*.2

    def getRentalRate(self):
        return self.rate*self.returnDate
