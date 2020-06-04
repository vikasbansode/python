#!/usr/bin/python3

#############################################################
#															#
# Python Program to Replace Characters in string            # 
# Special Character											#
# Created on : 05/01/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : USING REPLACE BUILT IN FUNCTION     					 	
*********************************************
""")

str1 = input("Please Enter your Own String : ")
ch = input("Please Enter your Own Character : ")
newch = input("Please Enter the New Character : ")

str2 = str1.replace(ch, newch)

print("\nOriginal String :  ", str1)
print("Modified String :  ", str2)


#############################################################

print("""
*********************************************
* Example 2 : USING FOR LOOP     					 	
*********************************************
""")

str1 = input("Please Enter your Own String : ")
ch = input("Please Enter your Own Character : ")
newch = input("Please Enter the New Character : ")

str2 = ''
for i in range(len(str1)):
    if(str1[i] == ch):
        str2 = str2 + newch
    else:
        str2 = str2 + str1[i]

print("\nOriginal String :  ", str1)
print("Modified String :  ", str2)



