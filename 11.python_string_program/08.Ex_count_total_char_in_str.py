#!/usr/bin/python3

#############################################################
#															#
# Python Program to Counting total Character in str  # 
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

str1 = input("Please Enter your Own String: ")
total = 0

for i in str1:
	total = total + 1
	

print("Total Number of Character in this string = ", total) 

print("""
*********************************************
* Example 1 : USING FOR LOOP  (LEN Function)     					 	
*********************************************
""")

str1 = input("Please Enter your Own String : ")
total = 0
 
for i in range(len(str1)):
    total = total + 1
 
print("Total Number of Characters in this String = ", total)