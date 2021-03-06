
# CSC221
# M3L1_CanjuraHylton
# Goal: [Gold]

"""
Author: Gabriela Canjura and Marie Hylton
creates or allows user to login loads or creates customer object 
receives input from user and uses classes to obtain movie rental info
and calculates rental cost and creates reciept
"""

import display
import login as l
import validateInput as v
import rentReturn 
from checkout import checkOut
import listBuilder as listB

def main():
    cart = []
    outCart = []
    totAddCost = 0
    maxOption = 2
    returned = []
    
    print(display.welcomeMessage())
    
    decision = v.menu(display.loginMenu(),maxOption)     
    # uses user input to login or create account    
    customer = l.loginDecision(decision)
    
    outCart = listB.getOutstandingRentals(customer)
    #lets user say if they are returning or renting maxOption changed to 3 
    #for exit option 
    decision = 1
    maxOption = 3
    
    while decision != maxOption:
        decision = v.menu(display.rentReturnMenu(),maxOption)
        if decision == 1: 
            rental = rentReturn.rentMovieMenu(customer)
            cart.append(rental)
        if decision == 2:
            outCart, addCost, returned = rentReturn.returnMovie(cart, outCart, customer, returned)
            totAddCost += addCost
                
    checkOut(cart, outCart, totAddCost, returned)
    
main()
