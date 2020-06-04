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

ch = input("Please enter your own Character : ")

if(ch.isupper()):
	print("The given Character ", ch, " is an UpperCase Alphabet")
else:
	print("The given character ", ch, " is not an uppercase Alphabet")
	
#############################################################

print("""
*********************************************
* Example 2 : Using without in built function          					 	
*********************************************
""")

ch = input("Please Enter Your Own Character : ")

if(ch >= 'A' and ch <= 'Z'):
    print("The Given Character ", ch, "is an Uppercase Alphabet")
else:
    print("The Given Character ", ch, "is Not an Uppercase Alphabet")

#############################################################
	
print("""
*********************************************
* Example 3 : Using ASCII VALUES          					 	
*********************************************
""")

ch = input("Please Enter Your Own Character : ")

if(ord(ch) >= 65 and ord(ch) <= 90):
    print("The Given Character ", ch, "is an Uppercase Alphabet")
else:
    print("The Given Character ", ch, "is Not an Uppercase Alphabet")
