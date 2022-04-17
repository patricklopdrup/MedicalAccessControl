from NationalDatabase import *
from AccessControl import *

access_control = AccessControl()
national_database = NationalDatabase()




admin = User("Admin", 30, "99999")
admin.add_to_role(Role.Admin)
test_user = User("Test", 24, "00005")
test_user.add_to_role(Role.Patient)
bob = User("Bob", 24, "00006")
bob.add_to_role(Role.Patient)





national_database.print_database()
try:
    national_database.add_user(bob, test_user)
except AccessControlException as e:
    print(e)

#national_database.add_vaccination(bob, test_user)
national_database.print_database()

#print(can_access(patrick, Resource.PandemicTest, Access.Read))