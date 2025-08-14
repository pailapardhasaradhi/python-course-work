#### programs on conditional statements
## Positive or Negative
n = int(input("enter the number: "))
if n >= 0 :
    print("{n} is positive number")
elif n < 0:
    print("{n} is negative number ")

##Even or Odd
n = int(input("enter the number: "))
if n % 2 ==0 :
    print("even nummber")
else:
    print("odd number")

##Divisible by 5
n = int(input("enter the number: "))
if n % 5==0:
    print("divisble by 5")
else:
    print("it does not divisble by 5")

## Divisible by 3 and 7
n = int(input("enter the number: "))
if n % 3 == 0 and n % 7 == 0:
    print("it is divisible by 3 and 7")
else:
    print("it does not divisibe by both numbers")

## Check for Leap Year
year = int(input("Enter the year:"))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is leap year")
else:
    print("it is not a leap year ")

##factorial
n = 5
fact = 1
for i in range(1,n+1):
    fact *= i
print(fact)

#fibonacci series
n = 5
a = 0, b = 1
for i in range(n):
    print(a, end=" ")
    a,b = b ,a+b

##palindrome
text = "pardhu"
if text == text[:: -1]:
    print("palindrome")
else:
    print("not a palindrome")

##prime number
n = int(input("enter the name :"))
if n <= 1:
    for i in range(2,n+1):
        if n % i == 0:
            print("not a prime number")
            break
        else:
            print("prime number")
    else:
            print("not a prime number")

### 

