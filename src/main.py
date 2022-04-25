from cgi import test
from NationalDatabase import *
from AccessControl import *
from Booking import *
import DataMaker

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

booking.booking()
booking.booking_approvement(admin, national_database)



