#!/usr/bin/python3

#############################################################
#															#
# Python Program to print characters in string              # 
# Special Character											#
# Created on : 05/01/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : USING FOR LOOP      					 	
*********************************************
""")

str1 = input("Please Enter your Own String : ")
 
for i in range(len(str1)):
    print("The Character at %d Index Position = %c" %(i, str1[i]))
	
	
#############################################################

print("""
*********************************************
* Example 2 : USING WHILE LOOP      					 	
*********************************************
""")

str1 = input("Please Enter your Own String : ")
i = 0

while(i < len(str1)):
    print("The Character at %d Index Position = %c" %(i, str1[i]))
    i = i + 1
	
