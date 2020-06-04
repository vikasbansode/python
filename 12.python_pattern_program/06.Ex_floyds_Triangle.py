#!/usr/bin/python3

######################################################################
#															         #
# Python Program to Print Floyd's Triangle           			 	 # 
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

rows = int(input("Please Enter the total Number of Rows: "))
number = 1

print("Floyd's Triange")
for i in range(1,rows + 1):
	for j in range(1, i + 1):
		print(number,end= ' ')
		number = number + 1
	print()

######################################################################

print("""
*********************************************
* Example 2 : USING WHILE LOOP	 	
*********************************************
""")

rows = int(input("Please enter the total number of Rows: "))
number = 1

print("Floyd's Triangle")
i = 1
while(i <= rows):
	j = 1
	while(j <= i):
		print(number,end= ' ')
		number = number + 1
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

print("Floyd's Triangle") 
for i in range(1, rows + 1):
    for j in range(1, i + 1):        
        print('* ', end = '  ')
    print()