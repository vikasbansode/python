#!/usr/bin/python3

#############################################################
#															#
# Python Program to check character is Alphabet or Not   	#
# Created on : 4/30/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : Using If Statement          					 	
*********************************************
""")

ch = input("Please enter your Own Character: ")

if ((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
	print("The Given character ", ch, "is an Alphabet")
else:
	print("The given character ", ch,"is Not an Alphabet")
	

#############################################################

print("""
*********************************************
* Example 1 : Using If Statement & ASCII          					 	
*********************************************
""")

ch = input("Please Enter Your Own Character : ")

if((ord(ch) >= 65 and ord(ch) <= 90) or (ord(ch) >= 97 and ord(ch) <= 122)):
    print("The Given Character ", ch, "is an Alphabet")
else:
    print("The Given Character ", ch, "is Not an Alphabet")
	
#############################################################

print("""
*********************************************
* Example 1 : Using isalpha in built function        					 	
*********************************************
""")

ch = input("Please Enter Your Own Character : ")

if(ch.isalpha()):
    print("The Given Character ", ch, "is an Alphabet")
else:
    print("The Given Character ", ch, "is Not an Alphabet")
