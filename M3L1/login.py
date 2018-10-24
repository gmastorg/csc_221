# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 17:13:11 2018

@author: gmastorg
"""
import csv
import customerLogins as cl
import validateInput as validate
import customer as c
import display

def loginDecision(decision):
    """receieves menu input and calls corresponding method"""
    if decision== 1:
        login()
    if decision==2:
        createAccount()

def login():
    ""
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
    
def createAccount():
    
    username = input("Username: ")
        
    password = input("Password: ")
    
    filename = username+".csv"

    cl.CustomerLogins(username, password, filename)
    
    createCustomer(filename)
    
    outfile = open('login.csv', 'a')
    
    outfile.write(username+','+password+','+filename+"\n")
    
    outfile.close()

def getCustomerInfo(filename):
        
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

