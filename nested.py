for row in range(5):
    for col in range(5):
        print("*",end='')
    print()

   
###
for row in range(5):
    for col in range(5):
        print(col,end='')
    print()
     
#####
    for row in range(5):
     for col in range(row+1):
        print("*",end='')
     print()
####
for row in range(5):
    for col in range(5-row):
       print("*",end='')
    print()

####
for row in range(5):
    for col in range(5-row-1):
           print('',end='')
    for col in range(row+1):
            print('*',end='')
    print()

#####ZERO
n= int(input("enter the number:"))
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or col==n-1:
           print("*",end='')
        else:
           print(' ',end='')
    print()
       

###X
n= int(input("enter the number:"))
for row in range(n):
    for col in range(n):
        if row+col==n-1 or row==col:
           print("*",end='')
        else:
           print(' ',end='')
    print()


###
for i in range(5):
    for j in range(5):
        if j == 0 or i==0 or (j==4 and i<=2) or i == 2 or (i == j and i>=2):
            print("*",end='')
            
        
