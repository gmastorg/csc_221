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
from rentReturn import rentReturnDecision

def main():
    maxOption = 2
    
    print(display.welcomeMessage())

    decision = v.menu(display.loginMenu(),maxOption)     
    # uses user input to login or create account    
    l.loginDecision(decision)
    
    #lets user say if they are returning or renting maxOption changed to 3 
    #for exit option 
    maxOption = 3
    
    while decision != maxOption:
        decision = v.menu(display.rentReturnMenu(),maxOption)
        rentReturnDecision(decision)
main()
