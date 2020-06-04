#!/usr/bin/python3

######################################################################
#															         #
# Python Program to Multiply All Items in a Dictionary			 	 # 
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

myDict = {'x': 20, 'y':5, 'z':60}
print("Dictionary: ", myDict)

total = 1
# Multiply Items
for key in myDict:
    total = total * myDict[key]
    
print("\nAfter Multiplying Items in this Dictionary: ", total)

######################################################################

print("""
*********************************************
* Example 2 : USING FOR LOOP	 	
*********************************************
""")

myDict = {'x': 2, 'y':50, 'z':70}
print("Dictionary: ", myDict)

total = 1
# Multiply Items
for i in myDict.values():
    total = total * i
    
print("\nAfter Multiplying Items in this Dictionary: ", total)
