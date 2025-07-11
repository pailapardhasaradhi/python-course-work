## for with else
l=['smartphones','laptop','airpods','shoes']
for i in l:
    if i=='laptop':
        break
    print(i.center(20,'-'))
else:
     print('End of the item')

##while with else
bullets=10
while bullets>0:
    if bullets==5:
        print("dead")
        break
    print(f"{bullets} are left-you can shoot()")
    bullets-=1
else:
        print("game over")


#prime numbers(2,3,5,7,11,13,17,19,23,29)
fact=0
n= int(input("enter the number:"))
for i in range(2,(n//2)+1):
     if n%i==0:
          fact+=1
     if fact==0:
      print(f"{n} is prime number\nfactors count(fact)")
     else:
      print(f"{n} is not prime number\nfactors count(fact)")
