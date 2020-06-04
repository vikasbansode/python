#!/usr/bin/python3

#############################################################
#															#
# Python Program to check character is Alphabet, Digit or   # 
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

if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')): 
    print("The Given Character ", ch, "is an Alphabet") 
elif(ch >= '0' and ch <= '9'):
    print("The Given Character ", ch, "is a Digit")
else:
    print("The Given Character ", ch, "is a Special Character")
	
#############################################################

print("""
*********************************************
* Example 2 : Using ASCII         					 	
*********************************************
""")	

ch = input("Please Enter Your Own Character : ")

if(ord(ch) >= 48 and ord(ch) <= 57): 
    print("The Given Character ", ch, "is a Digit") 
elif((ord(ch) >= 65 and ord(ch) <= 90) or (ord(ch) >= 97 and ord(ch) <= 122)):
    print("The Given Character ", ch, "is an Alphabet")
else:
    print("The Given Character ", ch, "is a Special Character")

#############################################################

print("""
*********************************************
* Example 2 : Using  isalpha,isdigit         					 	
*********************************************
""")

ch = input("Please Enter Your Own Character : ")

if(ch.isdigit()):
    print("The Given Character ", ch, "is a Digit")
elif(ch.isalpha()):
    print("The Given Character ", ch, "is an Alphabet")
else:
    print("The Given Character ", ch, "is a Special Character")

