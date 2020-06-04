#!/usr/bin/python3

#############################################################
#															#
# Python Program to find ASCII Value of Total Character    # 
# Special Character											#
# Created on : 05/01/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : using for Loop        					 	
*********************************************
""")

str1 = input("Please enter your own string : ")

for i in range(len(str1)):
	print("The ASCII Value of Character %c = %d" %(str1[i],ord(str1[i])))

#############################################################

print("""
*********************************************
* Example 2 : using while Loop        					 	
*********************************************
""")

str1 = input("Please Enter your Own String: ")
i = 0
while(i < len(str1)):
	print("The ASCII value of Character %c = %d" %(str1[i],ord(str1[i])))
	i = i + 1