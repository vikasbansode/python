#!/usr/bin/python3

#############################################################
#															#
# Python Program to Remove Odd Index char in a string       # 
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

str1 = input("Please Enter your Own String : ")

str2 = ''

for i in range(len(str1)):
    if(i % 2 == 0):
        str2 = str2 + str1[i]
        
print("Original String :  ", str1)
print("Final String :     ", str2)

#############################################################
print("""
*********************************************
* Example 1 : USING WHILE LOOP     					 	
*********************************************
""")

str1 = input("Please Enter your Own String : ")

str2 = ''
i = 0

while(i < len(str1)):
    if(i % 2 == 0):
        str2 = str2 + str1[i]
    i = i + 1
        
print("Original String :  ", str1)
print("Final String :     ", str2)

#############################################################
print("""
*********************************************
* Example 1 : USING FUNCTION     					 	
*********************************************
""")

def newString(str1):
    str2 = ''

    for i in range(len(str1)):
        if(i % 2 == 0):
            str2 = str2 + str1[i]
    return str2

string = input("Please Enter your Own String : ")       
print("Original String :  ", string)
print("Final String :     ", newString(string))