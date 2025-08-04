#addition
def add(a,b):
    return a+b
a=int(input())
b= int(input())
print(add(a,b))

#subtraction
def sub(a,b):
    return a-b
a = int(input())
b = int(input())
print(sub(a,b))

#factorial-n! = n × (n - 1) × (n - 2) × ... × 1
#iterative function
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
num=int(input("enter the num:"))
for i in range(1,num+1):
    print(f"{i}!={factorial(i)}")

##recursive function:
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
n=int(input())
print(factorial(n)) 


#sum of recursion
def sumofnumber(n):
    s=0
    for i in range(1,n+1):
        s+=i
        return s
    n= int(input())
    print(f"{n}!={sumofnumber(i)}")

###sum the numbers like 12345=15
n=input("enter the num")
sum=0
for i in n:
    sum+=int(i)
print(sum)

#fibonocci series
n=int(input("Enter the number:" ))
a=0
b=1
if n==1:
    print(a)
elif n>=2:
    print(a)
    print(b)
for i in range(n-2):
    c=a+b
    print(c)
    a=b
    b=c
##calculating radius of circle
radius = float(input("Enter radius: "))
pi = 3.14
area = pi * radius * radius
print("Area of circle is:", round(area, 2))

#calculating radius of circle using function {3.14*r*r}
def circle(r):
    return 3.14*r*r
r=int(input())
print("Area of circle is:", round(circle(r), 2))

#wishing the user
def wish(name):
    print(f"hello,{name}")
    
name=input()
wish(name)

#convert celsius to Fahrenheit--{(c * 9/5) + 32}
def conversion(temp):
    return (temp * 9/5)+32
temp = float(input())
print(conversion(temp))

##multiplying the three numbers
def multiply(a, b, c):
    return a * b * c

a, b, c = map(int, input("Enter 3 numbers separated by space: ").split())
print(multiply(a, b, c))

#simple interest = (p * t * r)/100
def interest(p,t,r):
    return (p * t * r)/100
p,t,r=map(int,input("Enter the numbers: ").split())
print(interest(p,t,r))

#length of the string
def length(s):
    return len(s)
s= input()
print(length(s))

##appending a list
def append(lst, element):
    lst.append(element)
    return lst
lst=[1,2,3,4]
element=5
print(append(lst, element))

##Double Each Element in a List
def double_elements(lst):
    return [l * 2 for l in lst]
lst = [1,2,3,4]
print(double_elements(lst))

#sorting a list
def sort(l):
    return l.sort()
l=[1,2,3,6,1,2,3,7,7]
print(sort(l))

##12. Clear a List Inside Function
def clear(l):
    l.clear()
    return l
l=[1,2,3,1]
print(clear(l))

## Update Dictionary Value
def update(dic):
    dic.update(a=2)
    return dic
dic={'a':1,'b':4}
print(update(dic))

#Remove Element from List by Value
def remove(l):
    l.remove(3)
    return l
l=[1,2,3,4,5,6]
print(remove(l))

#Add Key to Dictionary
def add(l):
    l.add(y= 20)
    return l
l={a:10}
print(add(l))

#Add Key to Dictionary
def add(d):
    d['y']= 20
    return d
d={'a':10}
print(add(d))

#Increment All Values in Dictionary
def increment(d):
    for i in d:
        d[i] = d[i] + 1
    return d

d = {'a': 1, 'b': 2, 'c': 3}
print(increment(d))

##Factorial of a Number
def factorial(f):
    fact = 1
    for i in range(1, f+1):
        fact*=i
    return fact
f=int(input("enter the number:"))
print(factorial(f))

##Fibonacci Number (Nth Term)
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

n = int(input("Enter the term number (n): "))
print(f"{n}th Fibonacci number is:", fibonacci(n))

##Fibonacci Series Using Loop
n = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci Series:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

#Sum of First N Natural Numbers
def sum_natural(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input("Enter a number: "))
print("Sum is:", sum_natural(n))

#Reverse a String Using Recursion
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return(s[1:] + s[0])
    s = input()
    print(reverse_string(s))