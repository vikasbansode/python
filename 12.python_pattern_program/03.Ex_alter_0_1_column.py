#!/usr/bin/python3

#############################################################
#															#
# Python Program to Print 0 and 1 in alternative column     # 
# Special Character											#
# Created on : 05/01/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : USING FOR LOOP  					 	
*********************************************
""")

rows = int(input("Please Enter the total Number of Rows  : "))
columns = int(input("Please Enter the total Number of Columns  : "))

print("Print Number Pattern - 1 and 0 in alternative rows") 
 
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        if(i % 2 != 0):          
            print('1', end = '  ')
        else:
            print('0', end = '  ')
    print()

#############################################################

print("""
*********************************************
* Example 2 : USING WHILE LOOP  					 	
*********************************************
""")

rows = int(input("Please Enter the total Number of Rows  : "))
columns = int(input("Please Enter the total Number of Columns  : "))

print("Print Number Pattern - 1 and 0 in alternative rows") 
i = 1
while(i <= rows):
    j = 1
    while(j <= columns):
        if(i % 2 != 0):          
            print('1', end = '  ')
        else:
            print('0', end = '  ')
        j = j + 1
    i = i + 1
    print()
	
#############################################################

print("""
*********************************************
* Example 3 : USING WITHOUT IF  					 	
*********************************************
""")	
	
rows = int(input("Please Enter the total Number of Rows  : "))
columns = int(input("Please Enter the total Number of Columns  : "))

print("Print Number Pattern - 1 and 0 in alternative rows") 
 
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        print('%d' %(i % 2), end = '  ')
    print()
	
#############################################################

print("""
*********************************************
* Example 4 : USING FOR LOOP  					 	
*********************************************
""")

rows = int(input("Please Enter the total Number of Rows  : "))
columns = int(input("Please Enter the total Number of Columns  : "))

print("Print Number Pattern - 0 and 1 in alternative rows") 
 
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        if(i % 2 != 0):          
            print('0', end = '  ')
        else:
            print('1', end = '  ')
    print()
	
	


