# CSC221
# M3L1_CanjuraHylton
# Goal: [Gold]
"""
class for customers 
"""
import validateInput as v

class Customer ():
    def __init__(self, firstName,lastName, address, city,state,zipcode, customerLogin):
        self.firstName=firstName
        self.lastName=lastName
        self.address=address
        self.city=city
        self.state=state
        self.zipcode=zipcode
        self.customerLogin=customerLogin


    def getCustomerName(self):
        return str(self.firstName)+" "+str(self.lastName)

    def getBilling(self):
        text=str(self.address)+'\n'+str(self.city)+','+str(self.state)
        return text+" "+str(self.zipcode)
    
    def getPayment(self):#if customer's not returning, cannot place on tab
        """receives customer payment option"""
        maxOption = 0; 
        payMethod={'1':['1.','Cash'],
                   '2':['2.','Debit Card'],
                   '3':['3.','Check'],
                   '4':['4.','Credit Card'],
                   '5':['5.','Tab']}
        
        print("\n")
        
        for val in payMethod.values():
            print(val[0],val[1])
            maxOption +=1
            
        method=input("How will you pay for your rental(s)?:")
        
        while v.validateNull(method)==False or v.validateText(method, maxOption)==False:
            method=input("How will you pay for your rental(s)?:")
   
        for key,value in payMethod.items():
            if method==key:
                payment=value[1]
    
                print("You have selected the following payment method: ",payment)
    
    
    def __str__(self):
        return str(self.getCustomerName()) +str(self.getBilling())