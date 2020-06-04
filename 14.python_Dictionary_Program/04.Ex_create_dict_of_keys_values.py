#!/usr/bin/python3

######################################################################
#															         #
# Python Program to CREATE DICTIONARY OF KEYS AND VALUES are SQUARE	 # 
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

number = int(input("please enter the Maximum number: "))
myDict = {}
for x in range(1,number + 1):
	myDict[x] = x**2
print("\nDictionary = ", myDict)

######################################################################

print("""
*********************************************
* Example 2 : USING SQUARE			 	
*********************************************
""")

number = int(input("Please enter the Maximum Number : "))
myDict = {x:x ** 2 for x in range(1, number + 1)}
print("\nDictionary = ", myDict)