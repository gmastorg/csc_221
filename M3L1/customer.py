# CSC221
# M3L1_CanjuraHylton
# Goal: [Gold]
"""
class for customers 
"""

class Customer ():
    def __init__(self, firstName,lastName, address, city,state,zipcode):
        self.firstName=firstName
        self.lastName=lastName
        self.address=address
        self.city=city
        self.state=state
        self.zipcode=zipcode


    def getCustomerName(self):
        return str(self.firstName)+" "+str(self.lastName)

    def getBilling(self):
        text=str(self.address)+'\n'+str(self.city)+','+str(self.state)
        return text+" "+str(self.zipcode)
    
    def __str__(self):
        return str(self.getCustomerName()) +str(self.getBilling())