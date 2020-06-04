#!/usr/bin/python3

######################################################################
#															         #
# Python Program to print Square number Pattern           		 	 # 
# 															         #
# Created on : 05/04/2020									         #
# Author     : Vikas Bansode								         #
#															         #
######################################################################

print("""
*********************************************
* Example 1 : USING FOR LOOP	 	
*********************************************
""")

side = int(input("Please Enter any side of a Square : "))

print("Square Number Pattern")

for i in range(side):
	for i in range(side):
		print('1',end=' ')
	print()
	
######################################################################

print("""
*********************************************
* Example 2 : USING WHILE LOOP	 	
*********************************************
""")	
	
side = int(input("Please Enter any Side of a Square  : "))
i = 0

print("Square Number Pattern") 

while(i < side):
    j = 0
    while(j < side):      
        j = j + 1
        print('5', end = '  ')
    i = i + 1
    print()
	
######################################################################

print("""
*********************************************
* Example 3 : USING FOR LOOP	 	
*********************************************
""")

side = int(input("Please Enter any Side of a Square  : "))
number = int(input("Please Enter any Number  : "))

print("Square Number Pattern") 

for i in range(side):
    for i in range(side):
        print(number, end = '  ')
    print()
	
