# CSC221
# M3L1_CanjuraHylton
# Goal: [Gold]

"""
creates list of movie objects and list of objects from previous customer rentals
"""
import csv
from movies import Movie

def getMovieLists():
    
    moviesList = [] 
    allMovies = []
    childrens = []
    newReleases = []
    regular = []
    
    with open("movies.csv") as file:
        inputFile = csv.reader(file)
        
        for row in inputFile:
             title=row[0]
             description = row[0]
             genre=row[1]
             year=row[7]
             movie = Movie(genre,description, title, year)
             allMovies.append(movie)
     
    allMovies.pop(0)
    
    for item in allMovies:
        if item.genre == "Animation":
            item.genre = "childrens"
            childrens.append(item)
        elif item.year == "2011":
            item.genre = "new release"
            newReleases.append(item)
        else:
            item.genre = "regular"
            regular.append(item)
    
    moviesList.append(newReleases)
    moviesList.append(regular)
    moviesList.append(childrens)
    

    return moviesList

def getOutstandingRentals(customer):
    
    outstandingRentals = []
    
    with open(customer.customerLogin.filename) as file:
        inputFile = csv.reader(file)
        
        for row in inputfile:
            title=row[0]
            Format=row[1]
            startDate=row[2]
    
    
