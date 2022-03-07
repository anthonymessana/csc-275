import random


class WorldFamousTCNJFlightAPI:
    """
    This is a class that acts like an API
    that returns the price of tickets.
    THIS CLASS DOES NOT NEED TO BE UNIT TESTED
    DIRECTLY i.e. there does not need to be a
    'test_tcnj_flight_api.py'.
    """
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def authenticated(self):
        return self._authenticated

    @authenticated.setter
    def authenticated(self):
        if not (self.username and self.password):
            raise TypeError("username and password required.")
        self._authenticated = True

    def cost(self, from_, to_, year):
        if not self.authenticated:
            raise Exception("Not authenticated.")
        return round(random.uniform(50, 500))