# CSC221
# M3L1_CanjuraHylton
# Goal: [Gold]

"""
class that deals with rental aspects
"""

from datetime import timedelta, date,datetime
import movies

class Rental(object):
    def __init__(self,startDate='',dueDate='',logTime='', days=3, Format='', rate =0.0):
        self.startDate=date.today()#startDate
        self.dueDate=self.startDate+(timedelta(days=3))
        self.logTime=datetime.now().time()
        self.days=days
        self.Format=Format
        self.rate=rate#do we need this?

        self.For={'1':['1.', 'VHS',1],#{menuChoice:heading,format,formatprice}
                  '2':['2.', 'DVD',3],
                  '3':['3.', 'BluRay',4],
                  '4':['4.', 'Stream',5]}

    def getTimeStamp(self):
        return self.logTime

    def calcTimeSpan(self):
        #Rent Time
        self.rentTime=datetime.now().time()
        #Return Time
        self.returnTime=datetime.now().time()
        #TimeSpan
        return self.returnTime-self.rentTime

    def getMovieFormat(self):
        """receives user input to let user select format"""
        maxOption = 0;
        for val in self.For.values():
            print(val[0],val[1])
            maxOption += 1
            
        Format=input("Select format: ")
        while v.validateNull(Format)==False or v.validateText(Format, maxOption)==False:
            Format=input("Select format: ")
        
        for key, value in self.For.items():
            if Format==key:           
                print("You have selected the following movie format: ",value[1])#MEnu
                rate=value[2]
                Format=value[1]
        return Format,rate
    
    def __str__(self):
        t=movies.Movie()
        text=("Time Stamp: "+str(self.logTime))
        text+=("\nRate: "+str(t.rate)+"\nStart Date: "+str(self.startDate))
        return text
tional day.")
