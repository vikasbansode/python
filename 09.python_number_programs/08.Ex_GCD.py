#!/usr/bin/python3

#############################################################
#															#
# Python Program to find GCD							    #
# Created on : 4/30/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : Using while loop          					 	
*********************************************
""")


a = float(input("Please enter the first value a: "))
b = float(input("Please enter the second value b: "))

i = 1

while(i <= a and i <= b):
	if(a % i == 0 and b % i == 0):
		gcd = i
	i = i + 1

print("\nHCF of {0} and {1} = {2}".format(a,b,gcd))


#############################################################

print("""
*********************************************
* Example 2 : Using while loop          					 	
*********************************************
""")

num1 = float(input("Please enter the first value a: "))
num2 = float(input("Please enter the second value b: "))

a = num1
b = num2

while(num2 != 0):
	temp = num2
	num2 = num1 % num2
	num1 = temp
	
gcd = num1
print("\nHCF of {0} and {1} = {2}".format(a,b,gcd))


#############################################################

print("""
*********************************************
* Example 3 : Using without Temp          					 	
*********************************************
""")

num1 = float(input("Please Enter the First Value Num1: "))
num2 = float(input("Please Enter the Second value Num2: "))

a = num1
b = num2

if(num1 == 0):
	print("\nHCF of {0} and {1} = {2}".format(a,b,b))

while (num2 != 0):
	if(num1 > num2):
		num1 = num1 - num2
	else:
		num2 = num2 - num1
gcd = num1
print("\nHCF of {0} and {1} = {2}".format(a,b,gcd))



#############################################################

print("""
*********************************************
* Example 4 : Using User Defined Function          					 	
*********************************************
""")

def findgcd(num1,num2):
	if(num1 == 0):
		print("\nHCF of {0} and {1} = {2}".format(a,b,b))
	
	while(num2 != 0):
		if(num1 > num2):
			num1 = num1 - num2
		else:
			num2 = num2 - num2
	return num1


a = float(input("Please Enter the First value a: "))
b = float(input("Please enter the second value b: "))

gcd = findgcd(a,b)
print("\nHCF of {0} and {1} = {2}".format(a,b,gcd))


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