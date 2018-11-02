# CSC221
# M3L1_CanjuraHylton
# Goal: [Gold]

"""
customer movie rental objects verifies if returned or not
"""

class CustomerRentals():
    
     def __init__(self,title,rate,Format,startDate,wasReturned):
        self.startDate=startDate
        self.rate=rate
        self.Format = Format
        self.title = title
        self.wasReturned = wasReturned
        