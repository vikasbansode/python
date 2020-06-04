#!/usr/bin/python3

#############################################################
#															#
# Python Program to check Digit or Not					    # 
# Special Character											#
# Created on : 4/30/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : Using If Statement          					 	
*********************************************
""")

ch = input("Please Enter Your Own Character : ")

if(ch >= '0' and ch <= '9'):
    print("The Given Character ", ch, "is a Digit")
else:
    print("The Given Character ", ch, "is Not a Digit")
	
#############################################################

print("""
*********************************************
* Example 2 : Using ASCII          					 	
*********************************************
""")

ch = input("Please Enter Your Own Character : ")

if(ord(ch) >= 48 and ord(ch) <= 57):
    print("The Given Character ", ch, "is a Digit")
else:
    print("The Given Character ", ch, "is Not a Digit")

#############################################################

print("""
*********************************************
* Example 3 : Using isalpha          					 	
*********************************************
""")

ch = input("Please Enter Your Own Character : ")

if(ch.isdigit()):
    print("The Given Character ", ch, "is a Digit")
else:
    print("The Given Character ", ch, "is Not a Digit")
	

	
