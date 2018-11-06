# CSC221
# M3L1_CanjuraHylton
# Goal: [Gold]

"""
class that deals with rental aspects
"""

from datetime import timedelta, date,datetime

class Rental(object):
    def __init__(self, Format, rate, movie):
        self.startDate=date.today()#startDate
        self.dueDate=self.startDate+(timedelta(days=3))
        self.logTime=datetime.now().time() #Why did we want the time?
        self.days=3
        self.Format=Format
        self.rate=rate
        self.movie=movie

    def getTimeStamp(self):
        return self.logTime

    def calcTimeSpan(self):
        #Rent Time
        self.rentTime=datetime.now().time()
        #Return Time
        self.returnTime=datetime.now().time()
        #TimeSpan
        return self.returnTime-self.rentTime

    
    def __str__(self):
        text=("Movie: "+self.movie.title+"\nTime Stamp: "+str(self.logTime))
        text+=("\nRate: "+str(self.rate)+"\nStart Date: "+str(self.startDate))
        return text

