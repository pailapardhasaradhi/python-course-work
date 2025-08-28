#### REGULAR EXPRESSION (RegEx)
## match
import re
res = re.match(r'hello','hello world')
print(res.group() if res else "no match" )
##  MATCH -checking for pattern
import re
res = re.match(r'\d','6378 oqjudbnusm')
res = re.match(r'[a-z]','puegfyfhj')
res = re.match(r'[a-z]','puegfyfhj')
res = re.match(r'[A-Z]','PUegfyfhj')
res = re.match(r'[0-9]','PUegfyfhj')
print(res.group() if res else "no match")

### SEARCH FUNCTION - it give single matched character it checks entire string
import re
res = re.search(r'0','hello world 089')
print(res.group() if res else "no match" )

## FIND ALL - IT GIVES ALL CHARACTERS WHICH ARE MATCHES 
import re
res = re.findall(r'0','hello world 089')
print(res.group() if res else "no match" )


import re
res = re.finditer(r'[0-9]{2}','hello world 76 56 30')
for i in res:
    print(i.group(),i.start())

import re 
res = re.fullmatch(r'[0-9]{2}','hello world 76 56 30')
print(res.group() if res else "no match" )



import re
res = re.split(r'[,:/0;]','dinesh,sanjay;jaswanth/mohit0tarak')
print(res)

text = 'java programming language'
res = re.sub(r'[a-z]','*')

import re

def validate_name(name):
    # Allow 2–25 letters for first name, optional last name (also 2–25 letters)
    pattern = r'^[A-Za-z]{2,25}( [A-Za-z]{2,25})?$'
    return bool(re.fullmatch(pattern, name))

print(validate_name("Pardhu"))         
print(validate_name("Pardhu Paila"))   
print(validate_name("Pa"))             
print(validate_name("P"))              
print(validate_name("Pardhu123"))      

# EMAIL VALIDATIONdef validate_name(name):
import re

def validate_name(name):
    # Allow 2–25 letters for first name, optional last name (also 2–25 letters)
    pattern = r'^[A-z0-9._]+@[a-z.-]+\.[A-z.-]{2,3}?$'
    return bool(re.fullmatch(pattern, name))
print(validate_name("pardhupaila"))
print(validate_name("Pardhu123"))
print(validate_name("PailaPardhu123@gmail.com"))

###  PHONE NUMBER
import re

def validate_name(name):
    
    pattern = r'^[A-z0-9._]+@[a-z.-]+\.[A-z.-]{2,3}?$'
    return bool(re.fullmatch(pattern, name))
print(validate_name("pardhupaila"))
print(validate_name("Pardhu123"))
print(validate_name("PailaPardhu123@gmail.com"))

### PASSWORD
import re

def validate_password(password):
    # At least one uppercase, one lowercase, one digit, one special char, min length 8
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return bool(re.fullmatch(pattern, password))


# Examples
print(validate_password("Pardhu@123"))   # ✅ True
print(validate_password("pardhu123"))    # ❌ False (no uppercase, no special char)
print(validate_password("PARDHU@123"))   # ❌ False (no lowercase)
print(validate_password("Pardhuuuu"))    # ❌ False (no digit, no special char)

