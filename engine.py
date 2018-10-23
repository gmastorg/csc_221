from customer import Customer
from movie import Movie
from rental import Rental


def createObject():
    c=Customer()
    return c
    
def getCustomerInfo():
    firstName=input("First Name: ")
    lastName=input("Last Name: ")
    address=input("Street Adress: ")
    city=input("City: ")
    state=input("State: ")
    zipcode=input("Zip Code: ")
    c=Customer(firstName, lastName, address, city, state, zipcode)
    print('\n',str(c))
    print()
    return c

def getCustomerStatus(c):
    status=c.getCustomerStatus()
    for val in status.values():
        print(val[0],val[1])
    opt=input("\nEnter your customer status: ")
    return status,opt

def getDiscount(c, status,opt):
    for key,value in status.items():
        if  opt==key:
           discount=value[2]
    print("You have earned a ",discount,"% discount.")
 #   return discount

def getPaymentMethod(c):
    payMethod=c.getPayment()
    for val in payMethod.values():
        print(val[0],val[1])
    method=input("How will you pay for your rental(s)?:")
    for key,value in payMethod.items():
        if method==key:
            payment=value[1]
    print("You have selected the following payment method: ",payment)
    #return payment

def main():
  #  c=createObject()
    c=getCustomerInfo()
    status,opt=getCustomerStatus(c)
    getDiscount(c, status,opt)
    getPaymentMethod(c)
    
   

main()

