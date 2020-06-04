#!/usr/bin/python3

#############################################################
#															#
# Python Program to Remove Odd Characters in a string       # 
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

for i in range(1, len(str1) + 1):
    if(i % 2 == 0):
        str2 = str2 + str1[i - 1]
        
print("Original String :  ", str1)
print("Final String :     ", str2)

#############################################################

print("""
*********************************************
* Example 2 : USING WHILE LOOP     					 	
*********************************************
""")


str1 = input("Please Enter your Own String : ")

str2 = ''
i = 1
while(i <= len(str1)):
    if(i % 2 == 0):
        str2 = str2 + str1[i - 1]
    i = i + 1
        
print("Original String :  ", str1)
print("Final String :     ", str2)


#############################################################

print("""
*********************************************
* Example 2 : USING FUNCTION     					 	
*********************************************
""")

def RemoveOddCharString(str1):
    str2 = ''

    for i in range(1, len(str1) + 1):
        if(i % 2 == 0):
            str2 = str2 + str1[i - 1]
    return str2

string = input("Please Enter your Own String : ")       
print("Original String :  ", string)
print("Final String    :  ", RemoveOddCharString(string))