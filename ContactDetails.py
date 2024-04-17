from Address import Address


class ContactDetails:
    # Constructor
    def __init__(self, name, phoneNumber, street, city, state, ZipCode):
        self.name = name
        self.phoneNumber = phoneNumber
        self.Address = Address(street, city, state, ZipCode)

    # To String method
    def __str__(self):
        return self.name + "" + self.phoneNumber + "" + self.Address
