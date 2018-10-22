from customer import Customer
from movie import Movie
from rental import Rental

    
def getCustomerInfo():
    firstName=input("First Name: ")
    lastName=input("Last Name: ")
    address=input("Street Adress: ")
    city=input("City: ")
    state=input("State: ")
    zipcode=input("Zip Code: ")
    c=Customer(firstName, lastName, address, city, state, zipcode)
    print()
    print(str(c))



def main():
    getCustomerInfo()
    
   

main()

