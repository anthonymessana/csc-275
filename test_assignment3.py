# Work with Matthew Hannum

import unittest
from assignment3 import Order, StudentDiscount, Item

class TestItem(unittest.TestCase):
    def test_price_getter(self):
        item = Item("item", 10, 0)
        self.assertEqual(item.price, 10)
    
    def test_price_setter_with_positive(self):
        item = Item("item", 5, .5)
        item.price = 5.0
        self.assertEqual(item.price, 2.5)
        
    def test_price_setter_with_negative(self):
        item = Item("item",1, 0)
        item.price = -5.0
        self.assertEqual(item.price, 1)
    

class TestStudentDiscount(unittest.TestCase):
    def setUp(self):
        self.fixture_data = (
        (
        # test with empty discount levels list 
        {"discount_levels" : None, "price": 10, "discount_price":.05},
        0
        ),
        (
        # test with max price level
        {"discount_levels" : [25, 15, 5], "price": 25, "discount_price":.05},
        (.05*3)
        ),
        (
        # test with price delta at min boundary
        {"discount_levels" : [25, 15, 5], "price": 25, "discount_price":.0001},
        (.0001*3)
        ),
        (
        # test with price delta at max boundary
        {"discount_levels" : [25, 15, 5], "price": 25, "discount_price":.9999},
        (.9999*3)
        ),
        (
        # test with price at min discount level
        {"discount_levels" : [25, 15, 5], "price": 5, "discount_price":.05},
        (.05)
        ),
        (
        # test with price lower than all discount levels
        {"discount_levels" : [25, 15, 5], "price": 4, "discount_price":.05},
        (0)
        ),
        (
        # test with unsorted discount level list
        {"discount_levels" : [5, 25, 15], "price": 25, "discount_price":.05},
        (.05*3)
        ),
    )
    
    def test_student(self):
        for context, expected in self.fixture_data:
            with self.subTest(context=context):
                discount = StudentDiscount(context["discount_levels"], context["discount_price"])
                price = discount.calculate_discount_price(
                    context["price"]
                )
                self.assertEqual(price, expected)
                
class TestOrder(unittest.TestCase):
    def test_add(self):
        studDiscount = StudentDiscount()
        order = Order(studDiscount)
        item = Item("Thing", 5, .5)
        order.add_item(item)
        self.assertEqual(len(order.items) , 1)
    def test_empty_list(self):
        studDiscount = StudentDiscount()
        order = Order(studDiscount)
        self.assertEqual(len(order.items) , 0)
     
    def test_empty_calculate_total(self):
        studDiscount = StudentDiscount()
        order = Order(studDiscount)
        price = order.calculate_total_price()
        self.assertEqual(price, 0)
    
    def test_calculate_total_no_discount(self):
        studDiscount = StudentDiscount()
        order = Order(studDiscount)
        item = Item("pencil", 1.00, 0)
        item2 = Item("notebook", 5.00, 0)
        item3 = Item("backpack", 10.00, 0)
        order.add_item(item)
        order.add_item(item2)
        order.add_item(item3)
        price = order.calculate_total_price()
        self.assertEqual(price, 16)
    
    def test_calculate_total_just_student_discount(self):
        studDiscount = StudentDiscount([1, 5, 9])
        order = Order(studDiscount)
        item = Item("pencil", 1.00, 0)
        item2 = Item("notebook", 5.00, 0)
        item3 = Item("backpack", 10.00, 0)
        order.add_item(item)
        order.add_item(item2)
        order.add_item(item3)
        price = order.calculate_total_price()
        self.assertEqual(price, 13.95)
        
    def test_calculate_total_just_item_discount(self):
        studDiscount = StudentDiscount()
        order = Order(studDiscount)
        item = Item("pencil", 1.00, .5)
        item2 = Item("notebook", 5.00, .5)
        item3 = Item("backpack", 10.00, .5)
        order.add_item(item)
        order.add_item(item2)
        order.add_item(item3)
        price = order.calculate_total_price()
        self.assertEqual(price, 8)
        
    def test_calculate_total_item_and_student_discount(self):
        studDiscount = StudentDiscount([1, 5, 9])
        order = Order(studDiscount)
        item = Item("pencil", 1.00, .5)
        item2 = Item("notebook", 5.00, .5)
        item3 = Item("backpack", 10.00, .5)
        order.add_item(item)
        order.add_item(item2)
        order.add_item(item3)
        price = order.calculate_total_price()
        self.assertEqual(price, 7.375)