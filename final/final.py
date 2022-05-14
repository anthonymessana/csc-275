class Address:
    def __init__(self, street, city, zip, state, country):
        self.street = street
        self.city = city
        self.zip = zip
        self.state = state
        self.country = country

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Value must be greater than 0")
        self._price = value

class Customer:
    def __init__(self, name, address, PaymentMethod, balance):
        self.name = name
        self.address = address
        self.payment = PaymentMethod
        self.balance = balance
    
    def place_order(self, restaurant, items):
        for item in items:
            bad_items = []
            if item not in restaurant.menu:
                bad_items.append(item)
        if bad_items:
            for bad_item in bad_items:
                raise ValueError(restaurant.name + " does not serve " + bad_item.name)
        else:
            order = Order(self, restaurant, items)
            return order


class Order:
    def __init__(self, customer, restaurant, items):
        self.customer = customer
        self.restaurant = restaurant
        self.items = items
        self.price = (items, restaurant)
    
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, menuTuple):
        total_price = 0
        items, restaurant = menuTuple
        for item in items:
            total_price += item.price
        
        total_discount = 0
        for level in sorted(restaurant.discount_levels, reverse=True):
            if total_price >= level:
                total_discount += restaurant.discount_rate
        self._price = round(total_price * (1 - total_discount), 2)

class Restaurant:
    def __init__(self, name, address, menu, discount_levels, discount_rate = 0.05):
        self.name = name
        self.address = address
        self.menu = menu
        self.discount_rate = discount_rate
        self.discount_levels = discount_levels
    
    def add_menu_item(self, item: Item):
        self.menu.append(item)
    
    def remove_menu_item(self, item: Item):
        self.menu.remove(item)

class OrderHandler:
    def __init__(self, customer, order, restaurant):
        self.customer = customer
        self.order = order
        self.restaurant = restaurant

    def make_payment(self):
        if (self.customer.balance - self.order.price < 0):
            raise ValueError("Sorry, you do not have the funds to complete this order")
        else:   
            self.customer.balance -= self.order.price
            return self.customer.balance


