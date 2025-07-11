#1. Arithmetic Operators
a=10
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
#2. Comparison Operators
x=10
y=5
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=10)
print(y<=5)


#3. Assignment Operators

x=20
x += 5
x -= 10
x *= 2
x /= 5
x //= 3
x %= 3
x **= 5
print(x)

#4. Logical Operators (Using Logic Gates)

x=10
y=5
print(x>5 and y>3)
print(x>y or x<y)
print(not (x>y))

#5. Membership Operators
#Membership operators check if a value exists within a sequence (like a list, string, or tuple).
fruits=["banana","apple","graps"]
print("apple" in fruits)
print("orang" not in fruits)

#6. Identity Operators
#Identity operators check whether two variables refer to the same object in memory.
a=[1,2,3]
b=a
c=[1,2,3]
print(a is c)
print(a is b)
print(a is not c)