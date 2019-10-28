total = 2
'''
#need a : at the end of an if statement
if total == 15:
    print("good")
else:
    print("bad")

if total % 2 == 0:
    print("even")
else:
    print("odd")

name = "Emma"

if len (name) > 7:
    print("perfect size")
else:
    print("not perfect")

#comparison operators
# == 
# >
# <
# >=
# <=
# != is not equal to


total = 6

if total > 15:
    print("good")
elif total > 10:
    print("reasonable")
elif total > 5:
    print ("bad")
else:
    print("disastrous")


grade = 45

if grade >= 80:
    print ("A")
elif grade >= 60:
    print ("B")
elif grade >= 50:
    print ("C")
else:
    print ("F")
'''

#a non-empty string is truthy and and empty string is falsey
if "hello world":
    print("yes, its true")

if "":
    print("its true")
else:
    print("it is false")

#any nunber that is not zero is truthy. 0 is falsey
if -8:
    print("it is true")

if 0:
    print("it is true")
else: 
    print("it is false")

a = -10
b = -11

if a > 0 or b < 0:
    print("Good!")

if a > 0 and b < 0:
    print("Excellent")
else:
    print("Not good")