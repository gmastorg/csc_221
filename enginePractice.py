from customer import Customer
from movie import Movie
from rental import Rental



def createObject():
    c=Customer()
    return c
 ############################CUSTOMER INFORMATION###############################   
def getCustomerInfo():
    firstName=input("First Name: ")
    lastName=input("Last Name: ")
    address=input("Street Adress: ")
    city=input("City: ")
    state=input("State: ")
    zipcode=input("Zip Code: ")
    c=Customer(firstName, lastName, address, city, state, zipcode)
    print('\n',str(c))
    print()
    return c

def getCustomerStatus(c):
    status=c.getCustomerStatus()
    for val in status.values():
        print(val[0],val[1])
    opt=input("\nEnter your customer status: ")
    return status,opt

def getDiscount(c, status,opt):
    for key,value in status.items():
        if  opt==key:
           discount=value[2]
    print("You have earned a ",discount,"% discount.")
 #   return discount

def getPaymentMethod(c):
    payMethod=c.getPayment()
    for val in payMethod.values():
        print(val[0],val[1])
    method=input("How will you pay for your rental(s)?:")
    for key,value in payMethod.items():
        if method==key:
            payment=value[1]
    print("You have selected the following payment method: ",payment)# MEnu
    #return payment


    
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
   # movie.append(title)
    description=Movie.getDescription(m)
    m=Movie(genre,Format,description, title)
    movie.append(m.title)###HELP
    #print(m)
    print("You have selected the following movie infomation: ", str(m))#MEnu
    return m,movie,title

##############################RENTAL INFORMAITON##############################

##############################CHARGES#########################################
def calCharges(m,movie):
   # pass# title, #Format, startDate, dueDate, rate?, rentalRate,lateFee
    #print(title)
    var='{:<20}'
    purchaseHeader=("RENTAL\FORMAT\tRATE\n")
    print(var.format(purchaseHeader))
    print((m.title,m.format,))
    def getRentalDates(Format,rate):
        r=Rental()
        startDate=r.getStartDate()
        dueDate=r.getDueDate()
    
        lateRate=r.getLateRate()
        rentalRate=r.getRentalRate()
        r=Rental(startDate,dueDate,rate)
    line=('-'*len(purchaseHeader))
##    for m in Movie:
##        print(m.title)       
        


#def printCharges():
    print(purchaseHeader,line)
##############################MAIN--TO GO ON MENU/DISPLAY?####################
def main():
  #  c=createObject()
    again='y'
    while again=='y':
        m,genre=getMovieGenre()
        m,Format,rate=getMovieFormat(m)
        m,movie,title=getMovieObject(m,genre,Format)
        calCharges(m,movie)
        #getRentalDates(Format,rate)
        print("Your movies are: ",movie,'\nAdd another movie?')
        again=input('y/n\n')
 #   calCharges(m, movie)
    c=getCustomerInfo()
    status,opt=getCustomerStatus(c)
    getDiscount(c, status,opt)
    getPaymentMethod(c)
 #   printCharges(movie)
    

main()

