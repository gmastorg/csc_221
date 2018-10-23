# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 18:36:46 2018

@author: gmastorg
"""
import login 

def verifyUsername(username):
    
    # need to fix this for empty files
    usernamesList = [login.getUserNames()]
    
    if not not usernamesList:
        for i in range(len(usernamesList)):
            if username == usernamesList[i].username:
                return True
    else:
        return False

def getFileName(username):
    
    usernamesList = [login.getUserNames()]
    
    for i in range(len(usernamesList)):
        if username == usernamesList[i].username:
            return usernamesList[i].filename

def verifyPassword(password):
    
    usernamesList = [login.getUserNames()]
    
    for i in range(len(usernamesList)):
        if password == usernamesList[i].password:
            return True
    
    return False
    
        