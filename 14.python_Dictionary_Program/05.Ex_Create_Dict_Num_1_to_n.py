#!/usr/bin/python3

######################################################################
#															         #
# Python Program to CREATE DICTIONARY OF NUMBERS 1 to N in(x,x*x)	 # 
# Special Character											         #
# Created on : 05/03/2020									         #
# Author     : Vikas Bansode								         #
#															         #
######################################################################

print("""
*********************************************
* Example 1 : USING FOR LOOP			 	
*********************************************
""")

number = int(input("Please enter the maximum Number: "))
myDict = {}

for x in range(1,number + 1):
	myDict[x] = x * x
	
print("\nDictionary = ", myDict)

######################################################################

print("""
*********************************************
* Example 2 : USING * OPERATOR			 	
*********************************************
""")

number = int(input("Please enter the Maximum Number : "))

myDict = {x:x * x for x in range(1, number + 1)}

print("\nDictionary = ", myDict)

