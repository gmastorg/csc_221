# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 13:15:17 2018

@author: canjurag4010
"""

import listBuilder as listB
import display
import validateInput as v
import rental as r

def rentReturnDecision(filename, decision):
    
    if decision == 1:
        rentMovieMenu(filename)
    if decision == 2:
        returnMovie(filename)

def returnMovie(filename):
    
    print("return")

def rentMovieMenu(filename):
    
    maxOption = 5
    
    decision = v.menu(display.searchMovies(),maxOption)
    
    genreDecision(filename,decision)
        
def genreDecision(filename,decision):
    movieList =[]
    
    movieList = listB.getMovieLists()
    
    if decision == 1:
        newReleases(filename,movieList)    
    if decision == 2:
        regular(filename, movieList)
    if decision == 3:
        childrens(filename, movieList)
    if decision == 4:
        allMovies(filename, movieList)
    if decision == 5:
        rentMovie(filename, movieList)

def newReleases(filename, movieList):
    
    for item in movieList[0]:
        print(str(item))
    
    rentMovie(filename, movieList)
    
def regular(filename, movieList):
    
    for item in movieList[1]:
        print(str(item))
    
    rentMovie(filename, movieList)

def childrens(filename, movieList):
    
    for  item in movieList[2]:
        print(str(item))

    rentMovie(filename, movieList)
    
def allMovies (filename, movieList):

    for item in movieList[0]:     
        print(str(item))
    
    for item in movieList[1]:     
        print(str(item))
    
    for item in movieList[2]:     
        print(str(item))    
        
    rentMovie(filename, movieList)
    
def rentMovie(filename, movieList):

    movie = input(display.movieName())
    
    for item in movieList[0]:
        if movie == item.title:
            selectedMovie = item
        else:
            display.invalidInput()
    
    for item in movieList[1]:
        if movie == item.title:
            selectedMovie = item
        else:
            display.invalidInput()
    
    for item in movieList[2]:
        if movie == item.title:
            selectedMovie = item
        else:
            display.invalidInput()
        
    getRateAndFormat(filename, selectedMovie)
    
def getRateAndFormat(filename, selectedMovie):
    #shouldn't the genre effect the price
    #{menuChoice:heading,format,formatprice}
    For={'1':['1.', 'VHS',1],
         '2':['2.', 'DVD',3],
         '3':['3.', 'BluRay',4],
         '4':['4.', 'Stream',5]}
        
    maxOption = 0
    
    for val in For.values():
        print(val[0],val[1])
        maxOption += 1
            
    Format=input("Select format: ")
    while v.validateNull(Format)==False or v.validateText(Format, maxOption)==False:
        Format=input("Select format: ")
        
    for key, value in For.items():
        if Format==key:           
            print("You have selected the following movie format: ",value[1])
            rate=value[2]
            Format=value[1]

    rental = r.Rental(Format, rate, selectedMovie)
    
    outfile = open(filename, 'a')
    
    outfile.write(rental.movie.title+","+str(rental.Format)+","+str(rental.startDate)+"\n")
    
    outfile.close()
    
    print(str(rental))
    
    
    

    
    
    
