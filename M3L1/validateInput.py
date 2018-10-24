# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 18:36:46 2018

@author: gmastorg
"""
import os 
import csv
import customerLogins as cl

def getUserNames():
    
    usernames = []
    
    if not os.stat("login.csv").st_size == 0:
        with open ('login.csv') as file:
            inputFile = csv.reader(file)
        
            for row in inputFile:
                username = row[0]
                password = row[1]
                filename = row[2]
                
                logins = cl.CustomerLogins(username, password, filename)
            
                usernames.append(logins) 
   
    return usernames

def verifyUsername(username):
    
    verify = False
    usernamesList = []
    
    usernamesList = getUserNames()

    for item in usernamesList:
        if username == item.username:
            verify = True

    return verify

def getFileName(username):
    
    usernamesList = []
    usernamesList = getUserNames()
    
    for item in usernamesList:
        if username == item.username:
            return item.filename

def verifyPassword(password):
    
    verify = False
    usernamesList = []
    
    usernamesList = getUserNames()

    for item in usernamesList:
        if password == item.password:
            verify = True

    return verify

 