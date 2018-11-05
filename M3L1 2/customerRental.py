from customer import Customer
from rental import Rental
from movies import Movie


firstName='Marie'
lastName='Hylton'

c=Customer('Marie', 'Hylton','123','ftb','nc','123456')       
print("Customer: ",c.firstName+' '+c.lastName)

r=Rental()
m=Movie()
rentDate=r.startDate
dueDate=r.dueDate
r=Rental(rentDate,dueDate)


print(dueDate)


#genre=m.getGenre()
m.title="Hallmark Christmas"
#print(m.title)
title=m.title
genre=m.getMovieGenre()
Format=m.getMovieFormat()
#descript=m.getDescription

print("Try this out!!!!!!!!!")
print()
#Format this object#
custRental=Customer(c.getCustomerName(),m.title,m.Format,r.startDate,r.dueDate,r.logTime)
print(custRental)
print('Customer: ',c.getCustomerName(),'\nTitle: ',m.title)
print()
print("hi")
lateRates=r.getLateRate()
print(lateRates)


r.titleMovie=(m.title)#Is this membership?
r.movieDetails=m
print(r.titleMovie)
print(r)#prints rental object including the title parameter from movie class
m.getMovieFormat()
print(r.movieDetails)


'''QUESTIONS:  no laterate, right?How are we passing r through getRentalDates?
Don't think we need customer rental, just run these methods through the rental
class, how much is the rental rate/day after 3 days...$1 for all or format rate?'''

class CustomerRental(object):#try passing the time obj. through the clas explicitly
    def __init__(self,logTime):
        self.logTime=datetime.now()
       

    def getTimeStamp(self):
        return self.logTime

    #Instead those can be vars in the code

##'''
##    def getExpectedRentDate(self):#redundant?  Use during rental checkout w/time
##        #return r.getStartDate()
##        return datetime.now()#time needed to calculate full day rent/returns
##    
##    def getActualReturnDate(self):#use during return check in w/ time
##        return datetime.now()#time needed to calculate full day rent/returns
##
##    def checkOutTime(self):
##        return datetime.now()
##'''   
##
##'''   def checkoutStatement(self):
##        #pull current time during checkout as a variable
##        #include 'dueStatement' about when rentals are due(time)
##        self.logTime
##'''

    def calcTimeSpan(self):
        #pull current time during rental return as a variable
        #calc timespan from checkoutStatement to current time during rent return
        #include statement about accruement of latefees if applicable AND
        #calc days rented for total amount due during payment.
        
        #Rent
        self.rentTime=datetime.now().time()
        #Return
        self.returnTime=datetime.now().time()
        #TimeSpan
        return self.returnTime-self.rentTime

    
