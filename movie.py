# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 13:52:43 2018

@author: hyltonc4469
"""


class Movie (object):
    def __init__(self,genre,Format, description,title='',):
        
        self.genre=genre
        self.format=Format
        self.description=description
        self.title=title

    def getGenre(self):
        genre={1:'Regular',2:'Children', 3:'New Release'}
        return genre
    
    def getDescription(self):
        return "This movie is about: "+ self.title


        

        
 ##    def getRentalSpan(self):
##        return self.startDate+timedelta(days=3)

       
        
        
    
