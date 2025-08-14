#control statements
#to print numbers from 2 to 11
for i in range(2,12):
       print(f'{i}')
#### ex= 3
# to print numbers 2 to 11 which are added to 2
for i in range(2,12,2):
       print(f'{i}')
# to print even numbers using for loop
for i in range(0,21):
 if i%2==0:
  print(f"{i}")

##to print odd number using ood number
for i in range(0,20):
    if i%2!=0:
        print(f"{i}")

## to 2 tables using for loop
for i in range(0,20):
 print(f"2*{i}={2*i}")

# to print 3 table using for loop
for i in range(0,20):
    print(f"3*{i}={3*i}") 

##right angle triangle
n = 6
for i in range(1,6):
    print("*" * i)

##2
n = 7
for i in range (7):
    print(" " * (n-i)+"*" * i)

#pyramid
n = 8
for i in range(8,0,-1):
    print(" " * (n-i)+"*" * (2*i -1))

##fibinocci
n = 5
a,b = 0,1
if n >= 2:
    for i in range(n):
        a,b = b,a+b
        print(a)

## using function
def fibonocci(n):
    a,b = 0,1
if n >= 2:
    for i in range(n):
        a,b = b,a+b
        print(a)
    else:
        print("greater than 2")

n = 6
fibonocci(n)

## Radius of circle --3.14 *r *r
r = 4
c = 3.14 * r * r
print(c)

## simple interest - ptr/100




