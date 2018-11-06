# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 15:22:35 2018

@author: gmastorg
"""

class Cart():
    
        def __init__(self,rental):
        
            self.rental=rental
        
        def getCart(self):
            cart=[]
            cart.append(self.rental)
            return cart