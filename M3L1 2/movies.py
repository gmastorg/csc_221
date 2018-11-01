# CSC221
# M3L1_CanjuraHylton
# Goal: [Gold]

"""
class of movie objects 
"""

import validateInput as v

class Movie (object):
    def __init__(self,genre='',Format='', description='',title='',rate = 0.0):
        
        self.genre=genre
        self.format=Format
        self.description=description
        self.title=title
        self.rate=rate

    def getGenre(self):
        """dictionary with movie type options for display"""
        gen={'1':['1.','Regular'],
               '2':['2.','Children'],
               '3':['3.','New Release']}
        return gen

    def getFormat(self):
        """dictionary with movie format options for display"""
        For={'1':['1.', 'VHS',1],
            '2':['2.', 'DVD',3],
            '3':['3.', 'BluRay',4],
            '4':['4.', 'Stream',5]}
        return For
    
    def getDescription(self):
        """movie description currently defaults to title of movie"""
        description= "This movie is about: "+ self.title
        return description

    def getMovieGenre(m):
        """receives user input to let them select the type of movie"""
        maxOption = 0;
        gen = Movie.getGenre(m);
        
        for val in gen.values():
            print(val[0],val[1])
            maxOption += 1
            
        genre=input("Select genre: ")
       
        while v.validateNull(genre)==False or v.validateText(genre, maxOption)==False:
            genre=input("Select genre: ")
        
        for key, value in gen.items():
            if genre==key:
                print("You have selected the following movie genre: ", value[1] )
                genre=value[1]
    
        return m,genre

    def getMovieFormat(m):
        """receives user input to let user select format"""
        maxOption = 0;
        For = Movie.getFormat(m)
        
        for val in For.values():
            print(val[0],val[1])
            maxOption += 1
            
        Format=input("Select format: ")
        
        while v.validateNull(Format)==False or v.validateText(Format, maxOption)==False:
            Format=input("Select format: ")
        
        for key, value in For.items():
            if Format==key:           
                print("You have selected the following movie format: ",value[1])#MEnu
                rate=value[2]
                Format=value[1]
        return m,Format,rate


    def __str__(self):                 
       return str(self.title)+' '+str(self.format)+' '+str(self.genre)+' '+str(self.getDescription())
