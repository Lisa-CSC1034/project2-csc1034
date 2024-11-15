from datetime import datetime, timedelta, time


class Booking:

 #constructor


 def __init__(self, room, start, hours, title, contact):
     # instance variables (private)
     self.__room=room
     self.__start=start
     self.__hours=hours
     self.__title=title
     self.__contact=contact

     #validating the inputs
     #check room is of type string
     if not isinstance(room,str):
         raise TypeError("Room should be of type string")

     #check if start is of type datetime
     if not isinstance(start,datetime):
         raise TypeError("Start should be of type datetime")

     #check if hours is of type int
     if not isinstance(hours,int):
         raise TypeError("Hours should be of type int")

     #check if title is of type string
     if not isinstance(title,str):
         raise TypeError("Title should be of type string")

     #check if contact is of type string
     if not isinstance(contact,str):
         raise TypeError("Contact should be of type string")

     #make sure booking on saturday or sunday is incorrect
     if start.weekday()==5 or start.weekday()==6:
         raise TypeError("Not available on the weekends")

     #check if time is valid
     valid_start_time=time(9,00)
     valid_end_time=time(18,00)

     #add the length of hours to the time to avoid incorrect booking
     booking_start_time_extra_hour=start + timedelta(hours=1)
     booking_start_time_extra_hour=booking_start_time_extra_hour.time()

     if valid_start_time >= start.time() or valid_end_time <booking_start_time_extra_hour:
         raise TypeError("Incorrect time")


#getter for room
 def get_room(self):
  return self.__room
 #getter for start
 def get_start(self):
  return self.__start
 #getter for hours
 def get_hours(self):
  return self.__hours
 #getter for title
 def get_title(self):
  return self.__title
 #getter for contact
 def get_contact(self):
  return self.__contact

#as appears to user
 def __str__(self):
  return f'Booking is {self.__room}, starting at {self.__start}, for {self.__hours}, the course is called {self.__title}, and staff contact details are {self.__contact}'

#as  appears to developer
 def __repr__(self):
  return f'Booking is {self.__room},{self.__start},{self.__hours},{self.__title},{self.__contact}'


 def __eq__(self, other):
  if not isinstance(self,other):
      return False

  return self.__room == other.room and self.__start == other.start and self.__hours == other.hours and self.__title == other.title and self.__contact == other.contact

 def __hash__(self):
  return hash((self.__room,self.__hours,self.__title,self.__contact))

#check for overlap bookings
 def overlaps_with(self, other):
  if self.__room != other.get_room():
      return False

  if self.__start.weekday() != other.get_start().weekday():
      return False

  current_time_end = self.__start + timedelta(hours=self.__hours)
  other_time_end = other.get_start() + timedelta(hours=other.get_hours())

  return max(self.__start,other, other.get_start()) <min(current_time_end, other_time_end)




#################### testing ##########################

import unittest
from datetime import datetime

#a bad booking
class TestBooking(unittest.TestCase):
 def test_bad_booking(self):
     try:
        Booking('FDC.G.41',datetime.strptime("14/11/2024, 11:35", "%d/%m/%Y, %H:%M"),1,'Lecture CSC1034','jennifer.warrender@newcastle.ac.uk')
     except TypeError:
        print("fails as expected")
     else:
        print("should have failed")



#a booking that works
 def test_good_booking(self):
     try:
         Booking('FDC.G.41',datetime.strptime("22/11/2024, 09:30", "%d/%m/%Y, %H:%M"),1,'Lecture CSC1034','jennifer.warrender@newcastle.ac.uk')
     except TypeError:
        print("works as expected")
     else:
        print("should have worked")


def test_bad_booking():
    pass


def main():
    test_bad_booking()

if __name__ == "__main__":
    unittest.main()
