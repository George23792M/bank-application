class Address:
    def __init__(self, streetName, city, state, zipCode):
        self.streetName = streetName
        self.city = city
        self.state = state
        self.zipCode = zipCode

    def str(self):
        return self.streetName + " " + self.city + " " + self.state + " " + self.zipCode
