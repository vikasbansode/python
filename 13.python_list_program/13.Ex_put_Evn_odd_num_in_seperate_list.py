#!/usr/bin/python3

#############################################################
#															#
# Python Program to PUT EVEN and ODD Numbers in seperat list# 
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
Even = []
Odd = []

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1,Number + 1):
	value = int(input("Please enter the value of %d Element: " %i))
	NumList.append(value)

for j in range(Number):
	if(NumList[j] % 2 == 0):
		Even.append(NumList[j])
	else:
		Odd.append(NumList[j])
print()
print("Element in Even List is : ", Even)
print("Element in Odd List is : ", Odd)

#############################################################

print("""
*********************************************
* Example 2 : USING WHILE LOOP					 	
*********************************************
""")

NumList = []
Even = []
Odd = []
j = 0

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1,Number + 1):
	value = int(input("Please enter the value of %d Element: " %i))
	NumList.append(value)
	
while(j < Number):
	if(NumList[j] % 2 == 0):
		Even.append(NumList[j])
	else:
		Odd.append(NumList[j])
	j = j + 1

print("Element in Even list is : ", Even)
print("Element in Odd list is : ", Odd)

#############################################################

print("""
*********************************************
* Example 2 : USING FUNCTION LOOP					 	
*********************************************
""")


def even_numbers(NumList):
	Even=[]
	for j in range(Number):
		if(NumList[j] % 2 == 0):
			Even.append(NumList[j])
	print("Element in Even List is : ", Even)

def odd_numbers(NumList):
	Odd = []
	for j in range(Number):
		if(NumList[j] % 2 != 0):
			Odd.append(NumList[j])
	print("Element in Odd List is : ", Odd)
	
NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
	value = int(input("Please enter the value of %d Element: " %i))
	NumList.append(value)
	
even_numbers(NumList)
odd_numbers(NumList)
