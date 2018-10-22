# CSC221
# M3L1_Canjura
# Goal: [Gold]

"""
Author: Gabriela Canjura
holds movie objects
"""

class Movies:
    
    def __init__(self, name,price):
         
        self._Name = name
        self._Price = price
    
    def totalCost(self, price, days):
        
        total = self._Price* days
        
        return total 
       
