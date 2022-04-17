from AccessControl import *

access_control = AccessControl()

class User():
    def __init__(self, name: str, age: int, cpr_number: str):
        self.name = name
        self.age = age
        self.cpr_number = cpr_number
        self.role = Role.Patient
        
    def add_to_role(self, role: Role):
        self.role = role

    def can_access(self, resource: Resource, access: Access) -> bool:
        if self.role in access_control.access_list:
            if resource in access_control.access_list[self.role]:
                access_for_role = access_control.access_list[self.role][resource]
                # Read is implicit when a user can write
                if access_for_role == Access.Write and access == Access.Read:
                    return True
                return access_for_role == access
        return False

    def check_access_control(self, resource: Resource, access: Access) -> bool:
        if not self.can_access(resource, access):
            raise AccessControlException(self, resource, access)
        return True