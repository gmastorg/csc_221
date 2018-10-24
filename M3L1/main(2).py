# CSC221
# M3L1_Canjura
# Goal: [Gold]

"""
Author: Gabriela Canjura
receives input from user
"""
import display
from movies import Movie
from rental import Rental
import string
import login as l  
 
################################## MOVIE INFORMATION############################
def getMovieGenre():
    m=Movie()
    gen=Movie.getGenre(m)
    for val in gen.values():
        print(val[0],val[1])
    genre=input("Select genre: ")
    for key, value in gen.items():
        if genre==key:
            print("You have selected the following movie genre: ", value[1] )
            genre=value[1]#   m=getMovieObject()])#MEnu
    return m,genre

def getMovieFormat(m):
    For=Movie.getFormat(m)
    for val in For.values():
        print(val[0],val[1])
    Format=input("Select format: ")
    for key, value in For.items():
        if Format==key:           
            print("You have selected the following movie format: ",value[1])#MEnu
            rate=value[2]
    Format=value[1]
    return m,Format,rate

def getMovieObject(m,genre,Format):
    title=input("Movie Title: ")
    description=Movie.getDescription(m)
    m=Movie(genre,Format,description, title)
    print(m)
    print("You have selected the following movie infomation: ", str(m))#MEnu
    return m

##############################RENTAL INFORMAITON##############################
def getRentalDates(Format,rate):
    print("The movie rental rate for ",Format,"is: $",rate," per day.")

##############################MAIN--TO GO ON MENU/DISPLAY?####################
def main():
  #  c=createObject()
    
    display.welcomeMessage()
    
    choice = display.loginMenu()
    while not choice:
        choice = display.loginMenu()
    while choice not in string.digits or int(choice) > 2:
        display.invalidInput()
        choice = display.loginMenu()
    decision = int(choice)
      
    l.loginDecision(decision)
    
    m,genre=getMovieGenre()
    m,Format,rate=getMovieFormat(m)
    m=getMovieObject(m,genre,Format)
    getRentalDates(Format,rate)
    getDiscount(c, status,opt)
    getPaymentMethod(c)
    
   

main()

