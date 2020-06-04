#!/usr/bin/python3

#############################################################
#															#
# Python Program to Replace blank space with Hypen in string# 
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

str2 = str1.replace(' ', '_')

print("Original String :  ", str1)
print("Modified String :  ", str2)


#############################################################

print("""
*********************************************
* Example 2 : USING FOR LOOP     					 	
*********************************************
""")


str1 = input("Please Enter your Own String : ")

str2 = ''

for i in range(len(str1)):
    if(str1[i] == ' '):
        str2 = str2 + '_'
    else:
        str2 = str2 + str1[i]
        
print("Modified String :  ", str2)







