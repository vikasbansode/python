#!/usr/bin/python3

######################################################################
#															         #
# Python Program to Print Hollow square Star Pattern  		 	     # 
# 															         #
# Created on : 05/03/2020									         #
# Author     : Vikas Bansode								         #
#															         #
######################################################################

print("""
*********************************************
* Example 1 : USING FOR LOOP	 	
*********************************************
""")

side = int(input("Please Enter any Side of a Square  : "))

print("Hollow Square Star Pattern") 
print()
for i in range(side):
    for j in range(side):
        if(i == 0 or i == side - 1 or j == 0 or j == side - 1):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
    print()
	
######################################################################

print("""
*********************************************
* Example 2 : USER INPUT	 	
*********************************************
""")

side = int(input("Please Enter any Side of a Square  : "))
ch = input("Please Enter any Character  : ")

print("Hollow Square Star Pattern") 
for i in range(side):
    for j in range(side):
        if(i == 0 or i == side - 1 or j == 0 or j == side - 1):
            print('%c' %ch, end = '  ')
        else:
            print(' ', end = '  ')
    print()
	
######################################################################

print("""
*********************************************
* Example 3 : USING WHILE LOOP	 	
*********************************************
""")

side = int(input("Please Enter any Side of a Square  : "))

print("Hollow Square Star Pattern")
i = 0
while(i < side):
    j = 0
    while(j < side):
        if(i == 0 or i == side - 1 or j == 0 or j == side - 1):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
        j = j + 1
    i = i + 1
    print()
	

