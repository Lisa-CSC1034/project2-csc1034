import unittest
from datetime import datetime

import csv

from booking import Booking

from booking_manager import BookingManager


from booking_manager import load_from_file

from booking_manager import BookingManager, add_booking


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
         Booking('FDC.G.41','22/10/2024, 09:00',1,'Lecture CSC1034','jennifer.warrender@newcastle.ac.uk')
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
