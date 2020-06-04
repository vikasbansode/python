#!/usr/bin/python3

#############################################################
#															#
# Python Program to Toggle Character case in a string	    # 
# Special Character											#
# Created on : 05/01/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : USING SWAPCASE FUNCTION  					 	
*********************************************
"""

string = input("Please Enter your Own String : ")

string1 = string.swapcase()
 
print("\nOriginal String                      =  ", string)
print("The Given String After Toggling Case =  ", string1)

#############################################################

print("""
*********************************************
* Example 2 : USING FOR LOOP  					 	
*********************************************
"""

string = input("Please Enter your Own String : ")

string1 = ''

for i in range(len(string)):
    if(string[i] >= 'a' and string[i] <= 'z'): 
        string1 = string1 + chr((ord(string[i]) - 32)) 
    elif(string[i] >= 'A' and string[i] <= 'Z'):
        string1 = string1 + chr((ord(string[i]) + 32))
    else:
        string1 = string1 + string[i]
 
print("\nOriginal String                      =  ", string)
print("The Given String After Toggling Case =  ", string1)

#############################################################

print("""
*********************************************
* Example 3 : USING WHILE LOOP  					 	
*********************************************
"""

string = input("Please Enter your Own String : ")

string1 = ''
i = 0

while(i < len(string)): 
    if(string[i] >= 'a' and string[i] <= 'z'): 
        string1 = string1 + chr((ord(string[i]) - 32)) 
    elif(string[i] >= 'A' and string[i] <= 'Z'):
        string1 = string1 + chr((ord(string[i]) + 32))
    else:
        string1 = string1 + string[i]
    i = i + 1
 
print("\nOriginal String                      =  ", string)
print("The Given String After Toggling Case =  ", string1)

