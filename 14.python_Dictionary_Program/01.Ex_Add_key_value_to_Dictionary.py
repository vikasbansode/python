#!/usr/bin/python3

######################################################################
#															         #
# Python Program to Add key-value pair to a Dictionary       		 # 
# Special Character											         #
# Created on : 05/03/2020									         #
# Author     : Vikas Bansode								         #
#															         #
######################################################################

print("""
*********************************************
* Example 1 : USING UPDATE FUNCTION					 	
*********************************************
""")

key = input("Please enter the Key : ")
value = input("Please enter the Value : ")

myDict = {}

# Add Key-Value Pair to a Dictionary in Python
myDict.update({key:value})
print("\nUpdated Dictionary = ", myDict)

######################################################################

print("""
*********************************************
* Example 2 : USING slicing					 	
*********************************************
""")

key = input("Please enter the Key : ")
value = input("Please enter the Value : ")

myDict = {}

# Add Key-Value Pair to a Dictionary in Python
myDict[key] = value
print("\nUpdated Dictionary = ", myDict)