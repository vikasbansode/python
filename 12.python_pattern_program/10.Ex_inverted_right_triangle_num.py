#!/usr/bin/python3

######################################################################
#															         #
# Python Program to INVERTEd RIGHT TRIANGLE NUMBERS 		 	     # 
# 															         #
# Created on : 05/03/2020									         #
# Author     : Vikas Bansode								         #
#															         #
######################################################################

print("""
*********************************************
* Example 1 : USING WHILE & FOR LOOP	 	
*********************************************
""")

rows = int(input("Please Enter the total Number of Rows  : "))

print("Inverted Right Triangle Pattern of Numbers") 
print()
i = rows
while(i >= 1):
    for j in range(1, i + 1):      
        print('%d ' %i, end = '  ')
    i = i - 1
    print()
	

######################################################################

print("""
*********************************************
* Example 1 : USING WHILE  LOOP	 	
*********************************************
""")

rows = int(input("Please Enter the total Number of Rows  : "))

print("Inverted Right Triangle Pattern of Numbers") 
i = rows
while(i >= 1):
    j = 1
    while(j <= i):      
        print('%d ' %i, end = '  ')
        j = j + 1
    i = i - 1
    print()