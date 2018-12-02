# CSC221
# M3L1_CanjuraHylton
# Goal: [Gold]

"""
class that deals with rental aspects
"""

from datetime import timedelta, date

class Rental(object):
    def __init__(self, Format, rate, startDate, movie, customer):
        self.startDate= startDate
        self.dueDate=self.startDate+(timedelta(days=3))
        self.days=3
        self.Format=Format
        self.rate=rate
        self.movie=movie #movie object
        self.customer=customer
    
    def __str__(self):
        text=("Movie: "+self.movie.title+"\nRate: "+str(self.rate))
        text+=("\nStart Date: "+str(self.startDate)+"\nDue Date: "+str(self.dueDate))
        return text

