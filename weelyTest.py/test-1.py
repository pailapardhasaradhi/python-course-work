##c1.hanging the age format
#type-1
date,month,year=input().split('-')
print(f"{year}/{month}/{date}")
##type-2
date=input("enter the date: ")
dd,mm,yyyy=date.split('-')
formatted_date=f"{yyyy}/{mm}/{dd}"
print(formatted_date)

#2. check the number is even or odd
num=int(input("enter the number:"))
if num % 2==0:
    print("it is a even number")
elif num %2!=0:
    print("it is not a even number")

#3.E replace with *
##type-1
alp=input()
alp=alp.replace('a',"*")
alp=alp.replace('e',"*")
alp=alp.replace('i',"*")
alp=alp.replace('o',"*")
alp=alp.replace('u',"*")
alp=alp.replace('s',"*")
print(alp)
##type-2
name=input()
print(name.translate(str.maketrans('aeiou','*****')))

##4.printing total and maximum number
list=list(map(float,input().split()))
print(sum(list))
print(max(list))

#5.login credentials:
credentials=("pardhu","pardhu@088")
username=input()
password=input()
if credentials[0]==username and credentials[1]==password:
    print("Login successful")
else:
    print("Access Denied")

##set operation
set=set(input("")).split()
print(set)