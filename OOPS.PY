'''#### OOPS CONCEPT --->> "OOP in Python is Object-Oriented Programming, a way of structuring code around classes and objects instead of just functions. It uses concepts like encapsulation, inheritance, polymorphism, and abstraction to make code reusable, modular, and easier to maintain
1. Attributes (Data): Properties or characteristics of the object.
2. Methods (Behavior): Functions or actions that the object can perform'''

'''# Step 1: Define a class
class Product:
# Attributes (data)
name = "Laptop"
price = 50000
quantity = 10
# Methods (functions)
def display_info(self):
print(f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}")'''

### 
class Login:
    def password(self,password):
        self.password = password
    def updatepassword(self,new_password):
        self.newpassword = new_password
    def display(self):
        print(self.password)

dinesh = Login()
pardhu = Login()

dinesh.password("pardhu09")
dinesh.display()

pardhu.password("pardhu0988888888888")
pardhu.display()

### ENCAPSULATION
class Details:
    def __init__(self,name,mail,password):
        self.name = name
        self._mail = mail
        self._password = password
    def getpassword(self):
        return self.__password
    def setpassword(self,new_password):
        self.__password = new_password
pardhu = Details("pardhu","pardhu@gmail.com","Pardhu@088")
print(pardhu.name)
print(pardhu._mail)
print(pardhu.getpassword())
pardhu.setpassword("pardhu0898765")
print(pardhu.getpassword())



######
class Bank:
    def __init__(self):
        self.name = "xyz"
        self._balance = 0

    @property
    def noresbalance(self):
        return self._balance

    @noresbalance.setter
    def noresbalance(self, amount):
        self._balance += amount

Bank = Bank()
print(Bank.noresbalance)
Bank.noresbalance = 3000
print(Bank.noresbalance)

## 2. INHERITENCE -----> 5-types of inheritence(single,hierarical,multiple,hybrid,multy)
##inheritance
class Status:
    def __init__(self,caption,image=None,vedio=None):
        self.caption = caption
        self.image = image
        self.vedio = vedio
        self.vediolength = 30
    def see_status(self):
        if self.vedio:
            print(f"---{self.vedio}---{self.caption}")
        else:
            print(f"---{self.image}---{self.caption}")

class statusv1(Status):
    def likes(self):
        print("Like")
    def addmusic(self,music):
        print(f"{music} Added")

pardhu =Status("hi friends","pardhu.png")
print(pardhu.image)
print(pardhu.vedio)

paila = statusv1("hi friends","pardhu.png")
paila.likes()
paila.addmusic("fire storm")

####single inheritance
class Status:
    def uploadImage(self,image):
        self.image = image
        print(f"{self.image} is uploaded to your status")
class StatusV1(Status):
    def addCaption(self,caption):
        self.caption = caption
        print(f"{self.caption} is uploaded to your status")


pardhu = Status()
pardhu.uploadImage("OG.png")

paila = StatusV1()
paila.uploadImage("ORIGINAL GANGSTER")
paila.addCaption("mass")



##hierarchical inheritance ----> SINGLE PARENT MANY CHILD
class Status:
    def uploadImage(self,image):
        self.image = image
        print(f"{self.image} is uploaded to your status")
class StatusV1(Status):
    def addCaption(self,caption):
        self.caption = caption
        print(f"{self.caption} is uploaded to your status")
class Statusv2(Status):
    def like(self):
        print(f" your status got likes")

pardhu = Status()
pardhu.uploadImage("OG.png")

paila = StatusV1()
paila.uploadImage("ORIGINAL GANGSTER")
paila.addCaption("mass")

saradhi = Statusv2()
saradhi.like()

## MULTIPLE ---->MANY PARENTS SINGLE CHILD
class Status:
    def uploadImage(self,image):
        self.image = image
        print(f"{self.image} is uploaded to your status")
class StatusV1(Status):
    def addCaption(self,caption):
        self.caption = caption
        print(f"{self.caption} is uploaded to your status")
