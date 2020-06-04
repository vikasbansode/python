#!/usr/bin/python3

######################################################################
#															         #
# Python Program to Right Triangled Number Pattern      		 	 # 
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

rows = int(input("Please enter the total Number of rows : "))

print("Right Triangled Pattern of Numbers")

for i in range(1, rows + 1):
	for j in range(1, i + 1):
		print('%d' %i, end = ' ')
	print()

######################################################################

print("""
*********************************************
* Example 2 : USING WHILE LOOP	 	
*********************************************
""")

rows = int(input("Please Enter the total Number of Rows :"))

print("Right Triangle Pattern of Numbers")
i=1
while(i <= rows):
	j = 1
	while(j <= i):
		print('%d' %i, end=' ')
		j = j + 1
	i = i + 1
	print()
