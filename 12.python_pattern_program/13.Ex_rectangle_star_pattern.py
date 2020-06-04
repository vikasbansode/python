#!/usr/bin/python3

######################################################################
#															         #
# Python Program to Rectangle Star Pattern						 	 # 
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

rows = int(input("Please enter the Totol Number of rows : "))
columns = int(input("Please enter the Total Number of Columns: "))

print("Rectangle Star Pattern")

for i in range(rows):
	for j in range(columns):
		print("*",end = ' ')
	print()

######################################################################

print("""
*********************************************
* Example 2 : USING FOR LOOP (GETTING USER INPUT)	 	
*********************************************
""")

rows = int(input("Please enter the total number of rows : "))
columns = int(input("Please enter the Total Number of Columns : "))
ch = input("Please enter any Character : ")

print("Rectangle Star Pattern")

for i in range(rows):
	for j in range(columns):
		print('%c' %ch, end = ' ')
	print()

######################################################################

print("""
*********************************************
* Example 3 : USING WHILE LOOP	 	
*********************************************
""")

rows = int(input("Please Enter the Total Number of Rows: "))
columns = int(input("Please enter the Total Number of columns : "))

print("Rectangle Star Pattern")
i = 0
while(i < rows):
	j = 0
	while(j < columns):
		print('*',end = ' ')
		j = j + 1
	i = i + 1
	print()

