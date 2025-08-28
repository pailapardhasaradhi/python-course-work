### EXCEPTION HANDLING
try:
    a = int(input("Enter the Number:"))
    b = int(input("Enter the Number:"))
    s = input()
    print(a+s)
    print(a+b)
except ZeroDivisionError:
    print("b cannot br Zero")
except ValueError:
    print("please enter the integer value")
except TypeError:
    print("Enter the same type")
except IndexError:
    print("Enter the index within range")


### method 2
try:
    a = int(input("Enter the Number:"))
    b = int(input("Enter the Number:"))
    s = input()
    print(a+s)
    print(a+b)
except (ZeroDivisionError,ValueError,TypeError,IndexError) as e:
    print(f"error occured: {e}")
else:
    print("All inputs are perfect no xceptions you can run the remaining code")

### METHOD 3
try:
    a = int(input("Enter the a: "))
    b = int(input("Enter the b: "))
    s = int(input("Enter the string: "))   # if you want string, remove int()
    
    l = [1, 2, 3, 4, 5]
    d = {"name": "tarak", "course": "python"}
    
    print(d)
    
    k = input("Enter the key: ")
    print(d[k])   # will throw KeyError if invalid key
    
    print(l)
    
    ind = int(input("Enter the index value: "))
    print(l[ind])  # will throw IndexError if invalid index
    
    print(a + s)
    print(a / b)   # will throw ZeroDivisionError if b=0

except Exception as e:
    print(f"Error occurred: {e}")

else:
    print("✅ All inputs are perfect, no exceptions. You can run the remaining code.")

#### TO RAISE AN ERROR
try:
    a = int(input("Enter the a: "))
    if a < 0:
        raise Exception("Please enter a positive number")

except Exception as e:
    print(f"Error occurred: {e}")
    

else:
    print("All inputs are perfect, no exceptions. You can run the remaining code")

finally:
    print(a)
    