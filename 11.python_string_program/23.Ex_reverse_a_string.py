#!/usr/bin/python3

#############################################################
#															#
# Python Program to Reverse a String					    # 
# Special Character											#
# Created on : 05/01/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : USING FOR LOOP     					 	
*********************************************
""")

string = input("Please enter your own String : ")

string2 = ''

for i in string:
    string2 = i + string2
    
print("\nThe Original String = ", string)
print("The Reversed String = ", string2)

#############################################################

print("""
*********************************************
* Example 2 : USING WHILE LOOP     					 	
*********************************************
""")

string = input("Please enter your own String : ")

string2 = ''
i = len(string) - 1

while(i >= 0):
    string2 = string2 + string[i]
    i = i - 1
    
print("\nThe Original String = ", string)
print("The Reversed String = ", string2))
print("The Given String in Lowercase =  ", string1)

#############################################################

print("""
*********************************************
* Example 3 : USING FUNCTION     					 	
*********************************************
""")

def StringReverse(str1):
    if(len(str1) == 0):
        return str1
    else:
        return StringReverse(str1[1:]) + str1[0]

string = input("Please enter your own String : ")

string2 = StringReverse(string)
print("\nThe Original String = ", string)
print("The Reversed String = ", string2)

#############################################################

print("""
*********************************************
* Example 3 : USING RECURSIVE FUNCTION     					 	
*********************************************
""")

def StringReverse(str1):
    str2 = str1[::-1]
    return str2

string = input("Please enter your own String : ")

string2 = StringReverse(string)
print("\nThe Original String = ", string)
print("The Reversed String = ", string2)