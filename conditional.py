# conditional statements

#if condition
data={'prasanth@gmail.com': '12@',
      'dinesh@gmail.com':'789!',
      'sanjay@gmail.com' :'456#',
      }
      
email,pwd=input('enter the email and pwd:').split()
      
if  data.get(email)==pwd:
    print('login succesful')
else:
    print('invalid login')

#2.example
items =['coffee','ice cream','samosa','idly']
stocks=[20,50,40,0]
data =input("enter the item :")
if data in items:
    ind=items.index(data)
    if stocks[ind]>0:
        print('available')
    else:
        print('out of stock')

  #3.filter example
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



##### example
num = int(input("enter the number:"))
if num%2==0:
  print("divisible by 2")
else:
  print("not divisible")

#division
num=int(input("enter the number:"))
if num%2==0 and num%3==0:
   print("Divisible by 2 & 3")
elif num%2==0:
   print("divisible by 2")
elif num%3==0:
   print("divisible by 3")
else:
   print("it doesnt divisible by 2&3") 

# checking whether leap year are not
n=int(input().strip())
if n%2!=0:
    print("Weird")
elif n%2==0 and 2<=n<=6:
    print("Not Wierd")
elif n%2==0 and 6<=n<=20:
    print("Wierd")
elif n%2==0 and n>20:
    print("Not Weird")
