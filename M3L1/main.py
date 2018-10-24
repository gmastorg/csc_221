# CSC221
# M3L1_Canjura
# Goal: [Gold]

"""
Author: Gabriela Canjura
receives input from user
"""
import string
import display
import login as l
import customer as c
from movies import Movie
from rental import Rental


def main():
    again='y'
    movie = []
    
    display.welcomeMessage()
    
    display.loginMenu()
    choice = input()
    """validates input"""
    while not choice:
        display.loginMenu()
        choice = input()
    while choice not in string.digits or int(choice) > 2:
        display.invalidInput()
        display.loginMenu()
        choice = input()

    decision = int(choice)
        
    l.loginDecision(decision)
    
    while again=='y':
        m=Movie()
        m, genre=Movie.getMovieGenre(m)
        m,Format,rate=Movie.getMovieFormat(m)
        m = getMovieObject(m,genre,Format)
        movie.append(m)
        Rental.getRentalDates(Format,rate)
        print('\nAdd another movie?')
        again=input('y/n\n')
        
    calCharges(movie)
    
    c.Customer.getPayment()   

def getMovieObject(m,genre,Format):
 
    title=input("Movie Title: ")  
    description=Movie.getDescription(m)
    m = Movie(genre,Format,description, title)
    
    print("You have selected the following movie infomation: ", str(m))#MEnu
    
    return m

def calCharges(movie):
    
    purchaseHeader=("RENTAL\tFORMAT\tRATE\n")
    line=('-'*len(purchaseHeader))
    
    print(purchaseHeader,line)
    for item in movie:
        print(item.title)       

#def printCharges():
    
##############################MAIN--TO GO ON MENU/DISPLAY?####################
    
main()
