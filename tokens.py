#sample program
l=20
w=10
area=l*w
if area>30:
    print("large area")
else:
    print("small area")








import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))

#Basic Variable Assignment
#1
product_name="hp laptop"
price=45000
in_stock=True
print(product_name,price,in_stock)
#2
product_name="mazza"
price=50
in_stock=True
capacity="1liter"
print(product_name,price,in_stock,capacity)
#3
my_name="venky"
my_age=24
study="Btech Cse"
print(my_name,my_age,study)

#Multiple Assignment
#1
a,b,c =10,20,30
print(a,b,c)
#2
x=y=z=100
print(x,y,z)
#3
q=w=r=200
print(q,w,r)
#Reassignment
#1
x=5
x=10
print(x)
#2
x=10
x=20
x=30
print(x)
#Swapping Variables
#1
a,b=10,20
a,b=b,a
print(a,b)
#2
#Deleting Variables
x=100
del x
print(x)
