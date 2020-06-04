#!/usr/bin/python3

######################################################################
#															         #
# Python Program to HOLLOW BOX PATTERN of NUMBER 1 and 0		 	 # 
# Special Character											         #
# Created on : 05/03/2020									         #
# Author     : Vikas Bansode								         #
#															         #
######################################################################

print("""
*********************************************
* Example 1 : USING FOR LOOP	 	
*********************************************
""")

rows = int(input("Please enter the total numbers of rows: "))
columns = int(input("Please enter the total number of columns: "))

print("Hollow Box pattern of Numbers")
print()
for i in range(1,rows + 1):
	for j in range(1, columns + 1):
		if (i == 1 or i == rows or j == 1 or j == columns):
			print('1',end=' ')
		else:
			print(' ',end= ' ')
	print()

######################################################################

print("""
*********************************************
* Example 2 : USING WHILE LOOP	 	
*********************************************
""")

rows = int(input("Please Enter the total Number of Rows  : "))
columns = int(input("Please Enter the total Number of Columns  : "))

print("Hollow Box Pattern of Numbers") 
print()
i = 1 
while(i <= rows):
    j = 1;
    while(j <= columns ):
        if(i == 1 or i == rows or j == 1 or j == columns):          
            print('1', end = '  ')
        else:
            print(' ', end = '  ')
        j = j + 1
    i = i + 1
    print()
	

######################################################################

print("""
*********************************************
* Example 3 : USING FOR LOOP	 	
*********************************************
""")

rows = int(input("Please Enter the total Number of Rows  : "))
columns = int(input("Please Enter the total Number of Columns  : "))

print("Hollow Box Pattern of Numbers") 
print()
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        if(i == 1 or i == rows or j == 1 or j == columns):          
            print('0', end = '  ')
        else:
            print(' ', end = '  ')
    print()
	
######################################################################

print("""
*********************************************
* Example 4 : USING OTHER SYSMBOLS	 	
*********************************************
""")

rows = int(input("Please Enter the total Number of Rows  : "))
columns = int(input("Please Enter the total Number of Columns  : "))

print("Hollow Box Pattern of Numbers") 
print()
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        if(i == 1 or i == rows or j == 1 or j == columns):          
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
    print()
	


