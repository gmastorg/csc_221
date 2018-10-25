
import string
import display
import login as l
import customer as c
from movies import Movie
from rental import Rental
from store import Store

outfile=open("receipt.txt",'w')#Creates a receipt file to hold rental items.
spacing=('\n'+'\n'+'\n')#Receipt spacing


def main():
    '''runs the program, integrating all classes involved'''
    again='y'#Used for a control loop.
    movie = []#Holds a list of movie objects
    rates = []#Holds a list of rental objects
    
    display.welcomeMessage()
    display.loginMenu()#User can log in or 
    choice = input()
    #validates input
    while not choice:
        display.loginMenu()
        choice = input()
    while choice not in string.digits or int(choice) > 2:
        display.invalidInput()
        display.loginMenu()
        choice = input()
    decision = int(choice)
        
    l.loginDecision(decision)
    
    while again=='y':
        m=Movie()
        m, genre=Movie.getMovieGenre(m)
        m,Format,rate=Movie.getMovieFormat(m)
        m = getMovieObject(m,genre,Format,rate)
        movie.append(m)
         
        r=Rental()
        r = Rental.getRentalDates(r,Format,rate)
        rates.append(r)
        print('\nAdd another movie?')
        again=input('y/n\n')
        
    cost,grandTotal=calCharges(movie,rates)
    
    c.Customer.getPayment()
    s=printHeader()
    printPurchase(movie,rates,s,cost,grandTotal)
def getMovieObject(m,genre,Format,rate):
 
    title=input("Movie Title: ")  
    description=Movie.getDescription(m)
    m = Movie(genre,Format,description, title, rate)
    
    print("You have selected the following movie infomation: ", str(m))#MEnu
    
    return m

def calCharges(movies, rates):
    
    total = 0
    
    purchaseHeader=("RENTAL\tFORMAT\tRATE\n")
    line=('-'*len(purchaseHeader))
    
    print(purchaseHeader,line)
    
    for item in movies:
        print(item.title+"\t"+item.format+"\t"+str(item.rate))
        
    for item in rates:
        cost = item.rate*item.days
        total += cost
    
    total = total*1.05
    
    print("\nTotal: $"+'{0:.2f}'.format(total)+"\n")
    grandTotal='{0:.2f}'.format(total)
    return cost, grandTotal

def printHeader():
    
    s=Store()
    storeName=Store.getName(s)
    location=Store.getFullAddress(s)
    time=Store.getTransactionTime(s)
    hours=Store.getHours(s)
    number=Store.getPhone(s)
    website=Store.getWebsite(s)
    
    header=(storeName+'\n'+location+'\n'+hours+'\n'+number+'\n'+website+spacing)
    outfile.write(header.center(80)+'\n'+str(time)+spacing)
    return s    

def printPurchase(movie, rates,s,cost,grandTotal):
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
    
 

    
main()
