#!/usr/bin/python3

######################################################################
#															         #
# Python Program to Print Mirrored Right Triangle Star Pattern	 	 # 
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

rows = int(input("Please Enter the Total Number of Rows  : "))

print("Mirrored Right Triangle Star Pattern")
print()
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if(j <= rows - i):
            print(' ', end = '  ')
        else:
            print('*', end = '  ')
    print()

######################################################################

print("""
*********************************************
* Example 2 : GETTING USER INPUT FOR CHARACTER 	
*********************************************
""")

rows = int(input("Please Enter the Total Number of Rows  : "))
ch = input("Please Enter any Character  : ")

print("Mirrored Right Triangle Star Pattern") 
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if(j <= rows - i):
            print(' ', end = '  ')
        else:
            print('%c' %ch, end = '  ')
    print()
	

######################################################################

print("""
*********************************************
* Example 3 : USING WHILE LOOP 	
*********************************************
""")

rows = int(input("Please Enter the Total Number of Rows  : "))

print("Mirrored Right Triangle Star Pattern")
print()
i = 1
while(i <= rows):
    j = 1
    while(j <= rows):
        if(j <= rows - i):
            print(' ', end = '  ')
        else:
            print('*', end = '  ')
        j = j + 1
    i = i + 1
    print()
	