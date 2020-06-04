#!/usr/bin/python3

######################################################################
#															         #
# Python Program to Remove given key from a Dictionary			 	 # 
# Special Character											         #
# Created on : 05/03/2020									         #
# Author     : Vikas Bansode								         #
#															         #
######################################################################

print("""
*********************************************
* Example 1 : USING IF STATEMENT	 	
*********************************************
""")

myDict = {'name': 'John', 'age': 25, 'job': 'Developer'}
print("Dictionary Items  :  ",  myDict)

key = input("Please enter the key that you want to Delete : ")

if key in myDict:
    del myDict[key]
else:
    print("Given Key is Not in this Dictionary")
    
print("\nUpdated Dictionary = ", myDict)

######################################################################
print("""
*********************************************
* Example 2 : USING IF STATEMENT	 	
*********************************************
""")

myDict = {'name': 'John', 'age': 25, 'job': 'Developer'}
print("Dictionary Items  :  ",  myDict)

key = input("Please enter the key that you want to Delete : ")

if key in myDict.keys():
    del myDict[key]
else:
    print("Given Key is Not in this Dictionary")
    
print("\nUpdated Dictionary = ", myDict)

######################################################################
print("""
*********************************************
* Example 3 : USING IF STATEMENT	 	
*********************************************
""")

myDict = {'name': 'John', 'age': 25, 'job': 'Developer'}
print("Dictionary Items  :  ",  myDict)

key = input("Please enter the key that you want to Delete : ")

if key in myDict.keys():
    print("Removed Item  :  ", myDict.pop(key))
else:
    print("Given Key is Not in this Dictionary")
    
print("\nUpdated Dictionary = ", myDict)