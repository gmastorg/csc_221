from customer import Customer
from movie import Movie
from rental import Rental



OUTFILE=open("receipt.txt",'w')
   

def writeHeader():
    pass


def printItems():
    OUTFILE.write("-"*80+"\n")
    OUTFILE.write("RENTAL\tFORMAT\tRATE")
    OUTFILE.write("-"*80+"\n")
    #for i in range (0,len(title)):
 #       OUTFILE.write(title[i])
    print("Your receipt is ready.")
    


        

def main():
 #   writeheader()
    printItems()
    OUTFILE.close()


main()
