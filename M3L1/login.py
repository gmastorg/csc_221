# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 17:13:11 2018

@author: gmastorg
"""
import customerLogins as cl
import csv
import validateInput as validate
import os


def getUserNames():
    
    usernames = []
    
    if not os.stat("login.csv").st_size == 0:
        with open ('login.csv') as file:
            inputFile = csv.reader(file)
        
            for row in inputFile:
                username = row[0]
                password = row[1]
                filename = row[3]
            
            usernames = cl.CustomerLogins(username, password, filename)

def loginDecision(decision):
    
    if decision== 1:
        login()
    if decision==2:
        createAccount()

def login():
    
    username = input("Username: ")
    password = input("Password: ")
    
    if (validate.verifyUsername(username) and
        validate.verifyPassword(password)):
        
        print("You are logged in.")
        
        filename = validate.getFileName(username)
        
        cl.getCustomerInfo(filename)
   
    
def createAccount():
    
    username = input("Username: ")
    
    while validate.verifyUsername(username):
       username = input("Username: ") 
        
    password = input("Password: ")
    
    filename = username+".csv"

    cl.CustomerLogins(username, password, filename)