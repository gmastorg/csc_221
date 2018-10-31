#Checkout

from customer import Customer
from rental import Rental
from movies import Movie

c=Customer()
c=Customer(getCustomerName(),getBilling(),getPayment())
print(c)
custRent=Rental()
custRent=Rental(str(c))
print("You have selected the following movies: ")#,movieList)
      


