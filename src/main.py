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

    patient = User("Patient", 30, "000099")
    patient.add_to_role(Role.Patient)
    # test_user = User("Test", 24, "000099")
    # test_user.add_to_role(Role.Patient)
    # bob = User("Bob", 24, "00006")
    # bob.add_to_role(Role.Patient)

    # try:
    #     national_database.add_user(bob, admin)
    # except AccessControlException as e:
    #     print(e)

    # national_database.add_test(bob, admin, TestResult.Positive)


    DataMaker.populate_database(100, national_database)

    national_database.print_database()




    while(True):
        print("Choose your role:")
        access_control.print_roles()
        option = input('>')
        role = patient
        if option == '0':
            role == admin
        elif option == '1':
            role == doctor
        elif option == '2':
            role == nurse
        elif option == '3':
            role == researcher
        elif option == '4':
            role == patient
        elif option == 'quit':
            break
        else:
            print('Unknown Command')
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
                        user = national_database.get_user_by_cpr(cpr)
                        national_database.get_vaccination_certificate(user, role)
                    elif ac == '1':             
                        print('Enter cpr for patient:')
                        cpr = input('>')
                        user = national_database.get_user_by_cpr(cpr)
                        national_database.add_vaccination(user, role)
                    elif ac == 'quit':
                        break
            elif action == '1':
                pass
            elif action == '2':
                pass
            elif action == '3':
                booking.booking()
                booking.booking_approvement(admin, national_database)
                print()
            elif action == '4':
                infected = national_database.get_infected_count_last_7_days()
                print()
            elif action == 'quit':
                break



if __name__ == '__main__':
    main()