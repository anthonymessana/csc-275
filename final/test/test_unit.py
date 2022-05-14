import unittest
from unittest.mock import MagicMock

from final import Address, Item, Customer, Order, Restaurant, OrderHandler

class TestItem(unittest.TestCase):

    def test_set_price_positive(self):
        item = Item("Burger", 5.99)
        print(item.price)
        self.assertEqual(item.price, 5.99)

    def test_set_price_zero(self):
        item = Item("Burger", 1.0)
        self.assertRaisesRegex(ValueError, "Value must be greater than 0", Item, "Burger", -1.0)

class TestCustomer(unittest.TestCase):

    def test_place_order(self):
        mAddress = MagicMock()
        cust = Customer("John", mAddress, "Card", 1000.0)
        mRestaurant = MagicMock(autospec=Restaurant)
        mItem1 = MagicMock(autospec=Item)
        mItem1.name = "Smoothie"
        mItem1.price = 3.00
        RestaurantMenu = [mItem1]
        mRestaurant.menu = RestaurantMenu
        CustomerOrder = [mItem1]
        order = cust.place_order(mRestaurant, CustomerOrder)
        self.assertEqual(len(order.items), 1)
    
    def test_bad_order(self):
        mAddress = MagicMock()
        cust = Customer("John", mAddress, "Card", 1000.0)
        mRestaurant = MagicMock(autospec=Restaurant)
        mItem1 = MagicMock(autospec=Item)
        mItem1.name = "Smoothie"
        mItem1.price = 3.00
        mItem2 = MagicMock(autospec=Item)
        mItem2.name = "Ice Cream"
        mItem2name = 2.00
        RestaurantMenu = [mItem1]
        mRestaurant.menu = RestaurantMenu
        mRestaurant.name = "Wendys"
        CustomerOrder = [mItem2]
        self.assertRaisesRegex(ValueError, "Wendys does not serve [Ice Cream]", cust.place_order, mRestaurant, CustomerOrder)      

class TestOrder(unittest.TestCase):

    def setUp(self):
        item1 = MagicMock(autospec=Item)
        item1.name = "Sandwich"
        item1.price = 5.00
        item2 = MagicMock(autospec=Item)
        item2.name = "Burger"
        item2.price = 5.00
        self.fixture_data = (
            (
                {"discount_levels": [5, 10, 15], "discount_rate": 0.05, "items": [item1, item2]}, 9.00, 
            ),
            (
                {"discount_levels": [15, 5, 10], "discount_rate": 0.05, "items": [item1, item2]}, 9.00,
            ),
            (
                {"discount_levels": [15, 10, 5], "discount_rate": 0.01, "items": [item1, item2]}, 9.8,
            ),
            (
                {"discount_levels": [15, 10, 5], "discount_rate": 0.49, "items": [item1, item2]}, 0.2,
            ),
            (
                {"discount_levels": [15, 12, 11], "discount_rate": 0.01, "items": [item1, item2]}, 10.0,
            ),
        )

    def test_order_pricing(self):
        for context, expected in self.fixture_data:
            with self.subTest(context=context):
                mCustomer = MagicMock()
                mRestaurant = MagicMock(autospec=Restaurant)
                mRestaurant.discount_levels = context["discount_levels"]
                mRestaurant.discount_rate = context["discount_rate"]
                order = Order(mCustomer, mRestaurant, context["items"]) 
                self.assertEqual(order.price, expected)


class TestRestaurant(unittest.TestCase):

    def test_add_menu(self):
        mAddress = MagicMock()
        restaurant = Restaurant("Wendys", mAddress, [], [15, 10, 5], 0.05)
        mItem = MagicMock(autospec=Item)
        mItem.name = "Salad"
        mItem.price = 2.00
        restaurant.add_menu_item(mItem)
        self.assertEqual(len(restaurant.menu), 1)
    def test_remove_menu(self):
        mAddress = MagicMock()
        mItem = MagicMock(autospec=Item)
        mItem.name = "Salad"
        mItem.price = 2.00
        restaurant = Restaurant("Wendys", mAddress, [mItem], [15, 10, 5], 0.05)
        restaurant.remove_menu_item(mItem)
        self.assertEqual(len(restaurant.menu), 0)

class TestOrderHandler(unittest.TestCase):

    def test_order(self):
        mOrder = MagicMock(autospec=True)
        mOrder.price = 10.0
        mCustomer = MagicMock(autospec=True)
        mCustomer.balance = 11.0
        mRestaurant = MagicMock(autospec=True)
        
        handler = OrderHandler(mCustomer, mOrder, mRestaurant)
        self.assertEqual(handler.make_payment(), 1)
    
    def test_insufficient_balance(self):
        mOrder = MagicMock(autospec=True)
        mOrder.price = 12.0
        mCustomer = MagicMock(autospec=True)
        mCustomer.balance = 11.0
        mRestaurant = MagicMock(autospec=True)
        
        handler = OrderHandler(mCustomer, mOrder, mRestaurant)
        self.assertRaisesRegex(ValueError, "Sorry, you do not have the funds to complete this order", handler.make_payment)

