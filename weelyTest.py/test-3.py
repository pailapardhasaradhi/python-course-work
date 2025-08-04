##1.calculating BMI - weight/(height*)
def calculate_bmi(weight,height):
    bmi = weight / (height * height)
    return bmi
weight = int(input("enter the num : "))
height = float(input("enter the num : "))
print("bmi:%.2f" %calculate_bmi(weight,height))

##2.filter even numbers
def filter_even(l):
    result = []
    for i in l:
        if i % 2 == 0:
            result.append(i)
    return result
l = [1,2,3,4,5,6,7,9,90,10]
print(filter_even(l))

##3.GENERATE A MULTIPLICATION TABLE
def generate_table(t):
    for i in range(1,13):
       print(f"{t} * {i} = {t *i}")
    return table
t = int(input("enter the number:"))
generate_table(t)

## 4.CHECK ANAGRAM 
'''str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()'''
    
def is_anagram(str1,str2):
    return sorted(str1) == sorted(str2)
str1 = "pardhu"
str2 = "ardhup"
if is_anagram(str1,str2):
    print("It Is Anagram")
else:
    print("It is not a Anagram")

### COUNT WORD OCCURENCE
def count_words(text):
    