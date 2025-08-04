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
