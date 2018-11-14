# CSC221
# M3L1_CanjuraHylton
# Goal: [Gold]

"""
deals with verification of login and creation of login/customer account
"""
import listBuilder as listB
import csv
import customerLogins as cl
import validateInput as validate
import customer as c
import display

def loginDecision(decision):
    """receieves menu input and calls corresponding method"""
    if decision== 1:
        customer = login()
    if decision==2:
        customer = createAccount()
            
    return customer

def login():
    """receives username and password verifies info and loads customer file to customer object"""
    username = input("Username: ")
    password = input("Password: ")
    
    verifyUsername = validate.verifyUsername(username)
    verifyPassword = validate.verifyPassword(password)
    
    if(verifyUsername == True and verifyPassword == True):
        
        print("Welcome back!\n")
        
        customerLogin = validate.getFileName(username)
        
        customer = getCustomerInfo(customerLogin)
    else:
        display.invalidInput()
        login()
    
    return customer

def createAccount():
    """has user create account if theirs does not exist"""
    username = input("Username: ")
        
    password = input("Password: ")
    
    filename = username+".csv"

    customerLogin = cl.CustomerLogins(username, password, filename)
    
    customer = createCustomer(customerLogin)
    
    outfile = open('login.csv', 'a')
    
    outfile.write(username+','+password+','+filename+"\n")
    
    outfile.close()
    
    return customer

def getCustomerInfo(customerLogin):
    """creates customer object from customer file""" 
    
    with open(customerLogin.filename) as file:
        inputFile = csv.reader(file)
        
        index = 0
        
        for row in inputFile:
             firstName=row[0]
             lastName=row[1]
             address=row[2]
             city=row[3]
             state=row[4]
             zipcode=row[5]
             
             index += 1
             if index==1: break
        
    customer = c.Customer(firstName, lastName, address, city, state, zipcode, customerLogin) 
     
    return customer 

def createCustomer(customerLogin):
   """creates new customer object and new customer file"""      
   firstName=input("First Name: ")
   lastName=input("Last Name: ")
   address=input("Street Adress: ")
   city=input("City: ")
   state=input("State: ")
   zipcode=input("Zip Code: ")
   
   customer=c.Customer(firstName, lastName, address, city, state, zipcode, customerLogin)
           
   outfile = open(customerLogin.filename, 'a')
    
   outfile.write(firstName+','+lastName+','+address+','+city+','+
                       state+','+zipcode+"\n")
    
   outfile.close()
   
   return customer

