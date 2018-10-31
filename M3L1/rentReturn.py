# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 13:15:17 2018

@author: canjurag4010
"""

import listBuilder as listB
from customer import Customer
import display
import validateInput as v
from movies import Movie
from rental import Rental
from store import Store

def rentReturnDecision(decision):
    
    if(decision == 1):
        rentMovie()
    if(decision ==2):
        returnMovie()

#def returnMovie():
    
    #return movie code

def rentMovie():
    
    moviesList = listB.getMovieLists() 
    
    maxOption = 4
    
    decision = v.menu(display.searchMovies(),maxOption)    
    
    
    
    outfile=open("receipt.txt",'w')#Creates a receipt file to hold rental items.

    movie = []
    rates = []
    
    #creates empty object to call methods from class
    
    
    m, genre=Movie.getMovieGenre(m)
    m,Format,rate=Movie.getMovieFormat(m)
    m = getMovieObject(m,genre,Format,rate)
    movie.append(m)
    #obtains and displays rental information per movie 
    r=Rental()
    r = Rental.getRentalDates(r,Format,rate)
    rates.append(r)
    print(str(r))
    
    maxOption = 3
    decision = v.menu(display.rentReturnMenu(),maxOption)
    rentReturnDecision(decision)

    cost,grandTotal=calCharges(movie,rates)
    
    Customer.getPayment()
    s=printHeader(outfile)
    printPurchase(outfile,movie,rates,s,cost,grandTotal) 

def getMovieObject(m,genre,Format,rate):
    """creates movie objects"""
    title=input("Movie Title: ")  
    description=Movie.getDescription(m)
    m = Movie(genre,Format,description, title, rate)
    
    print("You have selected the following movie infomation: ", str(m))#MEnu
    
    return m

def calCharges(movies, rates):
    """uses list of movie objects and list of rental objects to display movies rented as well as the total cost"""

    total = 0
    
    purchaseHeader=("RENTAL\tFORMAT\tRATE\n")
    line=('-'*len(purchaseHeader))
    
    print(purchaseHeader,line)
    
    for item in movies:
        print(item.title+"\t"+item.format+"\t"+str(item.rate))
        
    for item in rates:
        cost = item.rate*item.days
        total += cost
    tax = 1.05 # give 105% of the total basically same as (total*.05)+total
    total = total*tax 
    
    print("\nTotal: $"+'{0:.2f}'.format(total)+"\n")  
    grandTotal='{0:.2f}'.format(total)
    return cost, grandTotal

def printHeader(outfile):
    """creates header for reciept"""
    spacing=('\n'+'\n'+'\n')#Receipt spacing
    
    s=Store()
    storeName=Store.getName(s)
    location=Store.getFullAddress(s)
    time=Store.getTransactionTime(s)
    hours=Store.getHours(s)
    number=Store.getPhone(s)
    website=Store.getWebsite(s)
    
    header=(storeName+'\n'+location+'\n'+hours+'\n'+number+'\n'+website+spacing)
    outfile.write(header.center(80)+'\n'+str(time)+spacing)
    return s, outfile    

def printPurchase(outfile,movie, rates,s,cost,grandTotal):
    """writes data to reciept in .txt file"""
    
    spacing=('\n'+'\n'+'\n')#Receipt spacing
    survey=Store.getMessage(s)
    tax="5%"
    header='{:<20}'*3
    outfile.write(header.format("MOVIE RENTAL","FORMAT","RATE")+'\n')
    outfile.write("-"*50+"\n")
    var='{:<20}'
    for item in movie:
        item.title=var.format(item.title)
        item.format=var.format(item.format)
        item.rate='$'+var.format(str(item.rate))
        strCost='$'+str(cost)
        strTotal='$'+str(grandTotal)
        outfile.write(item.title+item.format+str(item.rate)+'\n')
    outfile.write(spacing*2)
    space='{:<60}'

    outfile.write((var.format('Total: '))+(space.format(strCost))+'\n')
    outfile.write((var.format('Tax: '))+(space.format(tax))+'\n')
    outfile.write((var.format('Grand Total: '))+(space.format(strTotal))+'\n')
    outfile.write((spacing*2))    
    
    outfile.write(survey)

    outfile.close()
    print("Your receipt is ready.")
    