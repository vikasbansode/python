#!/usr/bin/python3

#############################################################
#															#
# Python Program to PRINT EVEN NUMBERS IN A LIST			# 
# Special Character											#
# Created on : 05/02/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : USING FOR LOOP					 	
*********************************************
""")

NumList = []

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

print("\nEven Numbers in this List are : ")
for j in range(Number):
    if(NumList[j] % 2 == 0):
        print(NumList[j], end = '   ')
		


#############################################################

print("""
*********************************************
* Example 2 : USING WHILE LOOP					 	
*********************************************
""")


NumList = []
j = 0

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

print("\nEven Numbers in this List are : ")
while(j < Number):
    if(NumList[j] % 2 == 0):
        print(NumList[j], end = '   ')
    j = j + 1
	
#############################################################

print("""
*********************************************
* Example 3 : USING FUNCTION					 	
*********************************************
""")

def even_numbers(NumList):
    for j in range(Number):
        if(NumList[j] % 2 == 0):
            print(NumList[j], end = '   ')

      
NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

print("\nEven Numbers in this List are : ")
even_numbers(NumList)

