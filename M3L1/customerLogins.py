# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 18:26:38 2018

@author: gmastorg
"""
import csv
import customer as c

class CustomerLogins(object):
    
    def __init__(self, username, password, filename):
        
        self.username = username
        self.password = password
        self.filename = filename
    
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
    
    def createCustomer():
         
         firstName=input("First Name: ")
         lastName=input("Last Name: ")
         address=input("Street Adress: ")
         city=input("City: ")
         state=input("State: ")
         zipcode=input("Zip Code: ")
        
         c.Customer(firstName, lastName, address, city, state, zipcode)
    