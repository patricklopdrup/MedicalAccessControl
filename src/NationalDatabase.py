from AccessControl import *
from datetime import date
from User import *
from enum import Enum

class TestResult(Enum):
    Positive = 0
    Negative = 1
    Unknown = 2


class DatabaseObject():
    def __init__(self, user: User, vaccinated: bool = False, tested: bool = False, \
                    test_result: TestResult = TestResult.Unknown,\
                        last_test_date: date = None, vaccination_date: date = None):
        self.name = user.name
        self.age = user.age
        self.cpr_number = user.cpr_number
        self.vaccinated = vaccinated
        self.tested = tested
        self.test_result = test_result
        self.last_test_date = last_test_date
        self.vaccination_date = vaccination_date

    def __str__(self):
        return str(self.name)


class NationalDatabase():
    def __init__(self):
        self.database = [
            DatabaseObject(User("Patrick", 24, "00000"), True, True, TestResult.Negative, \
                            date(2022,1,1), date(2022,3,2)),
            DatabaseObject(User("John", 25, "00001"), False, False, TestResult.Unknown, \
                            None, None),
            DatabaseObject(User("Jane", 26, "00002"), True, True, TestResult.Positive, \
                            date(2022,3,20), date(2022,2,2)),
            DatabaseObject(User("Jack", 27, "00003"), False, False, TestResult.Unknown, \
                            None, None),
            DatabaseObject(User("Jill", 28, "00004"),False, True, TestResult.Negative, \
                            None, date(2022,2,2))
        ]

    def add_user(self, user_to_add: User, responsable: User):
        responsable.check_access_control(Resource.Database, Access.Write)
        self.database.append(DatabaseObject(user_to_add))

    def add_vaccination(self, user: User, responsable: User):
        responsable.check_access_control(Resource.VaccinationCertificate, Access.Write)
        for record in self.database:
            if record.cpr_number == user.cpr_number:
                record.vaccinated = True
                record.vaccination_date = date.today()
                return True
        print("User not found in database")
        return False

    def print_database(self) -> str:
        print("\nNational Database:")
        count = 0
        for record in self.database:
            count += 1
            print(f"{count}: {record} - Vaccine: {record.vaccinated}")
        
    def get_test_result(self, user: User) -> TestResult:
        for record in self.database:
            if record.cpr_number == user.cpr_number:
                return record.test_result
        print("User not found in database")
        return None

    def get_vaccination_certificate(self, user: User) -> str:
        for record in self.database:
            if record.cpr_number == user.cpr_number:
                if record.vaccinated:
                    return f"{record.name} has been vaccinated on {record.vaccination_date}"
                else:
                    return f"{record.name} has not been vaccinated"
        print("User not found in database")
        return None