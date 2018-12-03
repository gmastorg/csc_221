# CSC221
# M3L1_CanjuraHylton
# Goal: [Gold]

"""
validates input
"""
import csv
from MovieRental_CanjuraHylton import customerLogins as cl
import string
from MovieRental_CanjuraHylton import display

def validateNull(choice):
    """validates if no input"""
    if not choice:
        return False
    else:
        return True
    
def validateText(choice, maxOption):
    """validates if letter or not menu option"""
    if choice not in string.digits or int(choice) > maxOption:
        return False
    else:
        return True

def getUserNames():
    """creates list of login usernames and passwords from file"""
    usernames = []
    
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
    """checks the list of customer login objects for username entered by user"""
    verify = False
    usernamesList = []
    
    usernamesList = getUserNames()

    for item in usernamesList:
        if username == item.username:
            verify = True

    return verify

def getFileName(username):
    """once customer logs in retrieves their customer file"""
    usernamesList = []
    usernamesList = getUserNames()
    
    for item in usernamesList:
        if username == item.username:
            return item

def verifyPassword(password):
    """checks the list of customer login objects for password entered by user"""
    verify = False
    usernamesList = []
    
    usernamesList = getUserNames()

    for item in usernamesList:
        if password == item.password:
            verify = True

    return verify

def menu(menuText, maxOption):
    
    choice = input(menuText)
    #validates input
    while validateNull(choice) == False:
        choice = input(menuText)
    while validateText(choice, maxOption) == False:
        display.invalidInput()
        choice = input(menuText)
    decision = int(choice)
    
    return decision