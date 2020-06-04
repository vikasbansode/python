#!/usr/bin/python3

#############################################################
#															#
# Python Program to Convert string to Lowercase	            # 
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

string1 = string.lower()
 
print("\nOriginal String in Uppercase  =  ", string)
print("The Given String in Lowercase =  ", string1)

#############################################################

print("""
*********************************************
* Example 2 : USING FOR LOOP       					 	
*********************************************
""")

string = input("Please Enter your Own String : ")
string1 = ''

for i in range(len(string)):
    if(string[i] >= 'A' and string[i] <= 'Z'):
        string1 = string1 + chr((ord(string[i]) + 32))
    else:
        string1 = string1 + string[i]
 
print("\nOriginal String in Uppercase  =  ", string)
print("The Given String in Lowercase =  ", string1)

#############################################################

print("""
*********************************************
* Example 3 : USING WHILE LOOP       					 	
*********************************************
""")

string = input("Please Enter your Own String : ")
string1 = ''
i = 0

while(i < len(string)): if(string[i] >= 'A' and string[i] <= 'Z'):
        string1 = string1 + chr((ord(string[i]) + 32))
    else:
        string1 = string1 + string[i]
    i = i + 1
 
print("\nOriginal String in Uppercase  =  ", string)
print("The Given String in Lowercase =  ", string1)


#############################################################

print("""
*********************************************
* Example 4 : USING IF STATEMENT        					 	
*********************************************
""")

string = input("Please Enter your Own String : ")
string1 = ''

for i in string:
    if(i >= 'A' and i <= 'Z'):
        string1 = string1 + chr((ord(i) + 32))
    else:
        string1 = string1 + i
 
print("\nOriginal String in Uppercase  =  ", string)
print("The Given String in Lowercase =  ", string1)

#############################################################

print("""
*********************************************
* Example 5 : USING ASCII VALUE        					 	
*********************************************
""")

string = input("Please Enter your Own String : ")
string1 = ''

for i in string:
    if(ord(i) >= 65 and ord(i) <= 90):
        string1 = string1 + chr((ord(i) + 32))
    else:
        string1 = string1 + i
 
print("\nOriginal String in Uppercase  =  ", string)
print("The Given String in Lowercase =  ", string1)

