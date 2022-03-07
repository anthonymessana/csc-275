import unittest
from unittest.mock import MagicMock
from midterm_code import DiscountService, AirlineTicket, EmailTicketService, PriceService, TCNJFlightAPI

class TestDiscountService(unittest.TestCase):
    def setUp(self):
        self.fixture_data = (
            (1, 1.0), # Test lowest age
            (5, .4),  # Test middle age
            (10, .2),  # Test oldest age
            (11, 0) ,  # Test greater than oldest age
        )

    def test_calculuate_discount(self):
        for context, expected in self.fixture_data:
            with self.subTest(context=context):
                discount = DiscountService.calculate_discount(context)
                self.assertEqual(discount, expected)

class TestAirlineTicket(unittest.TestCase):
    def test_setter_current_year(self):
        ticket = AirlineTicket("Newark", "Dallas", 2022, 100)
        self.assertEqual(ticket.year, 2022)
    def test_setter_less_than_current_year(self):
        self.assertRaisesRegex(
            ValueError, 
            "Year must be current year or later", 
            AirlineTicket, "Newark", "Dallas", 1492, 100
            )

class TestEmailTicketService(unittest.TestCase):
    def test_send_email_to_purchaser(self):
        mock_ticket = MagicMock(autospec=AirlineTicket)
        emailService = EmailTicketService(mock_ticket)
        result = emailService.email_ticket_to_purchaser()
        self.assertTrue(result, "Confirmed. Ticket has be emailed to purchaser")

class TestPriceService(unittest.TestCase):
    def test_get_ticket_price(self):
        mock_flight_api = MagicMock(autospec=TCNJFlightAPI)
        PriceServiceInstance = PriceService(mock_flight_api)
        PriceServiceInstance.get_ticket_price("Newark", "Dallas", 2022)
        mock_flight_api.get_ticket_price.assert_called_with("Newark", "Dallas", 2022)