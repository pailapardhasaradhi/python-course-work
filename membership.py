# membership operaters

names=['venky', 'sangee', 'ritu', 'rushi']
print('in result:','sandy' in names)#in result: False
print('not in result:','sahas' in names)#not in result: False


# idently operaters
l=[1,2,3,4]
b=[1,2,3,4]
print('l is b:', l is b)
a=b # assin b to a
print("a is b:", a is b)
print("id(l)", id(l))
print("id(b)", id(b))
print("id(a)", id(a))
print("a is not b:", a is b)

#bitwise operater
'''1-0001
2-010
3-011
4-100
5-101
6-110
7-111

3-011
5-101
-----'''
x = 5 # Binary: 0101
y = 3 # Binary: 0011
print(x & y) # Output: 1 (Binary: 0001 → AND operation)
print(x | y) # Output: 7 (Binary: 0111 → OR operation)
print(x ^ y) # Output: 6 (Binary: 0110 → XOR operation)
print(~x) # Output: -6 (Binary: Inverts bits of 5)
print(x << 1) # Output: 10 (Binary: 1010 → Shifts left by 1)
print(x >> 1) # Output: 2 (Binary: 0010 → Shifts right by 1)

print('3&5: ',3&5)#1
'''5-101
6-110
------
5^6=011=3'''
print("5^6: ",5^6)#3
'''1-001
--------
-1=001
----'''
print("~1:",~1)#-2
'''2<<1
2=010
4=100'''
print("4>>1: ",4>>1)#4>>1:2

'''4>>1
4=100
2=010'''
print("4>>1: ",4>>1)#4>>1: 2

