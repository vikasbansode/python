#!/usr/bin/python3

######################################################################
#															         #
# Python Program to Right Triangled Star Pattern        		 	 # 
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

rows = int(input("Please Enter the Total Number of Rows :"))

print("Right Angled Triangle Star Pattern")

for i in range(1,rows + 1):
	for j in range(1, i + 1):
		print("*", end=' ')
	print()
	
	
######################################################################

print("""
*********************************************
* Example 2 : USING FOR LOOP(USER INPUT)	 	
*********************************************
""")	
	
rows = int(input("Please Enter the Total Number of Rows  : "))
ch = input("Please Enter any Character  : ")

print("Right Angled Triangle Star Pattern") 
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print('%c' %ch, end = '  ')
    print()
	
	
######################################################################

print("""
*********************************************
* Example 3 : USING WHILE LOOP	 	
*********************************************
""")	

rows = int(input("Please Enter the Total Number of Rows  : "))

print("Right Angled Triangle Star Pattern")
i = 1
while(i <= rows):
    j = 1
    while(j <= i):
        print('*', end = '  ')
        j = j + 1
    i = i + 1
    print()