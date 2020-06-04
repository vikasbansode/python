#!/usr/bin/python3

######################################################################
#															         #
# Python Program to check given key exits in a Dictionary       	 # 
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

myDict = {'a':'apple','b':'banana','c':'Cherry','d':'DragonFruit'}
print("Dictionary: ",myDict)

key = input("Please enter the key you want to search for: ")

# check whether the given key exists in a Dictionary or Not

if key in myDict.keys():
	print("\nKey Exists in this Dictionary")
	print("Key = ", key, " and value = ", myDict[key])
else:
	print("\nKey Does not exists in this Dictionary")

######################################################################

print("""
*********************************************
* Example 2 : USING IF STATEMENT					 	
*********************************************
""")

myDict = {'a': 'apple', 'b': 'Banana' , 'o': 'Orange', 'm': 'Mango'}
print("Dictionary : ", myDict)

key = input("Please enter the Key you want to search for: ")

# Check Whether the Given key exists in a Dictionary or Not
if key in myDict:
    print("\nKey Exists in this Dictionary")
    print("Key = ", key, " and Value = ", myDict[key])
else:
    print("\nKey Does not Exists in this Dictionary")
	
######################################################################

print("""
*********************************************
* Example 3 : USING IF STATEMENT					 	
*********************************************
""")	

myDict = {'a': 'apple', 'b': 'Banana' , 'o': 'Orange', 'm': 'Mango'}
print("Dictionary : ", myDict)

key = input("Please enter the Key you want to search for: ")

# Check Whether the Given key exists in a Dictionary or Not
if myDict.get(key) != None:
    print("\nKey Exists in this Dictionary")
    print("Key = ", key, " and Value = ", myDict[key])
else:
    print("\nKey Does not Exists in this Dictionary")
	
