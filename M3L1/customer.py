"""
Created on Mon Oct 15 13:52:43 2018
@author: hyltonc4469
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

    def getGenre(self):
        genre={1:'Regular',2:'Children', 3:'New Release'}
        return genre

    def getCustomerStatus(self):
        status={1:'New Customer', 2:'Returning Customer'}
        return status
    
    def getPayment():#if customer's not returning, cannot place on tab
         
        payMethod={'1':['1.','Cash'],
                   '2':['2.','Debit Card'],
                   '3':['3.','Check'],
                   '4':['4.','Credit Card'],
                   '5':['5.','Tab']}
        
        for val in payMethod.values():
            print(val[0],val[1])
    
        method=input("How will you pay for your rental(s)?:")
   
        for key,value in payMethod.items():
            if method==key:
                payment=value[1]
    
                print("You have selected the following payment method: ",payment)
    
    def __str__(self):
        return str(self.getCustomerName()) +str(self.getBilling())