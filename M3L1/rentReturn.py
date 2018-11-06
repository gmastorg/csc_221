# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 13:15:17 2018

@author: canjurag4010
"""

import listBuilder as listB
import display
import validateInput as v
import rental as r

def rentReturnDecision(customer, decision):
    
    if decision == 1:
        return rentMovieMenu(customer)
    if decision == 2:
        returnMovie(customer)

def returnMovie(customer):
    
    print("return")

def rentMovieMenu(customer):
    
    maxOption = 5
    
    decision = v.menu(display.searchMovies(),maxOption)
    
    return movieSelection(customer,decision)
    
        
def movieSelection(customer,decision):
    movieList =[]
    
    movieList = listB.getMovieLists()
    
    if decision == 1:
        selectedMovie = newReleases(movieList)    
    if decision == 2:
        selectedMovie = regular(movieList)
    if decision == 3:
        selectedMovie = childrens(movieList)
    if decision == 4:
        selectedMovie = allMovies(movieList)
    if decision == 5:
        selectedMovie = rentMovie(movieList)
        
    return getRateAndFormat(customer, selectedMovie)

def newReleases(movieList):
    
    for item in movieList[0]:
        print(str(item))
    
    return rentMovie(movieList)
    
def regular(movieList):
    
    for item in movieList[1]:
        print(str(item))
    
    return rentMovie(movieList)

def childrens(movieList):
    
    for  item in movieList[2]:
        print(str(item))

    return rentMovie(movieList)
    
def allMovies (movieList):

    for item in movieList[0]:     
        print(str(item))
    
    for item in movieList[1]:     
        print(str(item))
    
    for item in movieList[2]:     
        print(str(item))    
        
    return rentMovie(movieList)
    
def rentMovie (movieList):

    movie = input(display.movieName())
    
    for item in movieList[0]:
        if movie == item.title:
            selectedMovie = item
    
    for item in movieList[1]:
        if movie == item.title:
            selectedMovie = item          
    
    for item in movieList[2]:
        if movie == item.title:
            selectedMovie = item
            
    if not selectedMovie:
        print(movie, "is not an available movie.")
        rentMovie(movieList)
    
    return selectedMovie
    
def getRateAndFormat(customer, selectedMovie):
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

    rental = r.Rental(Format, rate, selectedMovie, customer)
    
    outfile = open(customer.customerLogin.filename, 'a')
    
    outfile.write(rental.movie.title+","+str(rental.Format)+","+str(rental.startDate)+"\n")
    
    outfile.close()
    
    print(str(rental))
    
    return rental
    

    
    
    
