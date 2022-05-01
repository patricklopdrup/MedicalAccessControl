from cgi import test
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

    infected = national_database.get_infected_count_last_7_days()
    print(infected)


    while(True):
        print("Choose your role:")
        access_control.print_roles()
        option = input('>')
        if option == '0':
            while(True):
                access_control.print_admin_actions()
                admin_option = input('>')
                if admin_option == '0':
                    print('Enter cpr for patient:')
                    cpr = input('>')
                    user = national_database.get_user_by_cpr(cpr)
                    national_database.add_vaccination(user, admin)
                elif admin_option == '1':
                    pass
                elif admin_option == '2':
                    pass
                elif admin_option == 'quit':
                    break
        elif option == '1':
            pass
        elif option == '2':
            pass
        elif option == '3':
            pass
        elif option == '4':
            booking.booking()
            booking.booking_approvement(admin, national_database)
        elif option == 'quit':
            break
        else:
            print('Unknown Command')


if __name__ == '__main__':
    main()
