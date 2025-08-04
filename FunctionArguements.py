##positional Arguement
def display(email,name,pwd):
    print(name,email,pwd)
name,email,pwd="pardhu","paila123@gmail.com","pardhu088"
display(name,pwd,email)

##Variable-Length Arguements - it is used for key word arguement
def display(**v):
    print(v)
display(user_name="pardhu" , pwd="pardhu@088", attendece="absent" )

#Variable-Length Arguements 
def display(*p):
    print(p)
display("pardhu","paila123@gmail.com","pardhu088")

#key word arguements
def display(email,pwd,name,status='absent'):
    print(name,pwd,email,status)
display(name="pardhu",email="paila123@gmail.com",pwd="pardhu088")

#wishing the name
def wish(name):
    print(f"hi,{name} welcome to codegnan")
name=input("enter the name: ")
wish(name)


#
def update(n):
    print("Before inside of the function",n)
    n = n+10
    print("After inside of the function",n)

n=20
update(n)
print("outside of the function",n)

#recursion sum example
def sumofnum(n):
    if n==1:
        return 1
    return n+sumofnum(n-1)
n = int(input("enter the number:"))
print(sumofnum(n))

#factorial example on recursion
def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

n=int(input("Enter the value: "))
print(factorial(n))

##sum the numbers like 12345=15
n=int(input())
sum=0
for i in range :
    sum+=int(i)
print(sum)

#febinocci series
n = int(input("enter the number:"))
a = 0
b = 1
if n == 1:
    print(a)
elif n >= 2:
    print(a)
    print(b)
    for i in range(n-2):
        c = a+b
        print(c)
        a = b
        b = c


#LAMBDA FUNCTION
l=[1,2,3,4]
squ = list(map(lambda i: i**2,l))
print(squ)

k=[i for i in range(1,1) if i%2==0]
print(k)

##even or odd using lamda
iseven=lambda n: "even" if n%2==0 else "odd"
n=int(input())
print(iseven(n))

#sqauring lambda
square= lambda n: n*n
n= int(input())
print(square(n))

#function
def square(n):
    return n*n
n=int(input())
print(square(n))

#
def square(n):
    for i in range(len(n)):
        n(i)=n(i)**2
        return n
n=[1,2,3,5,4,56,8]
print(square(n))

##
squ=list(map(lambda l:i**2,l))
l=[1,2,3,5,4,8]
print(squ(l))
