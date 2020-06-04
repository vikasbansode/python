#!/usr/bin/python3

######################################################################
#															         #
# Python Program to INVERTEd RIGHT TRIANGLE STAR PATTERN	 	     # 
# 															         #
# Created on : 05/03/2020									         #
# Author     : Vikas Bansode								         #
#															         #
######################################################################

print("""
*********************************************
* Example 1 : USING WHILE LOOP	 	
*********************************************
""")

rows = int(input("Please Enter the total Number of Rows  : "))
 
print("Inverted Right Angle Triangle of Stars") 
print()
i = rows
while(i > 0):
    j = i
    while(j > 0):      
        print('* ', end = '  ')
        j = j - 1
    i = i - 1
    print()
	
	
######################################################################

print("""
*********************************************
* Example 2 : GETTING USER INPUT OF CHARACTER 	 	
*********************************************
""")

rows = int(input("Please Enter the total Number of Rows  : "))
ch = input("Please Enter any Character  : ")
 
print("Inverted Right Angle Triangle of Stars") 
i = rows
while(i > 0):
    j = i
    while(j > 0):      
        print('%c' %ch, end = '  ')
        j = j - 1
    i = i - 1
    print()
