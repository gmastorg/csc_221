# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 13:52:43 2018

@author: hyltonc4469
"""

class Customer (object):
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
        text='\n'+str(self.address)+'\n'+str(self.city)+','+str(self.state)
        return text+" "+str(self.zipcode)

    def getCustomerStatus(self):
     #   status={'1.':'10% Discount for New Customers',
 #               '2.':'5% Discount for Returning Customers'}
        status={'1':['1.','New Customers',10],
                '2':['2.','Returning Customers',5]}
        return status
    
    def getPayment(self):#if customer's not returning, cannot place on tab
        payMethod={'1':['1.','Cash'],
                   '2':['2.','Debit Card'],
                   '3':['3.','Check'],
                   '4':['4.','Credit Card'],
                   '5':['5.','Tab']}
        return payMethod
    
    def __str__(self):
        return str(self.getCustomerName()) +str(self.getBilling())
        
        
    
    
        
    
