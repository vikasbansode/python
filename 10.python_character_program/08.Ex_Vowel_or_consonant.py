#!/usr/bin/python3

#############################################################
#															#
# Python Program to check Vowel or Consonant     		    # 
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

ch = input("Please Enter Your Own Character : ")

if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A'
       or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
    print("The Given Character ", ch, "is a Vowel")
else:
    print("The Given Character ", ch, "is a Consonant")

#############################################################

print("""
*********************************************
* Example 2 : Using ASCII VALUES          					 	
*********************************************
""")

ch = input("Please Enter Your Own Character : ")

if(ord(ch) == 65 or ord(ch) == 69 or ord(ch) == 73
       or ord(ch) == 79 or ord(ch) == 85
       or ord(ch) == 97 or ord(ch) == 101 or ord(ch) == 105
       or ord(ch) == 111 or ord(ch) == 117):
    print("The Given Character ", ch, "is a Vowel")
elif((ord(ch) >= 97 and ord(ch) <= 122) or (ord(ch) >= 65 and ord(ch) <= 90)):
    print("The Given Character ", ch, "is a Consonant")

