# CSC221
# M3L1_CanjuraHylton
# Goal: [Gold]

"""
deals with verification of login and creation of login/customer account
"""
import csv
import customerLogins as cl
import validateInput as validate
import customer as c
import display

def loginDecision(decision):
    """receieves menu input and calls corresponding method"""
    if decision== 1:
        filename = login()
    if decision==2:
        filename = createAccount()
    
    return filename

def login():
    """receives username and password verifies info and loads customer file to customer object"""
    username = input("Username: ")
    password = input("Password: ")
    
    verifyUsername = validate.verifyUsername(username)
    verifyPassword = validate.verifyPassword(password)
    
    if(verifyUsername == True and verifyPassword == True):
        
        print("Welcome back!\n")
        
        filename = validate.getFileName(username)
        
        getCustomerInfo(filename)
   
    else:
        display.invalidInput()
        login()
    
    return filename

def createAccount():
    """has user create account if theirs does not exist"""
    username = input("Username: ")
        
    password = input("Password: ")
    
    filename = username+".csv"

    cl.CustomerLogins(username, password, filename)
    
    createCustomer(filename)
    
    outfile = open('login.csv', 'a')
    
    outfile.write(username+','+password+','+filename+"\n")
    
    outfile.close()
    
    return filename

def getCustomerInfo(filename):
    """creates customer object from customer file"""  
    with open(filename) as file:
        inputFile = csv.reader(file)
        
        for row in inputFile:
             firstName=row[0]
             lastName=row[1]
             address=row[2]
             city=row[3]
             state=row[4]
             zipcode=row[5]
        
    c.Customer(firstName, lastName, address, city, state, zipcode) 
        
def createCustomer(filename):
   """creates new customer object and new customer file"""      
   firstName=input("First Name: ")
   lastName=input("Last Name: ")
   address=input("Street Adress: ")
   city=input("City: ")
   state=input("State: ")
   zipcode=input("Zip Code: ")
   
   c.Customer(firstName, lastName, address, city, state, zipcode)
           
   outfile = open(filename, 'a')
    
   outfile.write(firstName+','+lastName+','+address+','+city+','+
                       state+','+zipcode+"\n")
    
   outfile.close()

