#!/usr/bin/python3

#############################################################
#															#
# Python Program to PRINT NEGATIVE NUMBERS IN A LIST		# 
# Special Character											#
# Created on : 05/03/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : USING FOR LOOP					 	
*********************************************
""")

NumList = []
Number = int(input("Please enter the total number of list Elements: "))
for i in range(1,Number + 1):
	value = int(input("Please enter the value of %d Elements:" %i))
	NumList.append(value)

print("\nNegative Numbers in this list are : ")
for j in range(Number):
	if(NumList[j] < 0):
		print(NumList[j],end=' ')

#############################################################

print("""
*********************************************
* Example 2 : USING WHILE LOOP					 	
*********************************************
""")

NumList = []
j = 0
Number = int(input("Please enter the total number of List Elements: "))
for i in range(1,Number + 1):
	value = int(input("Please enter the value of %d Element : " %i))
	NumList.append(value)

print("\nNegative Numbers in this List are : ")
while(j < Number):
	if(NumList[j] < 0):
		print(NumList[j],end=' ')
	j = j + 1

#############################################################

print("""
*********************************************
* Example 3 : USING FUNCTION LOOP					 	
*********************************************
""")

def negative_number(NumList):
	for j in range(Number):
		if(NumList[j] < 0):
			print(NumList[j],end= ' ')

NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

print("\nNegative Numbers in this List are : ")
negative_number(NumList)

