# CSC221
# M3L1_CanjuraHylton
# Goal: [Gold]

"""
creates list of movie objects and list of objects from previous customer rentals
"""

import os
import csv
from MovieRental_CanjuraHylton import movies
from MovieRental_CanjuraHylton import rentals as rent
from datetime import timedelta, date,datetime

def getMovieLists():
    
    moviesList = [] 
    allMovies = []
    childrens = []
    newReleases = []
    regular = []
    
    with open(os.path.dirname(__file__)+"/CSVFiles/movies.csv") as file:
        inputFile = csv.reader(file)
        
        for row in inputFile:
             title=row[0]
             genre=row[1]
             year=row[7]
             movie = movies.Movie(title, genre, year)
             allMovies.append(movie)
     
    allMovies.pop(0)
    
    #for item in allMovies:
    #    if item.genre == "Animation":
    #        item.genre = "childrens"
    #        childrens.append(item)
    #    elif item.year == "2011":
    #        item.genre = "new release"
    #        newReleases.append(item)
    #    else:
    #        item.genre = "regular"
    #        regular.append(item)
    
    #moviesList.append(newReleases)
    #moviesList.append(regular)
    #moviesList.append(childrens)
    

    return allMovies

def getComments():
    """Gets Comments from file"""
    comments = []

    with open(os.path.dirname(__file__)+"/CSVFiles/comments.csv") as file:
        inputFile = csv.reader(file)
    
        for row in inputFile:
            comment = row[0]
            
            comments.append(comment)
            
    return comments

def getOutstandingRentals(customer):
    """gets customer's outstanding moveis"""
    rentals = []
    
    with open(customer.customerLogin.filename) as file:
        inputFile = csv.reader(file)

        if next(inputFile): #supposed to skip first line and check if second line exists
            for row in inputFile:
                if len(row)==6: 
                    title = row[0]
                    genre = row[1]
                    year = row[2]
                    Format = row[3]
                    rate = row[4]
                    startDate = datetime.strptime(row[5],'%Y-%m-%d')
                
                    movie = movies.Movie(title, genre, year)
                    rental = rent.Rental(Format, rate,startDate, movie, customer)
                    rentals.append(rental)
        
    return rentals
    
def getAllMovieTitles():
    
    allMovies = []
    titles = []
    
    allMovies = getMovieLists()

    for item in allMovies:
        titles.append(item.title)

    return titles
