
from array import array
from AccessControl import *
from datetime import date
from User import *
from enum import Enum
import subprocess
import sys


class BookingObject():
    def __init__(self, user: User, appointment: int):
        self.name = user.name
        self.age = user.age
        self.cpr_number = user.cpr_number
        self.appointment = appointment
        
   
class Booking():
    
    def __init__(self):
        self.data = [BookingObject]
        
         
    def booking(self)->str:
        
        print("Book your appointment:")
        booking ={
            1: "test",
            2: "vaccination"
        }
        for key, value in booking.items():
            print(key, ": ", value)
        print()
        
        appointment = input("Choose 1 or 2: ")
        print("Input your personal data: ")
        name = input("Your name: ") 
        age = input("Your age: ") 
        cpr_number = input("Your cpr: ") 
        print()
        
        self.data=[BookingObject(User(name,age,cpr_number),appointment)]
        
        self.print_booking()
        
    def print_booking(self) -> str:
        
        for d in self.data:
            print("New booking!")
            print(f"Type of booking: {d.appointment}")
            print(f"User name: {d.name}" )
            print(f"User age: {d.age}")
            print(f"User CPR: {d.cpr_number}")
            
        print()
   
    
        
   
        
        
    
        
    
        
                     
# result = subprocess.run([sys.executable, "-c"])