# CSC221
# M3L1_CanjuraHylton
# Goal: [Gold]

"""
creates list of movie objects and list of objects from previous customer rentals
"""
import csv
from movies import Movie
from rental import Rental
from datetime import timedelta, date,datetime

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
             genre=row[1]
             year=row[7]
             movie = Movie(title, genre, year)
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
                
                    movie = Movie(title, genre, year)
                    rental = Rental(Format, rate,startDate, movie, customer)
                    rentals.append(rental)
        
    return rentals
    
    
