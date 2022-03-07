import unittest
from midterm_code import TicketShoppingCart, AirlineTicket

class TestTicketShoppingCart(unittest.TestCase):
    def test_add_valid_year_ticket(self):
        shoppingCart = TicketShoppingCart()
        shoppingCart.add_to_shopping_cart("Newark", "Dallas", 2022, 100)
        self.assertEqual(shoppingCart.tickets[0].from_, "Newark")
        self.assertEqual(shoppingCart.tickets[0].to_, "Dallas")
        self.assertEqual(shoppingCart.tickets[0].year, 2022)
        self.assertEqual(shoppingCart.tickets[0].price, 100)
    def test_invalid_year_ticket(self):
        shoppingCart = TicketShoppingCart()
        self.assertRaisesRegex
        (
            ValueError,
            "Year must be current year or later",
            shoppingCart.add_to_shopping_cart,
            "Newark", "Dallas", 1441, 100
        )
