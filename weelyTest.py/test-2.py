def update(n):
    print("Before inside of the function",n)
    n = n+10
    print("After inside of the function",n)

n=20
update(n)
print("outside of the function",n)
