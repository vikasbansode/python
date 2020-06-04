#!/usr/bin/python3

######################################################################
#															         #
# Python Program to print Pyriamid Shape			           		 # 
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
for i in range(0,num):
	for j in range(0,num - i - 1):
		print(end=" ")
	for j in range(0,i+1):
		print("*",end=" ")
	print()

######################################################################

print("""
*********************************************
* Example 2 : USING WHILE LOOP	 	
*********************************************
""")

num = int(input("enter the number of rows: "))
row=0
while row < num:
    space = num-row-1
    while space > 0:
        print(end=" ")
        space = space-1
    star = row+1
    while star > 0:
        print("*",end=" ")
        star = star - 1
    row = row + 1
    print()

######################################################################

print("""
*********************************************
* Example 3 : USING FUNCTION	 	
*********************************************
""")

def pyramid(rows):
	for i in range(rows):
		print(' '*(rows-i-1)+'*'*(2*i+1))

pyramid(5)