class StatusV2(Status):
    def like(self):
        print(f" your status got likes")
class StatusV3(StatusV1,StatusV2):
    def AddMusic(self,music):
        self.music= music
        print(f"{self.music} is uploaded to your status")


pardhu = Status()
pardhu.uploadImage("OG.png")

paila = StatusV1()
paila.uploadImage("ORIGINAL GANGSTER")
paila.addCaption("mass")

saradhi = StatusV2()
saradhi.like()

pk = StatusV3()
pk.uploadImage("OG.png")
pk.addCaption("mass")
pk.like()
pk.AddMusic("FIRESTORM IS COMING.MP3")

##
class Instagram:
    def __init__(self, username):
        self.username = username
        self.post = []
        print(f"{self.username.center(40, '-')}")

class InstagramV1(Instagram):
    def __init__(self, username, bio):
        super().__init__(username)
        self.bio = bio
        print(f'bio uploaded')

dinesh = Instagram('dinesh123')
sanjay = InstagramV1("sanjay", "Coder")

####
class Instagram:
    def __init__(self, username):
        self.username = username
        print(f"{self.username} user is created! parent-1")

class InstaV1:
    def __init__(self, username):
        self.username = username
        print(f"{self.username} user is created! parent-2")

class InstaV2(Instagram, InstaV1):
    def __init__(self, username):
        Instagram.__init__(self, username)
        InstaV1.__init__(self, username)
        print("Creating users from version 3")

i = InstaV2("username--Xyz")

##polymorphism ---> SAME METHOD DIFFERENT ACTION --> EX-- YOUTUBE PLAY OPTION SOME PERSON GET ADDS ANOTHER ONE DIDNT GET ADDS
class normalUser:
    def playvideo(self, name):
        print(f"\n{name} is playing video with :"n1.Normal Quality"\n2.Ads run"
              f"\n3.No background play"
              f"\n4.Limited videos download"
              f"\n5.Music with ads")
    
    def likes(self):
        pass
    
    def comments(self):
        pass
    
    def share(self):
        pass
    
    def title(self):
        pass
    
    def description(self):
        pass
    
    def subscribe(self):
        pass


class premiumUser(normalUser):
    def playvideo(self, name):
        print(f"\n{name} is playing video with :"
              f"\n1.High Quality"
              f"\n2.Ads Free"
              f"\n3.Background play"
              f"\n4.Download anything"
              f"\n5.Exclusive Music")


dinesh = normalUser()
sanjay = premiumUser()

dinesh.playvideo("Dinesh")
sanjay.playvideo("Sanjay")


### OVERLOAD OPERATORS
class number:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return number(self.n + other.n)

    def __sub__(self, other):
        return number(self.n - other.n)

    def __mul__(self, other):
        return number(self.n * other.n)

    def __str__(self):
        return f"{self.n}"
    
number1 = number(10)
number2 = number(20)


print(number1 + number2)    # 30
print(number1 - number2)    # -10
print(number1 * number2)    # 200
print(number1 / number2)    # 0.5

print(number1 == number2)   # False
print(number1 < number2)    # True
print(number1 > number2)    # False

### ABSTARCTION
from abc import ABC, abstractmethod
class Upload(ABC):
    @abstractmethod
    def compress(self):
        self
    print("image is compressed to 2MB")
class Image(Upload):
    def compress(self):
        print("Image is compressed to 2MB")
class reel(Upload):
    def compress(self):
        print("Reel is compressed to 3MB")

r = reel()
i = Image()
r.compress()
i.compress()

#### FOOD ORDER EXAMPLE
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

def handle_order(order):
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


######## BANK EXAMPLE
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def make_payment(self, amount):
        print(f"Paid ${amount} using Credit Card.")

class PayPalPayment(Payment):
    def make_payment(self, amount):
        print(f"Paid ${amount} via PayPal.")

def process_payment(payment: Payment, amount):
    payment.make_payment(amount)

process_payment(CreditCardPayment(), 100)
process_payment(PayPalPayment(), 200)



