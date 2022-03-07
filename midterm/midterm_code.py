from tcnj_flight_api import WorldFamousTCNJFlightAPI


class DiscountService:
    """
    This service calculates the discount of an airline ticket
    based on age of the passenger.
    """
    CHILD_DISCOUNT = .2
    LOWEST_AGE = 2  # lowest age for discount
    MIDDLE_AGE = 5  # middle age for discount
    OLDEST_AGE = 10  # oldest age for discount

    @staticmethod
    def calculate_discount(passenger_age):
        """
        Calculates the discount for each passenger by age.
        *Note: The numbers 1.0, 2, and 0 have comments and
        for this exam do not need to be made into constants.
        """
        if passenger_age < DiscountService.LOWEST_AGE:
            return 1.0  # discount 100% of ticket price
        if passenger_age <= DiscountService.MIDDLE_AGE:
            return 2 * DiscountService.CHILD_DISCOUNT  # discount 2 times the CHILD_DISCOUNT
        if passenger_age <= DiscountService.OLDEST_AGE:
            return DiscountService.CHILD_DISCOUNT
        return 0  # return 0 discount


class AirlineTicket:
    """
    This is a class for a ticket.
    *Note: `year` is used instead of `date` for simplicity
    of the exam.
    """

    CURRENT_YEAR = 2022

    def __init__(self, from_, to_, year, price):
        self.from_ = from_
        self.to_ = to_
        self.year = year
        self.price = price

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if value < AirlineTicket.CURRENT_YEAR:
            raise ValueError("Year must be current year or later")
        self._year = value

# Abstracted out email_ticket_to_purchaser in seperate class for breaking Single Responsibility Principle
class EmailTicketService:
    def __init__(self, ticket):
        self.ticket = ticket
    @staticmethod
    def email_ticket_to_purchaser():
        """
        *Note: Assume this method sends an email to the purchaser of the ticket
        and returns the below as confirmation.
        """
        return "Confirmed. Ticket has be emailed to purchaser"

class PriceService:
    def __init__(self, flight_api):
        self.flight_api = flight_api

    def get_ticket_price(self, from_, to_, year):
        """
        Gets price of ticket from api.
        """
        return self.flight_api.get_ticket_price(from_, to_, year)


class TCNJFlightAPI:
    """
    This is the class for a flight API that returns the ticket price.
    """
    def __init__(self, username, password):
        self.api = WorldFamousTCNJFlightAPI(username, password)

    def get_ticket_price(self, from_, to_, year):
        return self.api.cost(from_, to_, year)


class TicketShoppingCart:
    """
    Class for adding new tickets to shopping cart.
    *Note: This class should be integration tested in a separate
    file and does NOT need to be unit tested.
    """
    def __init__(self):
        self.tickets = []

    def add_to_shopping_cart(self, from_, to_, year, price):
        self.tickets.append(
                AirlineTicket(from_, to_, year, price)
            )