#!/usr/bin/python3

#############################################################
#															#
# Python Program to find ASCII Value of Single Character    # 
# Special Character											#
# Created on : 05/01/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : using ord function          					 	
*********************************************
""")

ch = 'T'

print("The ASCII value of %c = %d" %(ch,ord(ch)))

#############################################################

print("""
*********************************************
* Example 2 : Using users input          					 	
*********************************************
""")

ch = input("Please enter any Character: ")

print("The ASCII Value of %c = %d" %(ch,ord(ch)))


print("""
*********************************************
* Example 3 : Return ASCII Value of Character          					 	
*********************************************
""")

ch = input("Please enter any Character  :  ")
print("The ASCII Value = %d" %ord(ch[0]))
