# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 13:15:17 2018

@author: canjurag4010
"""

import listBuilder as listB
import display
import validateInput as v


def rentReturnDecision(decision):
    
    if decision == 1:
        rentMovieMenu()
    if decision == 2:
        returnMovie()

def returnMovie():
    
    print("return")

def rentMovieMenu():
    
    maxOption = 4
    
    decision = v.menu(display.searchMovies(),maxOption)
    
    genreDecision(decision)
        
def genreDecision(decision):
    movieList =[]
    
    movieList = listB.getMovieLists()
    
    if decision == 1:
        newReleases(movieList[0])    
    if decision == 2:
        regular(movieList[1])
    if decision == 3:
        childrens(movieList[2])
    if decision == 4:
        allMovies(movieList)

def newReleases(newReleases):
    genre = "newRelease"
    
    for item in newReleases:
        print(str(item))
    
    rentMovie(newReleases, genre)
    
def regular(regular):
    genre = "regular"
    
    for item in regular:
        print(str(item))
    
    rentMovie(regular, genre)

def childrens(childrens):
    genre = "childrens"
    
    for  item in childrens:
        print(str(item))

    rentMovie(childrens, genre)
    
def allMovies (movieList):

    for item in movieList:
        if item.genre == "Animation":
            genre = "childrens"
        if item.year == "2011":
            genre = "new release"
        else:
            genre = "regular"
        
        print(str(item))
        
    rentMovie(movieList, genre)
    
def rentMovie(moviesList, genre):
    
    movie = input(display.movieName()).Lower()
    
    for item in moviesList:
        if movie == item.title:
            selectedMovie = item
        else:
            display.invalidInput()
        

    