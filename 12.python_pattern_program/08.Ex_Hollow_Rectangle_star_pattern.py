#!/usr/bin/python3

######################################################################
#															         #
# Python Program to Print Hollow Rectangle Star Pattern  		 	 # 
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


rows = int(input("Please enter the Total Number of Rows: "))
columns = int(input("Please enter the total number of columns: "))

print("Hollow Rectangle Star Pattern")
print()
for i in range(rows):
	for j in range(columns):
		if(i == 0 or i == rows - 1 or j == 0 or j == columns -1):
			print("*",end=' ')
		else:
			print(' ',end=' ')
	print()

######################################################################

print("""
*********************************************
* Example 2 : USING FOR LOOP (Getting Difference CHaracter from User)	 	
*********************************************
""")

rows = int(input("Please Enter the Total Number of Rows  : "))
columns = int(input("Please Enter the Total Number of Columns  : "))
ch = input("Please Enter any Character  : ")

print("Hollow Rectangle Star Pattern") 
print()
for i in range(rows):
    for j in range(columns):
        if(i == 0 or i == rows - 1 or j == 0 or j == columns - 1):
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

rows = int(input("Please Enter the Total Number of Rows  : "))
columns = int(input("Please Enter the Total Number of Columns  : "))

print("Hollow Rectangle Star Pattern") 
print()
i = 0
while(i < rows):
    j = 0
    while(j < columns):
        if(i == 0 or i == rows - 1 or j == 0 or j == columns - 1):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
        j = j + 1
    i = i + 1
    print()


