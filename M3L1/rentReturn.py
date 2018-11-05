# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 13:15:17 2018

@author: canjurag4010
"""

import listBuilder as listB
import display
import validateInput as v
import rental as r


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
    if decision == 5:
        rentMovie(movieList)

def newReleases(newReleases):
    
    for item in newReleases:
        print(str(item))
    
    rentMovie(newReleases)
    
def regular(regular):
    
    for item in regular:
        print(str(item))
    
    rentMovie(regular)

def childrens(childrens):
    
    for  item in childrens:
        print(str(item))

    rentMovie(childrens)
    
def allMovies (movieList):

    for item in movieList:      
        print(str(item))
        
    rentMovie(movieList)
    
def rentMovie(moviesList):
    
    movie = input(display.movieName())
    
    for item in moviesList:
        if movie == item.title:
            selectedMovie = item
        else:
            display.invalidInput()
    
def getRateAndFormat(selectedMovie):
    
        #choice=input("Add movie to your queue? (y/n)\n")
        #choice=choice.lower()
        Format,rate=getFormat()
        if choice=='y':
            m=Movie()
            title=search
            m.genre=genre
            m.Format=Format
            m.rate=rate
            year=row[3]
            m=Movie(title, m.description, year, m.genre,m.Format,m.rate)
            print(m)
            movies.append(m)
            r=Rental()
            r=Rental(r.startDate,r.dueDate,m.rate)#obtains and displays rental information per movie
            rates.append(r)
            #again=input("Add another movie? (y/n)\n")
            #again=again.lower()
    
    
