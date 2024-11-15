#import class and datetime

from datetime import datetime, timedelta

from booking import Booking


import csv




#create a class
class BookingManager:

 def __init__(self, bookings=None):
  if bookings is None:
      self.bookings=[]
  else:
      self.bookings = bookings

def get_bookings(self):
  return self.bookings

#for the users
def __str__(self):
  return f'Booking is {self.bookings}'

#for the developers
def __repr__(self):
  return f'({self.bookings})'

 #create booking
def add_booking(self, booking):
     booking_available = True
     for booking_check in self.bookings:
         if booking.room == booking_check.room:
             booking_available = False

         if booking_available is True:
            self.bookings.append(booking)

 #delete booking
def remove_booking(self, booking):
  if booking in self.bookings:
      self.bookings.remove(booking)

 #edit booking
def edit_booking(self, old_booking, new_booking):
    booking_available = True
    for booking_check in self.bookings:
        if Booking.get_room == booking_check.room:
            booking_available = False

    if booking_available is True:
        old_booking /= new_booking

def search_by_room(self, room):
    matching_bookings = []

    for booking in self.bookings:
        if booking.get_room() == room:
            matching_bookings.append(booking)

    return matching_bookings


def search_by_start(self, start):
     matching_bookings = []

     for booking in self.bookings:
         if booking.get_start() == start:
             matching_bookings.append(booking)

     return matching_bookings

def search_for_room_timetable(self, date_from, date_to, room):
    matching_bookings = []

    for booking in self.bookings:
        if booking.get_room() == room and date_from <= booking.get_start() <= date_to:
            matching_bookings.append(booking)

    return matching_bookings

#find available rooms
def get_available_rooms(self, start, hours, all_rooms):
     self.all_rooms=all_rooms
     start_time = datetime.strptime(start, '%d/%m/%Y, %H:%M')
     end_time = start_time + timedelta(hours=hours)
     available_rooms = []

     #check rooms bookings
     for room, bookings in all_rooms.item():
        is_available = True
        for booking in bookings:
             booking_start = datetime.strptime(booking[0], 'd%/m%/%Y, %H:%M')
             booking_end = datetime.strptime(booking[1], '%d/%m/%Y, %H:%M')

             if start_time < booking_end and end_time > booking_start:
                 is_available = None

        if is_available:
            self.available_rooms.append(room)

     return self.available_rooms

#load saved/downloaded file for booking information
def load_from_file(self, file_name):
    data_file = open(file_name,"r")
    date_lines = data_file.readlines()
    data_lines = date_lines[1:]

    for line in data_lines:
        line = line.split('.')
        start_booking = datetime.strptime(line[1] + " " + line[2], "%d/%m/%Y, %H:%M")
        new_booking = Booking(line[0], start_booking, int(line[3]), line[4], line[5])
        self.booking.append(new_booking)



def save_to_file(self, file_name):
    data_file = open(file_name, "w")
    writer = csv.writer(data_file)

    for booking in self.bookings:
        writer.writerow([booking.get_room(),booking.get_start(),booking.get_hours(),booking.get_title(),booking.get_contact()])
