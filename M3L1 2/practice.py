from datetime import timedelta, date,time, datetime

from rental import Rental

print(datetime.now())#date and time
print(time())#zeros
#print(time.now())
print("hello")
print(datetime.now().time())#just the time

print('\npractice\n')
r=Rental()

print(r.startDate)#
print(r.dueDate)#
print(r.rate)
print(r.getLateRate())#
print(r.getRentalRate())#
print(str(r))


