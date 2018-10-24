# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 13:52:43 2018
@author: hyltonc4469
"""
class Movie (object):
    def __init__(self,genre='',Format='', description='',title='',rate = 0.0):
        
        self.genre=genre
        self.format=Format
        self.description=description
        self.title=title
        self.rate=rate

    def getGenre(self):
        gen={'1':['1.','Regular'],
               '2':['2.','Children'],
               '3':['3.','New Release']}
        return gen

    def getFormat(self):
        For={'1':['1.', 'VHS',1],
            '2':['2.', 'DVD',3],
            '3':['3.', 'BluRay',4],
            '4':['4.', 'Stream',5]}
        return For
    
    def getDescription(self):
        description= "This movie is about: "+ self.title
        return description

    def getMovieGenre(m):
        
        gen = Movie.getGenre(m);
        
        for val in gen.values():
            print(val[0],val[1])
            
        genre=input("Select genre: ")
        
        for key, value in gen.items():
            if genre==key:
                print("You have selected the following movie genre: ", value[1] )
                genre=value[1]
    
        return m,genre

    def getMovieFormat(m):
        
        For = Movie.getFormat(m)
        
        for val in For.values():
            print(val[0],val[1])
            
        Format=input("Select format: ")
        for key, value in For.items():
            if Format==key:           
                print("You have selected the following movie format: ",value[1])#MEnu
                rate=value[2]
                Format=value[1]
        return m,Format,rate


    def __str__(self):
##        header=['Title','Format','Genre','Description']
##        choice=[str(self.title),str(self.format),str(self.genre),str(self.getDescription())]
##        for x in header:
##            for y in choice:
##                line=x+':'+y
## #               line=str(line)+' '
##                return str(line)
       
            
       return str(self.title)+' '+str(self.format)+' '+str(self.genre)+' '+str(self.getDescription())