name='pardhu'
surname='paila'
result=name+ surname
print(result)

#concantation - it means it adds two strings
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)

#repetation- it is used to repeat strings how many times u want
wish = 'hi hello'*3
print(wish)

slogan= "babulake babu kalyan babu" *5
print(slogan)

#Indexing - it prints the particular character
name="pardhupaila"
print(name[3])
print(name[-5])
name="pardhu paila"
print(name[5])

#slicing - it means it prints  more characters in the string
name ="pardhu paila"
print(name[0:5])
print(name[0:6])
print(name[6:])

#membersship - it used to wether the character is present in  the string or not
name ="pardhu paila"
print("pardhu" in name)
print("paila" not in name )
print("pardha" in name)
print("pardh" in name)

##built in functions 

# len() - it used to print the length of the string
name ="pardhu paila"
print(len(name))
name ="pardhupaila"
print(len(name))

# max() - it used to print max or min value in the string according to ascii value
name ="pardhupaila"
print(min(name))
print(max(name))
print(min(name))

#sort() -  it gives order of the characters according to the ascii value
numbers ="2,6,7,3,2,1,4"
print(sorted(numbers))
name ="pardhu"
print(sorted(name))

#char() - Converts an integer (ASCII value) to a characte
print(chr(30))
print(chr(50))
print(chr(69))

#ord() -  Converts a character to its ASCII (Unicode) integer value
print(ord("b"))
print(ord("c"))
print(ord("g"))

###case conversions
# upper()- to convert capital letters
name ="pardhupaila"
print(name.upper())
name ="jaya janaki nayaka"
print(name.upper())
print("pardhu".upper())

#lower()- to convert small letters
name ="PARDHU PAILA"
print(name.lower())
name ="JAYA JANAKI NAYAKA"
print(name.lower())

#capitalize - to give capital letter for first letter of the sentence
name = "pardhupaila"
print(name.capitalize())
name = "ardhupaila"
print(name.capitalize())
name="ardhya gandivalasa"
print(name.capitalize())

#tittle - it gives capital letter to first letter of every sentence
name = "pardhu paila"
print(name.title())
name="ardhya gandivalasa"
print(name.title())
name='ardhya gandivalasa'
print(name.title())

##swap case - it converts uppercase to lower case vise versa
name="ardhya gandivalasa"
print(name.swapcase())
name = "pardhu paila"
print(name.swapcase())
name="PARDHASARADHI"
print(name.swapcase())

#casefold - it is similar to lower()
name = "PARDHUPAILA"
print(name.casefold())
name="pardhupaila"
print(name.casefold())

#alignments & formatting

#center() - it puts the sentence in the center(width value,"any symbol")
name ="pardhu"
print(name.center(20,"-"))
name="paila"
print(name.center(30,"#"))

#ljust()- it gives the symbol from left side of the sentence
name ="ardhya"
print(name.ljust(10,"/"))
print(name.ljust(10,"*"))

#rjust() - it gives the symbol from right side of the sentence
name ="pardhu paila"
print(name.rjust(20,"^"))

#zfill() - it adds the zeros to the sentence from left side
name ="pardhu"
print(name.zfill(10))
name ="pardhu"
print(name.zfill(20))

#format() -to insert a sentence in the {}
name ="pardhu is a {} boy"
print(name.format("good"))

name ="Aradhya is a {} girl"
print(name.format("little"))

#format_map() - it is also insert a data in to the strings
data={"name":"pardhu", "branch": "ece"}
print("name:{name}, branch:{branch}".format_map(data))