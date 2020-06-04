#!/usr/bin/python3

#############################################################
#															#
# Python Program to check LowerCase or Not				    # 
# Special Character											#
# Created on : 05/01/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : Using If Statement          					 	
*********************************************
""")

ch = input("Please enter Your Own Character: ")

if(ch.islower()):
	print("The given character ", ch," is a LowerCase Alphabet")
else:
	print("The given Character ",ch," is not a LowerCase Alphabet")

print("""
*********************************************
* Example 2 : Using ASCII Values          					 	
*********************************************
""")

ch = input("Please Enter Your Own Character: ")

if(ord(ch) >= 97 and ord(ch) <= 122):
	print("The given character ", ch," is a LowerCase Alphabet")
else:
	print("The given character ",ch, "is not a lowercase Alphabet")
	
	