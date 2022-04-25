from hashlib import new
from AccessControl import *
from User import *
from NationalDatabase import *
from DataMaker import *


access_control = AccessControl()
national_database = NationalDatabase()



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
        
       
       
        
    def booking_approvement(self, admin: User, db:NationalDatabase) :
         
        for d in self.data:
            if d.appointment=='1':
                print("You recieved a new booking for Covid test!")
                print()
                print(f"User name: {d.name}" )
                print(f"User age: {d.age}")
                print(f"User CPR: {d.cpr_number}")
                print()
                user=User(d.name,d.age,d.cpr_number)
                user.add_to_role(Role.Patient)
                
                approve = input("If the personal data is corect? y/n : ")
                if not db.user_exists(user,admin) and approve == 'y':
                    try: 
                        db.add_user(user, admin)
                        add_new_test_for_user(user, admin, db)  
                        print("New user was registered for the Covid test!")
                        print()
                    except AccessControlException as e:
                        print(e)
                elif db.user_exists(user,admin) and approve == 'y':
                    try: 
                        add_new_test_for_user(user, admin, db)
                        print()
                        print("Old user was registered for the Covid test!")
                        print()
                    except AccessControlException as e:
                        print(e)
            elif d.appointment=='2':
                print("You recieved a new booking for vaccination!")
                print()
                print(f"User name: {d.name}" )
                print(f"User age: {d.age}")
                print(f"User CPR: {d.cpr_number}")
                print()
                user=User(d.name,d.age,d.cpr_number)
                user.add_to_role(Role.Patient)
                approve = input("If the personal data is corect? y/n : ")
                if not db.user_exists(user,admin) and approve == 'y':
                    try: 
                        db.add_user(user, admin)
                        booked_vaccination_date(user, admin, db)  
                        print("New user was registered for the vaccination!")
                        print()
                    except AccessControlException as e:
                        print(e)
                elif db.user_exists(user,admin) and approve == 'y':
                    try: 
                        booked_vaccination_date(user, admin, db)
                        print()
                        print("Old user was registered for the Covid test!")
                        print()
                    except AccessControlException as e:
                        print(e)
                       
        db.print_database()   
            
            
                
        print()
        
  
    
        
   
        
        
    
        
    
        
                     
# result = subprocess.run([sys.executable, "-c"])