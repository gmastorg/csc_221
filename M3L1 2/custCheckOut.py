import display
import login as l
import validateInput as v
import customer as c
from movies import Movie
from rental import Rental

from store import Store

########################LOGIN############################################
def login():
    maxOption = 2
    pass
##    print(display.welcomeMessage())
##    choice = input(display.loginMenu())
##    while v.validateNull(choice) == False:#validates input
##        choice = input(display.loginMenu())
##    while v.validateText(choice, maxOption) == False:
##        display.invalidInput()
##        choice = input(display.loginMenu())
##    decision = int(choice)# uses user input to login or create account       
##    l.loginDecision(decision)
########################################################################
def createHeader():
    s=Store()
    header=str(s)
    print(header)#Needs alignment work.
    return s,header
########################CHOICE############################################
def mainChoice():
    menu="1. RENT\n 2. RETURN\n 3. EXIT\n"
 
    print("\nChoose an option:\n\n",menu,)
    option=input("Enter '1', '2', or '3': ")
    if option=='1':
        getRentals()
    elif option=='2':
        pass
    elif option=='3':
        exit
    else:
        print("Enter a valid choice.")

def getRentals():
    movies,rates=getMovie()
    cost,grandTotal=checkOut(movies,rates)
    c.Customer.getPayment()
    makeReceipt(movies, rates, cost, grandTotal)

def getReturns():
    pass
########################GENRECHOICES#######################################
def getGenre():
    m=Movie()
    genre=m.getMovieGenre()
    return genre
#####################INCOMPLETE: SEARCHMOVIES############################################
def searchMovies():
#for search in movies:
    #print(search)
#print("You have selected the following movies: ")
#pass "m" through and print: title, format
#
    pass
#####################MOVIECHOICE############################################
def getMovie():
    movie=[]
    rates=[]
    again='y'
    while again=='y':
        m=Movie()#creates empty object to call methods from class
        title='Hallmark Christmas'#convert to film title from movieList
        genre=getGenre()
        Format,rate=getFormat()
        year=2011#convert to year from movieList
        m=Movie(genre,Format,title,m.description,year,genre,Format,rate)
        movie.append(m)
        r=Rental()
        r=Rental(r.startDate,r.dueDate,m.rate,r.getRentalRate())#obtains and displays rental information per movie
        rates.append(r)
        again=input("\nAdd another movie?(y/n)\n")
        again=again.lower()
    
    return movie,rates
########################FORMATCHOICE#####################################
def getFormat():
    m=Movie()
    Format,rate=m.getMovieFormat()
    return Format,rate

###########################calCharges#####################################
def checkOut(movies, rates):
    """uses list of movie objects and list of rental objects to display movies rented as well as the total cost"""
    total = 0
    purchaseHeader=("RENTAL\tFORMAT\tRATE\n")
    line=('-'*len(purchaseHeader))
    
    print(purchaseHeader,line)
    
    for item in movies:
        print(item.title+"\t"+item.Format+"\t"+str(item.rate))
        
    for item in rates:
        cost = item.rate*item.days
        total += cost
    tax = 1.05 # give 105% of the total basically same as (total*.05)+total
    total = total*tax 
    
    print("\nTotal: $"+'{0:.2f}'.format(total)+"\n")  
    grandTotal='{0:.2f}'.format(total)
    return cost, grandTotal

###########################RECEIPT MOVE TO CLASS #############################
def makeReceipt(movies,rates,cost,grandTotal):
    s,header=createHeader()
    '''writes data to receipit in txt file'''
    outfile=open("receipt.txt",'w')#Creates a receipt file to hold rental items.
    spacing=('\n'+'\n'+'\n')
    outfile.write(header+'\n'+spacing)#str(getTransactionTime(s))+spacing)
    tax="5%"
    head='{:<20}'*3
    outfile.write(head.format("MOVIE RENTAL","FORMAT","RATE")+'\n')
    outfile.write("-"*50+"\n")
    var='{:<20}'
    for item in movies:
        item.title=var.format(item.title)
        item.format=var.format(item.Format)
        item.rate=var.format(str(item.rate))
        strCost='$'+str(cost)
        strTotal='$'+str(grandTotal)
        outfile.write(item.title+item.format+str(item.rate)+'\n')
    outfile.write(spacing*2)
    space='{:<60}'

    outfile.write((var.format('Total: '))+(space.format(strCost))+'\n')
    outfile.write((var.format('Tax: '))+(space.format(tax))+'\n')
    outfile.write((var.format('Grand Total: '))+(space.format(strTotal))+'\n')
    outfile.write((spacing*2))    
    
    outfile.write(s.message)

    outfile.close()
    print("Your receipt is ready.")
    
###########################MAIN###########################################

def main():
    login()
    createHeader()
    mainChoice()
main()
#########################CUSTOMEROBJECT########################################
def customerRental(m,r,):
    c=Customer('Marie', 'Hylton','123','ftb','nc','123456')#pass this in when finished.
    custRental=Customer(c.getCustomerName(),m.title,m.Format,r.startDate,r.dueDate)
 
