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

## 2. INHERITENCE
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



