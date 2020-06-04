#!/usr/bin/python3

######################################################################
#															         #
# Python Program to print reverse Pyriamid Shape			         # 
# Created on : 05/04/2020									         #
# Author     : Vikas Bansode								         #
#															         #
######################################################################

print("""
*********************************************
* Example 1 : USING FOR LOOP	 	
*********************************************
""")

num = int(input("Enter the number of rows: "))
print()
for i in range(num,0,-1):
	for j in range(0,num - i):
		print(end=" ")
	for j in range(0,i):
		print("*",end=" ")
	print()