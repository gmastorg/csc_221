# CSC221
# M3L1_CanjuraHylton
# Goal: [Gold]

"""
Author: Gabriela Canjura and Marie Hylton
tallies total displays to screen wrties to reciept
"""

from store import Store

def checkOut(cart, outstandingCart, additionalCost):
    """uses list of movie objects and list of rental objects to display movies rented as well as the total cost"""
    
    if cart:
        cart[0].customer.getPayment()
        
        total = 0
        days=3
        purchaseHeader=("RENTAL\tFORMAT\tDAILY RATE\n")
        line=('-'*len(purchaseHeader))
    
        print(purchaseHeader,line)
    
        for item in cart:
            print(item.movie.title+"\t"+item.Format+"\t"+str(item.rate))
            cost = float(item.rate)*days
            total += cost
        
        tax = 1.05 # give 105% of the total basically same as (total*.05)+total
        total = total*tax 
    
        print("\nTotal: $"+'{0:.2f}'.format(total)+"\n")  
        grandTotal='{0:.2f}'.format(total)
    
    elif outstandingCart:
        outstandingCart[0].customer.getPayment()
        
        cart = outstandingCart
        print("Your outsanding Rentals are: ")
        for item in cart:
            print(item.movie.title+"\t"+item.Format+"\t"+str(item.rate))        
        
        cost = additionalCost
        tax = 1.05
        total = cost*tax
        
        print("Additional costs for returning movie after due date: ")
        print("\nTotal: $"+'{0:.2f}'.format(total)+"\n")  
        grandTotal='{0:.2f}'.format(total)

    makeReceipt(cart, cost, grandTotal)
    

def makeReceipt(cart,cost,grandTotal):
    s,header=createHeader()
    '''writes data to receipit in txt file'''
    outfile=open("receipt.txt",'w')#Creates a receipt file to hold rental items.
    spacing=('\n'+'\n'+'\n')
    outfile.write(header+'\n'+spacing)#str(getTransactionTime(s))+spacing)
    tax="5%"
    head='{:<20}'*3
    outfile.write(head.format("MOVIE RENTAL","FORMAT","DAILY RATE")+'\n')
    outfile.write("-"*50+"\n")
    var='{:<20}'
    for item in cart:
        item.movie.title=var.format(item.movie.title)
        item.format=var.format(item.Format)
        item.rate=var.format(str(item.rate))
        strCost='$'+str(cost)
        strTotal='$'+str(grandTotal)
        outfile.write(item.movie.title+item.format+str(item.rate)+'\n')
    outfile.write(spacing*2)
    space='{:<60}'

    outfile.write((var.format('Min. 3 Day SubTotal: '))+(space.format(strCost))+'\n')
    outfile.write((var.format('Tax: '))+(space.format(tax))+'\n')
    outfile.write((var.format('Grand Total: '))+(space.format(strTotal))+'\n')
    outfile.write((spacing*2))    
    
    outfile.write(s.message)

    outfile.close()
    print("Your receipt is ready.")
    #customerRental(cart,cost,grandTotal)

def createHeader():
    s=Store()
    header=str(s)
    return s,header