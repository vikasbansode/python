#!/usr/bin/python3

#########################################################
#														#
# python program to find largets of two numbers			#
# Created on : 4/28/2020								#
# Author     : Vikas Bansode							#
#														#
#########################################################


print("Example 1 : using if statement")
print()
a = float(input("Please enter the first number: "))
b = float(input("Please enter the second number: "))

if( a > b):
	print("{0} is greater than {1}".format(a,b))
elif(b > a):
	print("{0} is greater than {1}".format(b,a))
else:
	print("both {0} and {1} are equal".format(a,b))
	
print()
print("#########################################################")
print()
print("Example 2 : using nested if")

a = float(input("Please enter the first number: "))
b = float(input("Please enter the second number: "))

if(a > b):
	print("{0} is greater than {1}".format(a,b))
else:
	largest = a if a > b else b
	print("{0} is the Largest Value".format(largest))
	
print()
print("#########################################################")
print()
print("Example 3 : using nested if")

a = float(input("Please enter the first value: " ))
b = float(input("Please enter the second value: "))

if(a - b > 0):
	print("{0} is greater than {1}".format(a,b))
elif(b - a > 0):
	print("{0} is greater than {1}".format(b,a))
else:
	print("{0} and {1} are equal numbers".format(a,b))


print()
print("#########################################################")
print()
print("Example 4 :")

a = float(input("Please enter first number: "))
b = float(input("Please enter second number: "))
c = float(input("please enter third number: "))

if( a > b and a > c):
	print("{0} is greater than both {1} and {2}".format(a,b,c))
elif(b > a and b > c):
	print("{0} is greater than both {1} and {2}".format(b,a,c))
elif(c > a and c > b):
	print("{0} is greater than both {1} and {2}".format(c,a,b))
else:
	print("Either any two values or all the three values are equal")
	
	
print()
print("#########################################################")
print()
print("Example 5 :")	


a = float(input("Please Enter the First value: "))
b = float(input("Please Enter the First value: "))
c = float(input("Please Enter the First value: "))

if (a-b > 0) and (a-c > 0):
    print("{0} is Greater Than both {1} and {2}". format(a, b, c))
else:
    if(b - c > 0):
        print("{0} is Greater Than both {1} and {2}". format(b, a, c))
    else:
        print("{0} is Greater Than both {1} and {2}". format(c, a, b))
		