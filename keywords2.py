import keyword

print(keyword.kwlist) # List of all keywords
print(len(keyword.kwlist)) # Total number of keywords 35


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