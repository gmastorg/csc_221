# CSC221
# M3L1_CanjuraHylton
# Goal: [Gold]

"""
class of movie objects 
"""
import validateInput as v

class Movie (object):
    def __init__(self,gen='',For='', title='',description='',year='',genre='',Format='',rate = 0.0):
        
        self.gen={'1':['1.','Regular'],
                    '2':['2.','Children'],
                    '3':['3.','New Release']}
        
        self.For={'1':['1.', 'VHS',1],#{menuChoice:heading,format,formatprice}
                     '2':['2.', 'DVD',3],
                     '3':['3.', 'BluRay',4],
                     '4':['4.', 'Stream',5]}
        self.title=title
        self.description="This movie is about: "+ self.title
        self.year=year
        self.genre=genre
        self.Format=Format
        self.rate=rate#do we need this?


    def getMovieGenre(self):
        """receives user input to let them select the type of movie"""
        maxOption = 0;
        for val in self.gen.values():
            print(val[0],val[1])
            maxOption += 1
        genre=input("Select genre: ")
        while v.validateNull(genre)==False or v.validateText(genre, maxOption)==False:
            genre=input("Select genre: ")
            
        for key, value in self.gen.items():
            if genre==key:
                print("You have selected the following movie genre: ", value[1] )
                genre=value[1]
        return genre
    
    def getMovieFormat(self):
        """receives user input to let user select format"""
        maxOption = 0;
        for val in self.For.values():
            print(val[0],val[1])
            maxOption += 1
            
        Format=input("Select format: ")
        while v.validateNull(Format)==False or v.validateText(Format, maxOption)==False:
            Format=input("Select format: ")
        
        for key, value in self.For.items():
            if Format==key:           
                print("You have selected the following movie format: ",value[1])#MEnu
                rate=value[2]
                Format=value[1]
        return Format,rate

    def __str__(self):
        text='\nTitle: '+ str(self.title)+'\nFormat: '+str(self.Format)
        text+='\nGenre: '+str(self.genre)+'\nDescription: '+str(self.description)
        text+='\nYear: '+str(self.year)+('\nRate: $'+str(self.rate))
        return text
