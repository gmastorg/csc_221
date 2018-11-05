# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 13:07:30 2018

@author: canjurag4010
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
        if item.year == "2011":
            item.genre = "new release"
            newReleases.append(item)
        else:
            item.genre = "regular"
            regular.append(item)
    
    moviesList.append(newReleases)
    moviesList.append(regular)
    moviesList.append(childrens)
    

    return moviesList


            
            
        
    
    
