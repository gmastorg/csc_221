# CSC221
# M3L1_CanjuraHylton
# Goal: [Gold]

"""
store class displays store data
"""

from datetime import datetime

class Store(object):
    def __init__(self, name='', address='', city='', state='', zipcode='', hours='', phone='',website='',message=''):
        self.name=name
        self.address=address
        self.city=city
        self.state=state
        self.zipcode=zipcode
        self.hours=hours
        self.phone=phone
        self.website=website
        self.message=message
        
    def getName(self):
        return "RedFox Movie Rentals"

    def getFullAddress(self):
        self.address="123 Carolina Lane"
        self.city="Fayetteville"
        self.state="North Carolina"
        self.zipcode="12345"
        text=str(self.address)+'\n'+str(self.city)+','+str(self.state)
        return text+" "+str(self.zipcode)

    def getPhone(self):
        return "555-867-5309"
    
    def getTransactionTime(self):
        return datetime.now()
        
    def getHours(self):
        return "10:00-20:00, Sun\n09:00-20:00, Mon-Sat"

    def getWebsite(self):
        return "www.redfoxrentals.com"

    def getMessage(self):
        return "Thank you for renting with RedFox Rentals.\nWe enjoy serving "\
               "the best customers in the world!\nPlease provide us with your\n"\
               "feedback:  https://www.surveyape.com\n"