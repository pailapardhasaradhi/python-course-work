age =int(input("enter the age:"))
if age <4:
    print("child")
elif age >=10:
    print("boy")
elif age >=18:
    print("men")
elif age >= 40:
    print("uncle")
else:
    print("baccha")

 ## example 2
num= int(input('enter the number:'))
if num > 0:
 print("positive")
elif num < 0:
    print("negative")
else:
    print("null")
 
 #example -3
a= int(input("enter the number:"))
b= int(input("enter the number:"))
if a>b:
   print(f"{a}is greater than {b}")
elif a==b:
   print(f"{a} is equal to {b}")
else:
   print(f"{b} is greater than {a}")

#example-4
items =['coffee','ice cream','samosa','idly']
stocks=[20,50,40,0]
distance=[13,4,9,12]
rating=[3.2,4,4.3,1]
cost=[150,60,20,40]
veg=[True,True,False,True]
time=[40,30,25,15]
data=input("enter the item: ")
if data in items:
 ind=items.index(data)
if distance[ind]<5 and rating[ind]>4 and cost[ind]<500 and veg[ind]:
   print("distance,stock,ratings,cost,veg ,time is applied")
elif  distance[ind]<5 and rating[ind]>4 and cost[ind]<500:
   print("distance,rating,cost applied")
elif  distance[ind]<5 and rating[ind]>4:
   print("distance,rating applied")
else:
   print("all the filters are not applied")

##
l= ['pardhu','mounish']
l.insert('goutham')
print(l)

####
gallery={'1.beach.png','2.mountain.jpg','3.party1.jpg','4.selfie.png','5.birthday.png','6.sunset','7.trip1.jpg'}
i=int(input('enter the number:'))
if i in range(gallery):
   print(i)

##
n= input()
n=n.replace('e','*')
print(n)

#
def wish(name):
   batch = 30
   print(f"welcome to hyderabad {name}")
   name = input("Enter the name:")
   wish(name)