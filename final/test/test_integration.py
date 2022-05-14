import unittest

from final import Address, Item, Customer, Order, Restaurant, OrderHandler

class TestCustomer(unittest.TestCase):

    def test_place_order(self):
        custAddress = Address("5 Hillside Ave", "Airmont", "10952", "NY", "US")
        restAddress = Address("3 Hillside Ave", "Airmont", "10952", "NY", "US")
        Item1 = Item("Smoothie", 3.00)
        RestaurantMenu = [Item1]
        CustomerOrder = [Item1]
        cust = Customer("John", Address, "Card", 1000.0)
        restaurant = Restaurant("Wendys", restAddress, RestaurantMenu, [15, 10, 5], 0.05)
        order = cust.place_order(restaurant, CustomerOrder)
        self.assertEqual(order.restaurant.name, "Wendys")
        self.assertEqual(order.items[0].name, "Smoothie")
        self.assertEqual(order.items[0].price, 3.00)

class TestRestaurant(unittest.TestCase):

    def test_add_menu(self):
        restAddress = Address("3 Hillside Ave", "Airmont", "10952", "NY", "US")
        restaurant = Restaurant("Wendys", restAddress, [], [15, 10, 5], 0.05)
        item = Item("Salad", 2.00)
        restaurant.add_menu_item(item)
        self.assertEqual(restaurant.menu[0].name, "Salad")
        self.assertEqual(restaurant.menu[0].price, 2.00)
    
    def test_remove_menu(self):
        restAddress = Address("3 Hillside Ave", "Airmont", "10952", "NY", "US")
        item = Item("Salad", 2.00)
        restaurant = Restaurant("Wendys", restAddress, [item], [15, 10, 5], 0.05)
        restaurant.remove_menu_item(item)
        self.assertNotIn(item, restaurant.menu, "Item is still on menu")