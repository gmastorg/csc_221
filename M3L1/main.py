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
    rates = []
    
    display.welcomeMessage()
    """
    display.loginMenu()
    choice = input()
    #validates input
    while not choice:
        display.loginMenu()
        choice = input()
    while choice not in string.digits or int(choice) > 2:
        display.invalidInput()
        display.loginMenu()
        choice = input()

    decision = int(choice)
        
    l.loginDecision(decision)
    """
    while again=='y':
        m=Movie()
        m, genre=Movie.getMovieGenre(m)
        m,Format,rate=Movie.getMovieFormat(m)
        m = getMovieObject(m,genre,Format,rate)
        movie.append(m)
         
        r=Rental()
        r = Rental.getRentalDates(r,Format,rate)
        rates.append(r)
        print('\nAdd another movie?')
        again=input('y/n\n')
        
    calCharges(movie,rates)
    
    c.Customer.getPayment()   

def getMovieObject(m,genre,Format,rate):
 
    title=input("Movie Title: ")  
    description=Movie.getDescription(m)
    m = Movie(genre,Format,description, title, rate)
    
    print("You have selected the following movie infomation: ", str(m))#MEnu
    
    return m

def calCharges(movies, rates):
    
    total = 0
    
    purchaseHeader=("RENTAL\tFORMAT\tRATE\n")
    line=('-'*len(purchaseHeader))
    
    print(purchaseHeader,line)
    
    for item in movies:
        print(item.title+"\t"+item.format+"\t"+str(item.rate))
        
    for item in rates:
        cost = item.rate*item.days
        total += cost
    
    total = total*1.05
    
    print("\nTotal: $"+'{0:.2f}'.format(total)+"\n")   
        

#def printCharges():
    
##############################MAIN--TO GO ON MENU/DISPLAY?####################
    
main()
