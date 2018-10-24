from customer import Customer

   

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