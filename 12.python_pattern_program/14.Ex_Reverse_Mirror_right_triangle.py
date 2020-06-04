#!/usr/bin/python3

######################################################################
#															         #
# Python Program to Print Reverse Mirrored Right Triangle		 	 # 
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

rows = int(input("Please enter the Total Number of rows :"))

print("Reverse Mirrored Right Triangle Star Pattern")

for i in range(1,rows + 1):
	for j in range(1, rows + 1):
		if( j < i):
			print(' ', end=' ')
		else:
			print('*', end = ' ')
	print()
	
######################################################################

print("""
*********************************************
* Example 2 : USING FOR LOOP (GETTING USER INPUT)	 	
*********************************************
""")

rows = int(input("Please enter the Total Number of Rows : "))
ch = input("Please enter any Character : ")

print("Reverse Mirrored Right Triangle Star Pattern")
print()
for i in range(1,rows + 1):
	for j in range(1,rows + 1):
		if(j < i):
			print(' ',end = ' ')
		else:
			print('%c' %ch, end=' ')
	print()

######################################################################

print("""
*********************************************
* Example 3 : USING FOR LOOP (Adjust Print space you will get different pattern)	 	
*********************************************
""")

rows = int(input("Please enter the Total Number of Rows : "))
ch = input("Please enter any Character : ")

print("Reverse Mirrored Right Triangle Star Pattern")
print()
for i in range(1,rows + 1):
	for j in range(1,rows + 1):
		if(j < i):
			print('',end = ' ')
		else:
			print('%c' %ch, end=' ')
	print()
	
######################################################################

print("""
*********************************************
* Example 4 : USING WHILE LOOP	 	
*********************************************
""")
		
		
rows = int(input("Please enter the Total Number of Rows : "))

print("Reverse Mirrored Right Triangle Star Pattern")

i = 1
while(i <= rows):
	j = 1
	while(j <= rows):
		if(j < i):
			print(' ',end = ' ')
		else:
			print('*',end=' ')
		j = j + 1
	i = i + 1
	print()
	

