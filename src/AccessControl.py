from enum import Enum



class Role(Enum):
    Admin = 0
    Doctor = 1
    Nurse = 2
    Researcher = 3
    Patient = 4


class Resource(Enum):
    VaccinationCertificate = 0
    PandemicTest = 1
    Database = 2


class Access(Enum):
    Read = 0
    Write = 1


class AccessControl():
    def __init__(self):
        self.access_list = {
            Role.Admin: {
                Resource.VaccinationCertificate: Access.Write,
                Resource.PandemicTest: Access.Write,
                Resource.Database: Access.Write
            },
            Role.Doctor: {
                Resource.VaccinationCertificate: Access.Write,
                Resource.PandemicTest: Access.Write
            },
            Role.Nurse: {
                Resource.VaccinationCertificate: Access.Read,
                Resource.PandemicTest: Access.Read
            },
            Role.Researcher: {
                Resource.VaccinationCertificate: Access.Read,
                Resource.PandemicTest: Access.Read
            },
            Role.Patient: {
                Resource.VaccinationCertificate: Access.Read
            }
        }
    
    def print_io(self):
        print('(0) Read')
        print('(1) Write')
    
    def print_roles(self):
        for role in self.access_list:
            print(f'({role.value}) {role.name}')

    def print_all_actions(self):
        for res, ac in self.access_list[Role.Admin].items():
            print(f'({res.value}) Read/{ac.name} {res.name}')
        print(f'({res.value + 1}) Booking')
        print(f'({res.value + 2}) Add booking')
        print(f'({res.value + 3}) Statistics')


class AccessControlException(Exception):
    def __init__(self, user, resource: Resource, access: Access):
        self.message = f"{user.name} does not have '{access.name}' access to '{resource.name}'."
        super().__init__(self.message)

