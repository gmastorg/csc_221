# CSC221
# M3L1_CanjuraHylton
# Goal: [Gold]

"""
Author: Gabriela Canjura and Marie Hylton
goes through rental and return processes 
"""
import listBuilder as listB
import display
import validateInput as v
import rental as r
from datetime import timedelta, date , datetime

def returnMovie(cart, oCart, customer, returned):
    """return method"""
    additionalCost = 0
    oCart = listB.getOutstandingRentals(customer)
        
    if not oCart:
        print("You have no outstanding rentals.")
        
    else:
        outfile = open(oCart[0].customer.customerLogin.filename, 'w')
        outfile.write(oCart[0].customer.firstName+","+oCart[0].customer.lastName+","+ 
                  oCart[0].customer.address+","+ oCart[0].customer.city+","+
                  oCart[0].customer.state+","+ oCart[0].customer.zipcode+"\n")

        movie = input("Enter the name of the movie you would like to return: ")
        
        index = 0 
        
        for item in oCart:
            if movie == item.movie.title:
                returned.append(item)
                returnDate = datetime.now()
                additionalCost = getAdditionalCosts(returnDate, item)
                additionalCost = int(additionalCost)
                oCart.pop(index)
                index += 1 
            else:
                returnDate = ""
                oCart.append(item)
                
            outfile.write(item.movie.title+","+str(item.movie.genre)+","+
                  str(item.movie.year)+","+str(item.Format)+","+
                  str(item.rate)+','+str(item.startDate)+','+
                  str(returnDate)+"\n")
        
        outfile.close()
        
        for item in cart:
            appendToFile(item)
        
    return oCart, additionalCost, returned

def getAdditionalCosts(returnDate, item):
    
    if item.dueDate < returnDate:
        delta = returnDate - item.dueDate
        days = delta.days
        additionalCost = days*item.rate
    else: 
        additionalCost = 0
       
    return additionalCost
def rentMovieMenu(customer):
    """menu for option to search for movies"""
    maxOption = 5
    
    decision = v.menu(display.searchMovies(),maxOption)
    
    rental = movieSelection(customer,decision)
   
    return rental
    
        
def movieSelection(customer,decision):
    """calls methods corresponding to menu"""
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
        
    rental= getRateAndFormat(customer, selectedMovie)
    
    return rental

def newReleases(movieList):
    """prints new relases and searches new releases"""
    for item in movieList[0]:
        print(str(item))
    
    return rentMovie(movieList)
    
def regular(movieList):
    """prints regular and searches regular releases"""
    for item in movieList[1]:
        print(str(item))
    
    return rentMovie(movieList)

def childrens(movieList):
    """prints childrens and searches childrens"""
    for  item in movieList[2]:
        print(str(item))

    return rentMovie(movieList)
    
def allMovies (movieList):
    """prints all movies and searches all movies"""
    for item in movieList[0]:     
        print(str(item))
    
    for item in movieList[1]:     
        print(str(item))
    
    for item in movieList[2]:     
        print(str(item))    
        
    return rentMovie(movieList)
    
def rentMovie (movieList):
    """user types in the movie name and it says if movie is available"""
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
   
    """need to fix this doesn't work just crashes"""        
    if not selectedMovie:
        print(movie, "is not an available movie.")
        rentMovie(movieList)
    
    return selectedMovie
    
def getRateAndFormat(customer, selectedMovie):
    """gets the format option from the customer and creates rental objects"""
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
    startDate = date.today()
    
    rental = r.Rental(Format, rate, startDate, selectedMovie, customer)
    
    appendToFile(rental)
    
    print(str(rental))
    
    return rental

def appendToFile(rental):
  
    outfile = open(rental.customer.customerLogin.filename, 'a')
    
    outfile.write(rental.movie.title+","+str(rental.movie.genre)+","+
                  str(rental.movie.year)+","+str(rental.Format)+","+
                  str(rental.rate)+','+str(rental.startDate)+"\n")
    
    outfile.close()
    
    
    

    
    
    
