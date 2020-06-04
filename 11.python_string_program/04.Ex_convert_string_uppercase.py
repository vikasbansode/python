#!/usr/bin/python3

#############################################################
#															#
# Python Program to Convert string to uppercase	            # 
# Special Character											#
# Created on : 05/01/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : Basic       					 	
*********************************************
""")


string = input("Please Enter your Own String : ")

string1 = string.upper()
 
print("\nOriginal String in Lowercase  =  ", string)
print("The Given String in Uppercase =  ", string1)

#############################################################

print("""
*********************************************
* Example 2 : Using for Loop       					 	
*********************************************
""")

string = input("Please Enter your Own String : ")
string1 = ''

for i in range(len(string)):
    if(string[i] >= 'a' and string[i] <= 'z'):
        string1 = string1 + chr((ord(string[i]) - 32))
    else:
        string1 = string1 + string[i]
 
print("\nOriginal String in Lowercase  =  ", string)
print("The Given String in Uppercase =  ", string1)

#############################################################

print("""
*********************************************
* Example 3 : Using while Loop   (Uppercase)    					 	
*********************************************
""")

string = input("Please Enter your Own String : ")
string1 = ''
i = 0

while(i < len(string)): if(string[i] >= 'a' and string[i] <= 'z'):
        string1 = string1 + chr((ord(string[i]) - 32))
    else:
        string1 = string1 + string[i]
    i = i + 1
 
print("\nOriginal String in Lowercase  =  ", string)
print("The Given String in Uppercase =  ", string1)

#############################################################

print("""
*********************************************
* Example 4 : Using for  Loop  (Lowercase)     					 	
*********************************************
""")

string = input("Please Enter your Own String : ")
string1 = ''

for i in string:
    if(i >= 'a' and i <= 'z'):
        string1 = string1 + chr((ord(i) - 32))
    else:
        string1 = string1 + i
 
print("\nOriginal String in Lowercase  =  ", string)
print("The Given String in Uppercase =  ", string1)

#############################################################

print("""
*********************************************
* Example 5 : Using for  Loop  (ASCII)     					 	
*********************************************
""")

string = input("Please Enter your Own String : ")
string1 = ''

for i in string:
    if(ord(i) >= 97 and ord(i) <= 122):
        string1 = string1 + chr((ord(i) - 32))
    else:
        string1 = string1 + i
 
print("\nOriginal String in Lowercase  =  ", string)
print("The Given String in Uppercase =  ", string1)

