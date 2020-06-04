#!/usr/bin/python3

######################################################################
#															         #
# Python Program to Sum of Items in a Dictionary    			 	 # 
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

myDict = {'x': 250, 'y':500, 'z':410}
print("Dictionary: ", myDict)

# Print Values using get
print("\nSum of Values: ", sum(myDict.values()))

######################################################################

print("""
*********************************************
* Example 2 : USING FOR LOOP	
*********************************************
""")

myDict = {'x': 250, 'y':500, 'z':410}
print("Dictionary: ", myDict)
total = 0

# Print Values using get
for i in myDict.values():
    total = total + i
    
print("\nThe Total Sum of Values : ", total)

######################################################################

print("""
*********************************************
* Example 3 : USING FOR LOOP	
*********************************************
""")

myDict = {'x': 250, 'y':500, 'z':410}
print("Dictionary: ", myDict)
total = 0

# Print Values using get
for i in myDict:
    total = total + myDict[i]
    
print("\nThe Total Sum of Values : ", total)