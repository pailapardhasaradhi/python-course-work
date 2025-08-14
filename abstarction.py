'''from abc import ABC, abstractmethod
class upload(ABC):
    @abstarctmethod
    def compress(self):
        pass
class Image(upload):
    def compress(self):
        print("Image is compressed to 2MB")
class reel(upload):
    def compress(self):
        print("reel is compressed to 3MB")
r = reel()
i = Image()

r.compress
i.compress'''

###
from abc import ABC, abstractmethod

class Order(ABC):
    @abstractmethod
    def process_order(self):
        pass

class FoodOrder(Order):
    def process_order(self):
        print("Processing Food Order: Check chef availability, estimate time.")

class GroceryOrder(Order):
    def process_order(self):
        print("Processing Grocery Order: Check inventory, bag & dispatch.")

class MedicineOrder(Order):
    def process_order(self):
        print("Processing Medicine Order: Validate prescription, assign secure delivery.")

class CloudKitchenOrder(Order):
    def process_order(self):
        print("Processing Cloud Kitchen Order: Confirm partner, coordinate menu & delivery.")

class PetSuppliesOrder(Order):
    def process_order(self):
        print("Processing Pet Supplies Order: Check product categories, ensure safe packaging.")

class MeatOrder(Order):
    def process_order(self):
        print("Processing Meat/Seafood Order: Confirm freshness, assign chilled transport.")

class CakeOrder(Order):
    def process_order(self):
        print("Processing Party Cake Order: Bulk baking, team coordination, special decorations.")

class JuiceOrder(Order):
    def process_order(self):
        print("Processing Fresh Juice Order: Immediate preparation, cold packaging.")

def handle_order(order: Order):
    order.process_order()

# List of orders
Orders = [
    FoodOrder(),
    GroceryOrder(),
    MedicineOrder(),
    CloudKitchenOrder(),
    PetSuppliesOrder(),
    MeatOrder(),
    CakeOrder(),
    JuiceOrder()
]

# Processing each order
for order in Orders:
    handle_order(order)


###
from abc import ABC, abstractmethod
class payment(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass
class creditcardPayment(payment):
    def make_payment(self, amount):
        print(f"Paid ${amount} using credit card.")

class Paypalpaypement(payment):
    def make_payment(self, amount):
        print(f"paid ${amount} via paypal.")

def process_payment(payment, amount):
    payment.make_payment(amount)

process_payment(creditcardPayment(), 100)
process_payment(Paypalpaypement(), 200)


