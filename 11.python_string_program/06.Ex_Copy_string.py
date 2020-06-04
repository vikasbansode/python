#!/usr/bin/python3

#############################################################
#															#
# Python Program to Copy String					            # 
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

str1 = input("Please enter your own string: ")

str2 = str1
str3 = str1[:]

print("The Final String : str2 = ", str2)
print("The Final String : str3 = = ", str3)

#############################################################

print("""
*********************************************
* Example 2 : USING FOR LOOP       					 	
*********************************************
""")

str1 = input("Please enter Your Own String: ")
str2 = ''

for i in str1:
	str2 = str2 + i

print("The Final String : str2 = ", str2)

#############################################################

print("""
*********************************************
* Example 3 : USING FOR LOOP       					 	
*********************************************
""")


str1 = input("Please Enter Your Own String : ")
str2 = ''

for i in range(len(str1)):
    str2 = str2 + str1[i]
    
print("The Final String : Str2  = ", str2)
