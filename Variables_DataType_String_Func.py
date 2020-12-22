import sys
import math
import random
import threading
import time
from functools import reduce

print("Hello World")

# ask for input
name = input("What is your name")

print("Hi", name)

# extends multiples lines

a = ('1' + '2' + '3' +
     '4' + '5'
     )

print(a)

v1 = 1 + 2 \
     + 3

print('Wow, this also works?',
      'I never knew!'
      )

v1 = 5; v1 -= 1

# Comment
'''
multi comment
'''

'''
Data type in python
floats, integer, complex number strings booleans
'''


print(type(10))
# print maxsize of the system
print(sys.maxsize)
print(sys.float_info.max)




# float inaccurate after 15 digits
f1 = 1.1111111111111111
f2 = 1.1111111111111111
f3 = f1 + f2
print(f3);

# real part + imaginary
cn1 = 5 + 6j

b1 = False;

str1 = "Escape Sequences \' \" \t \\ \n"
str2 = '''Triple Quoted'''

# type casting
print("Cast", type(int(5.4)))
print("Cast", type(str(5.4)))
print("Cast", type(chr(97)))
print("Cast", type(ord('a')))

print(12, 21, 1974, sep='/')
print("No Newline", end='')
print("\n%04d %s %.2f %c" % (1, "Derek", 1.234, 'A'))

print("5 + 2 = ", 5 + 2)
print("5 - 2 = ", 5 - 2)
print("5 * 2 = ", 5 * 2)
print("5 / 2 = ", 5 / 2)
print("5 % 2 = ", 5 % 2)
print("5 ** 2 = ", 5**2)
print("5 // 2 = ", 5//2) # integer divison

i1 = 2
i1 += 1
print("i1", i1)

# Math Functions
print("abs(-1) ", abs(-1))
print("max(5, 4) ", max(5, 4))
print("min(5, 4) ", min(5, 4))
print("pow(2, 2) ", pow(2, 2))
print("ceil(4.5) ", math.ceil(4.5))
print("floor(4.5) ", math.floor(4.5))
print("round(4.5) ", round(4.5))
print("exp(1) ", math.exp(1))  # e**x
print("log(e) ", math.log(math.exp(1)))
print("log(100) ", math.log(100, 10))  # Base 10 Log
print("sqrt(100) ", math.sqrt(100))
print("sin(0) ", math.sin(0))
print("cos(0) ", math.cos(0))
print("tan(0) ", math.tan(0))
print("asin(0) ", math.asin(0))
print("acos(0) ", math.acos(0))
print("atan(0) ", math.atan(0))
print("sinh(0) ", math.sinh(0))
print("cosh(0) ", math.cosh(0))
print("tanh(0) ", math.tanh(0))
print("asinh(0) ", math.asinh(0))
print("acosh(pi) ", math.acosh(math.pi))
print("atanh(0) ", math.atanh(0))
print("hypot(0) ", math.hypot(10, 10))  # sqrt(x*x + y*y)
print("radians(0) ", math.radians(0))
print("degrees(pi) ", math.degrees(math.pi))

print("Random", random.randint(1, 101))

print(math.inf > 0)

print(math.inf - math.inf)

#if else

age = 30
if age > 18:
    print("adult")
elif age < 10:
    print("kid")
else:
    print("teenager")

# and or not <-- logical operator

drinkingAge = True

if age > 18 and drinkingAge:
    print("you can drink")

# string

print(r"I'll be ignored \n")
print("Hello" + "You")
str3 = "Hello You"
print("Length", len(str3))
print("1st", str3[0])
print("Last", str3[-1])
print("1st 3 ", str3[0:3])
# start from index 0, then grab every 2nd index
print("Every other", str3[0:-1:2])


# str3[0] = "2" does not work

str3.replace("Hello", "GoodBye")

# go to index 8 replace it with y then go print out the rest
str3 = str3[:8] + "y" + str3[9:]
print(str3)

#check if the data in there
print("you" not in str3)

# find the string then return the index
print("You index", str3.find("you"))

#remove space

print("  Hello ".strip())

#join strings

print(" ".join(["Some", "Words"]))

# return an array

print("A string".split(" "))

int1 = int2 = 5

print(f'{int1} + {int2} = {int1 + int2}')

#case sensitive manipulation

print("A String".lower())
print("A String".upper())

print("A String 123".isalnum())
print("A String".isalpha())
print("123"
      "".isdigit())
