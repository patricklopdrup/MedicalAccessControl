from NationalDatabase import *
from AccessControl import *
from Booking import *

access_control = AccessControl()
national_database = NationalDatabase()
booking = Booking()


admin = User("Admin", 30, "99999")
admin.add_to_role(Role.Admin)
test_user = User("Test", 24, "00005")
test_user.add_to_role(Role.Patient)
bob = User("Bob", 24, "00006")
bob.add_to_role(Role.Patient)

try:
    national_database.add_user(bob, admin)
except AccessControlException as e:
    print(e)

national_database.add_test(bob, admin, TestResult.Positive)


national_database.print_database()


booking.booking()  
