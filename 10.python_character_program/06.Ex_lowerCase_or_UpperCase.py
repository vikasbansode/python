#!/usr/bin/python3

#############################################################
#															#
# Python Program to check LowerCase or UpperCase		    # 
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

ch = input("Please Enter Your Own Character: ")

if(ch.isupper()):
	print("The given character ", ch, " is an UpperCase Alphabet")
elif(ch.islower()):
	print("The given character ", ch," is a LowerCase Alphabet")
else:
	print("The given character ", ch," is not a lower or uppercase alphabet")

#############################################################

print("""
*********************************************
* Example 2 : Using without in built function          					 	
*********************************************
""")

ch = input("Please Enter Your Own Character: ")

if(ch >= 'A' and ch <= 'Z'):
	print("The given character ",ch," is an Uppercase Alphabet")
elif(ch >= 'a' and ch <= 'z'):
	print("The given character ",ch, " is a lowercase Alphabet")
else:
	print("The given character", ch," is not a Lower or or uppercase Alphabet")


#############################################################

print("""
*********************************************
* Example 3 : Using ASCII VALUES         					 	
*********************************************
""")


ch = input("Please Enter Your Own Character: ")

if(ord(ch) >= 65 and ord(ch) <= 90):
	print("The given character ", ch, " is an uppercase Alphabet")
elif(ord(ch) >= 97 and ord(ch) <= 122):
	print("The given Character ", ch, "is a lowercase Alphabet")
else:
	print("The given character ", ch, " is not a lower or UpperCase Alphabet")
