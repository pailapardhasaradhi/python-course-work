# 1.Even number
n = 5
if n % 2 == 0:
    print("even")
elif n % 2 != 0:
    print("odd")

# Using function
def is_even(n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd")
is_even(6)

## 2.prime number
n = 3
if n > 1:
    for i in range(2,n):
        if n % i ==  0:
            print('not a prime number')
            break
        else:
            print("prime number")


## Using function 
def is_prime(n):
    if n > 1:
        for i in range(2,n):
            if n % i ==  0:
                print('not a prime number')
                break
            else:
                print("prime number")
is_prime(4)

### 3. Factorial 
n = 5
fact = 1
for i in range(1,n+1):
    fact *= i
    print(fact)

# Using function
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
print(factorial(6))

### 4.multiplication Table
n = 4
for i in range(1,12):
    table = n * i
    print(f"{n} * {i} = {n * i}")
### using functions
def multiplication(n):
    for i in range(1,12):
        print(f"{n} * {i} = {n * i}")
        
multiplication(5)

## 5.Palindrome
s = "madam"
rs = s[::-1]
if s == rs :
    print("palindrome")
else:
    print("Not a palindrome")
## Using function
def is_palindrome(text):
    return text == text[::-1]
print(is_palindrome("noon"))

### 6.sum of the numbers
n = input("enter the num:")
sum = 0
for i in n:
  sum +=int(i) 
print(sum)

# using functions
def sumof_numbers(n):
    sum = 0
    for i in n:
        sum += int(i)
    return sum
n = input("enter the name:")
print(sumof_numbers(n))

### 7.Leap year
n = 2003
if (n % 4 == 0 and n % 100 != 0) or (n % 400 ==0) :
    print("Leap year")
else:
    print("its not a leap year")

## 8.string reversal
s = "pardhu"
rs = s[::-1]
print(rs)

## 9. Anagram
name1 = "listen"
name2 = "silent"
if sorted(name1) == sorted(name2):
    print("anagram")
else:
    print("false")

## 10.right angle triangle
n = 7
for i in range(n):
    print("*" * i)

##11.
n = 7
for i in range(n):
    print(" " * (n - i) + "*" * i)

## 12. pyramid
n = 6
for i in range(n):
    print(" " * (n - i) + "*" * (2*i - 1))
###factors of a number
n = 10
for i in range(1,10):
    if n % i == 0:
        print(i)

##
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
print(factorial(6))

##
def reverse(s):
    if s == s[::-1]:
    return s
    else:
return s == s[::-1]:

print(reverse("pardhu"))


