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

def main():
    
    display.welcomeMessage()
    
    choice = input(display.loginMenu())
    """validates input"""
    while not choice:
        choice = input(display.loginMenu())
    while choice not in string.digits or int(choice) > 2:
        display.invalidInput()
        choice = input(display.loginMenu())

    decision = int(choice)
        
    l.loginDecision(decision)
    
main()