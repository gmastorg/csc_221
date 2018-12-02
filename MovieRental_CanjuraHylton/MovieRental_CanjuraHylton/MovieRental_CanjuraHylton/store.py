# CSC221
# M3L1_CanjuraHylton
# Goal: [Gold]

"""
store class displays store data
"""

from datetime import datetime

class Store(object):
    def __init__(self, name='', address='', city='', state='', zipcode='', hours='', phone='',website='',message=''):
        self.name=('RedFox Movie Rentals')
        self.address="123 Carolina Lane"
        self.city="Fayetteville"
        self.state="North Carolina"
        self.zipcode="12345"
        self.hours="Hours: 10:00-20:00 Sun, 09:00-20:00, Mon-Sat"
        self.phone="Phone: (555)-867-5309"
        self.website="Visit us: www.redfoxrentals.com"
        self.message="Thank you for renting with RedFox Rentals.\nWe enjoy serving "\
               "the best customers in the world!\n"

    def getFullAddress(self):#Full Address for CSV,site,and receipt
        text='{:^80}'.format(str(self.address+'\n'))+str(self.city+', '+self.state)
        return text+" "+str(self.zipcode)
    
    def getTransactionTime(self):#TimeStamp
        return datetime.now()
        
    def getMessage(self):#Message at bottom of paper receipts
        return "Thank you for renting with RedFox Rentals.\nWe enjoy serving "\
               "the best customers in the world!\nPlease provide us with your\n"\
               "feedback:  https://www.surveyape.com\n"

    def __str__(self):#Prints Header for site and receipt
        text='{:^80}'.format(str(self.name))+'\n'+str(self.getFullAddress())
        text+='\n'+'{:^100}'.format(str(self.hours))+'{:^30}'.format(str(self.phone))
        text+='\n'+'{:^90}'.format(str(self.website))
        return text
        