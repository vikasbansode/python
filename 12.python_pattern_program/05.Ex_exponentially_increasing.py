#!/usr/bin/python3

#############################################################
#															#
# Python Program to Exponentially Increasing Star pattern   # 
# Special Character											#
# Created on : 05/02/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : USING FOR LOOP  					 	
*********************************************
""")

import math

rows = int(input("Please Enter the total Number of Rows  : "))

print("Exponentially Increasing Stars") 
for i in range(rows + 1):
    for j in range(1, int(math.pow(2, i) + 1)):        
        print('*', end = '  ')
    print()


#############################################################

print("""
*********************************************
* Example 1 : USING WHILE LOOP  					 	
*********************************************
""")

import math

rows = int(input("Please Enter the total Number of Rows  : "))

print("Exponentially Increasing Stars") 
i = 0
while(i <= rows):
    j = 1
    while(j <= math.pow(2, i)):        
        print('*', end = '  ')
        j = j + 1
    i = i + 1
    print()
	
