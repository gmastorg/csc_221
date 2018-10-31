# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 13:07:30 2018

@author: canjurag4010
"""
import csv
from movies import Movie
import rental

def getMovieLists():
    
    moviesList = [] 
    allMovies = []
    childrensMovies = []
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
        
    for item in allMovies:
        if item.genre == "Animation":
            childrensMovies.append(item)
        if item.year == 2011:
            newReleases.append(item)
        else:
            regular.append(item)
    
    moviesList.append(allMovies, childrensMovies, newReleases, regular)
    
    return moviesList


            
            
        
    
    