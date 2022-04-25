from NationalDatabase import *
from User import User
import random


NAMES = [
            "Patrick",
            "John",
            "Jane",
            "Jack",
            "Jill",
            "Bob",
            "Alice",
            "Charlie",
            "Daniel",
            "Evelyn",
            "Fred",
            "Greta",
            "Holly",
            "Ida",
            "Jenny",
            "Karen",
            "Linda",
            "Mary",
            "Nancy",
            "Olivia",
            "Peter",
            "Quinn",
            "Robert",
            "Samantha"
        ]


def populate_database(population_size:int, db:NationalDatabase):
    admin = User("Admin", 30, "99999")
    admin.add_to_role(Role.Admin)
    for i in range(population_size):
        user = create_user(i)
        user.add_to_role(Role.Patient)
        try:
            db.add_user(user, admin)
        except:
            pass
        add_test_for_user(user, admin, db)
        
        
def create_user(index):
    name = NAMES[index % len(NAMES)]
    cpr = str(index).zfill(6)
    age = random.randint(18, 80)
    return User(name, age, cpr)


def add_test_for_user(user, admin, db):
    test_result = get_random_test_result()
    test_date = get_random_test_date()
    db.add_test(user, admin, test_result, test_date)
    
def add_new_test_for_user(user, admin, db):
    test_date = get_random_new_test_date()
    db.new_test_user(user, admin, test_date)

def get_random_test_result():
    if random.randint(0, 10) <= 4:
        return TestResult.Positive
    else:
        return TestResult.Negative

def get_random_test_date():
    day_offset = random.randint(0, 14)
    return date.today() - timedelta(days=day_offset)

def get_random_new_test_date():
    day_offset = random.randint(0, 14)
    return date.today() + timedelta(days=day_offset)

if __name__ == "__main__":
    populate_database(6)