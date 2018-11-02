# CSC221
# M3L1_CanjuraHylton
# Goal: [Gold]

"""
class of movie objects 
"""

class Movie ():
    def __init__(self, genre, description, title, year):
        
        self.genre=genre
        self.description=description
        self.title=title
        self.year = year

    def getDescription(self):
        """movie description currently defaults to title of movie"""
        description= "This movie is about: "+ self.title
        return description

    def __str__(self):                 
       return str(self.title)+'\t\t'+str(self.genre)+' '+str(self.description)
   
    
