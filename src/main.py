from cgi import test
from cmath import e
from pydoc import doc
from NationalDatabase import *
from AccessControl import *
from Booking import *
import DataMaker

def main():
    access_control = AccessControl()
    national_database = NationalDatabase()
    booking = Booking()

    admin = User("Admin", 30, "99999")
    admin.add_to_role(Role.Admin)

    doctor = User("Doctor", 30, "99998")
    doctor.add_to_role(Role.Doctor)

    nurse = User("Nurse", 30, "99997")
    nurse.add_to_role(Role.Nurse)

    researcher = User("Researcher", 30, "99996")
    researcher.add_to_role(Role.Researcher)

    patient = User("Patient", 30, "99995")
    patient.add_to_role(Role.Patient)

    DataMaker.populate_database(100, national_database)

    national_database.print_database()


    while(True):
        print("Choose your role:")
        access_control.print_roles()
        option = input('>')
        role = patient
        if option == '0':
            role = admin
        elif option == '1':
            role = doctor
        elif option == '2':
            role = nurse
        elif option == '3':
            role == researcher
        elif option == '4':
            role = patient
        elif option == 'quit':
            break
        else:
            print('Unknown commant')
        while(True):
            access_control.print_all_actions()
            action = input('>')
            if action == '0':
                while(True):
                    access_control.print_io()
                    ac = input('>')
                    if ac == '0':
                        print('Enter cpr for patient:')
                        cpr = input('>')
                        user = national_database.get_user_by_cpr(cpr, role)
                        national_database.get_vaccination_certificate(user, role)
                    elif ac == '1':             
                        print('Enter cpr for patient:')
                        cpr = input('>')
                        user = national_database.get_user_by_cpr(cpr, role)
                        national_database.add_vaccination(user, role)
                    elif ac == 'quit':
                        break
                    else:
                        print('Unknown Command')
            elif action == '1':
                while(True):
                    access_control.print_io()
                    ac = input('>')
                    if ac == '0':
                        print('Enter cpr for patient:')
                        cpr = input('>')
                        user = national_database.get_user_by_cpr(cpr, role)
                        if user is not None:
                            result = national_database.get_test_result(user, role)
                            if result is not None:
                                print(result)
                    elif ac == '1':             
                        print('Enter cpr for patient:')
                        cpr = input('>')
                        user = national_database.get_user_by_cpr(cpr, role)
                        print('Enter test result:')
                        if user is not None:
                            result = input('>').lower()
                            if result == 'negative':
                                res = TestResult.Negative
                                national_database.add_test(user, role, res)
                            elif result == 'positive':
                                res = TestResult.Positive
                                national_database.add_test(user, role, res)
                            else:
                                print('Result must be eiter Positive or Negative')
                    elif ac == 'quit':
                        break
                    else:
                        print('Unknown Command')
            elif action == '2':
                while(True):
                    access_control.print_io()
                    ac = input('>')
                    if ac == '0':
                        print('Enter cpr for patient:')
                        cpr = input('>')
                        record = national_database.get_db_entry_by_cpr(cpr, role)
                        if record is not None:
                            print(record)
                    elif ac == '1':
                        print('Enter patient name:')
                        name = input('>')          
                        print('Enter patient age:')    
                        age = input('>')     
                        print('Enter cpr for patient:')
                        cpr = input('>')
                        user = User(name=name, age=int(age), cpr_number=str(cpr))
                        national_database.add_user(user, role)
                    elif ac == 'quit':
                        break
                    else:
                        print('Unknown Command')
            elif action == '3':
                booking.booking()
                booking.booking_approvement(admin, national_database)
            elif action == '4':
                infected = national_database.get_infected_count_last_7_days()
            elif action == 'quit':
                break
            else:
                print('Unknown Command')



if __name__ == '__main__':
    main()