from customer import Customer
from movies import Movie
from rental import Rental

   
################################## MOVIE INFORMATION############################
def getMovieGenre():
    m=Movie()
    gen=Movie.getGenre(m)
    for val in gen.values():
        print(val[0],val[1])
    genre=input("Select genre: ")
    for key, value in gen.items():
        if genre==key:
            print("You have selected the following movie genre: ", value[1] )
            genre=value[1]#   m=getMovieObject()])#MEnu
    return m,genre

def getMovieFormat(m):
    For=Movie.getFormat(m)
    for val in For.values():
        print(val[0],val[1])
    Format=input("Select format: ")
    for key, value in For.items():
        if Format==key:           
            print("You have selected the following movie format: ",value[1])#MEnu
            rate=value[2]
            Format=value[1]
    return m,Format,rate

def getMovieObject(m,genre,Format):
    movie=[]
    title=input("Movie Title: ")
    description=Movie.getDescription(m)
    m=Movie(genre,Format,description, title)
    movie.append(m)###HELP
    #print(m)
    print("You have selected the following movie infomation: ", str(m))#MEnu
    return m,movie,title

##############################RENTAL INFORMAITON##############################
def getRentalDates(Format,rate):
    r=Rental()
    startDate=r.getStartDate()
    print("Start Date:",startDate)
    dueDate=r.getDueDate()
    print("Return Date",dueDate)
    lateRate=r.getLateRate()
    rentalRate=r.getRentalRate()
    r=Rental(startDate,dueDate,rate)
    print("The movie rental rate for ",Format,"is: $",rate," per day.")
    print(str(r))
 #   rentalRate
##############################CHARGES#########################################
def calCharges(m,movie):
   # pass# title, #Format, startDate, dueDate, rate?, rentalRate,lateFee
    #print(title)
    purchaseHeader=("RENTAL\tFORMAT\tRATE\n")
    line=('-'*len(purchaseHeader))
##    for m in Movie:
##        print(m.title)       
    
        


#def printCharges():
    print(purchaseHeader,line)
##############################MAIN--TO GO ON MENU/DISPLAY?####################
def main():
  #  c=createObject()
    again='y'
    
    
    c=getCustomerInfo()
    status,opt=getCustomerStatus(c)
    getDiscount(c, status,opt)
    getPaymentMethod(c)
    while again=='y':
        m,genre=getMovieGenre()
        m,Format,rate=getMovieFormat(m)
        m,movie,title=getMovieObject(m,genre,Format)
        calCharges(m,movie)
        getRentalDates(Format,rate)
        for item in movie:
            print("Your movies are: ",item.title)
        print('\nAdd another movie?')
        again=input('y/n\n')
 #   printCharges(movie)
    

main()