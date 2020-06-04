#!/usr/bin/python3

#############################################################
#															#
# Python Program to find LCM of two Numbers				    #
# Created on : 4/30/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : Using if Statement          					 	
*********************************************
""")

a = float(input("Please enter the first value a: "))
b = float(input("Please Enter the second value b: "))

if (a > b):
	maximum = a
else:
	maximum = b

while(True):
	if(maximum % a == 0 and maximum % b == 0):
		print("\nLCM of {0} and {1} = {2}".format(a,b,maximum))
		break;
	maximum = maximum + 1

#############################################################

print("""
*********************************************
* Example 2 : Using user Defined function          					 	
*********************************************
""")

def findlcm(a,b):
	if(a > b):
		maximum = a
	else:
		maximum = b
	while(True):
		if(maximum % a == 0 and maximum % b == 0):
			lcm = maximum
			break;
		maximum = maximum + 1
	return lcm
	
num1 = float(input(" Please Enter the First Value  Num1 : "))
num2 = float(input(" Please Enter the Second Value Num2 : "))
lcm = findlcm(num1, num2)
print("\n LCM of {0} and {1} = {2}".format(num1, num2, lcm))


# first value * second value / GCD

#############################################################

print("""
*********************************************
* Example 3 : Using GCD          					 	
*********************************************
""")

num1 = float(input(" Please Enter the First Value  Num1 : "))
num2 = float(input(" Please Enter the Second Value Num2 : "))

a = num1
b = num2

while(num2 != 0):
    temp = num2
    num2 = num1 % num2
    num1 = temp

gcd = num1
print("\n GCD of {0} and {1} = {2}".format(a, b, gcd))
lcm = (a * b) / gcd

#############################################################

print("""
*********************************************
* Example 4 : Using Recursion Function          					 	
*********************************************
""")

def findgcd(a, b):
    if(b == 0):
        return a;
    else:
        return findgcd(b, a % b)
    
num1 = float(input(" Please Enter the First Value  Num1 : "))
num2 = float(input(" Please Enter the Second Value Num2 : "))

gcd = findgcd(num1, num2)
print("\n GCD of {0} and {1} = {2}".format(num1, num2, gcd))

lcm = (num1 * num2) / gcd
print("\n LCM of {0} and {1} = {2}".format(num1, num2, lcm))

