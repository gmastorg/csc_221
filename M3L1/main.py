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
    
main()
