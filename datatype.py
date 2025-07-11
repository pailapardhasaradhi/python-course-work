#1. Numeric Types
#a. int – Integer
product_quantaty=3
order_id=1240565
print(type(product_quantaty))
print(type(order_id))

#b. float – Floating-point
product_price=74.12
discunt=5.5
rating=4.3
print(type(product_price))
print(type(discunt))
print(type(rating))

#c. complex – Complex Numbers
z = 5 + 2j
print(type(z))

#2. Sequence Types
#a. str – String
custamer_name="Venky"
product_name="grocery"
delevery_adress="hyd kphb colony"
print(type(custamer_name))
print(type(product_name))
print(type(delevery_adress))

#b. list – List
cart_itams=["shoees","shits","sandal","pants"]
top_catagary=["mobile","watchs","beauty"]
print(cart_itams)
print(len(top_catagary))
#c. tuple – Tuple
warehouse_location=(11.255,58.23)
product_dem=(44.23,88.36,69.22)
print(type(warehouse_location))


#3. Set Types
#a. set – Set
avaliable_size={"m","s","l","xl"}
popular_brands={"nike","puma","zara","nike"}
print(popular_brands)
#b. frozenset – Immutable Set
frozen_tags = frozenset(["Sale", "Limited Edition","Trending"])

#4. Mapping Type
#a. dict – Dictionary
product_details={
    "name": "wireless mouse",
    "brand": "logitech",
    "price": 599,
    "rating": 4.5

}
custamer_details={
    "name": "Venky",
    "email": "venky@143",
    "prime_number": True

}
print(product_details["brand"])
print(product_details["name"])
print(product_details["price"])
print(product_details["rating"])
if custamer_details ["prime_number"]:
    print("prime_number")
else:
    print("not a prime_number")


#5. Boolean Type
#a. bool – Boolean

is_logged_in = True
is_payment_successful = False
is_in_stock = True
print(type(is_logged_in ))

#6. None Type
#a. NoneType – Represents a null or missing value
tracking_number = None
delivery_partner = None
print(type(tracking_number))
