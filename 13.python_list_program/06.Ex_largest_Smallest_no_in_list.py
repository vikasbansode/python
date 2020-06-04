#!/usr/bin/python3

#############################################################
#															#
# Python Program to Find Larget & Smallet Number in a List	# 
# Special Character											#
# Created on : 05/02/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : USING MIN MAX fUNCTION					 	
*********************************************
""")

NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1,Number + 1):
	value = int(input("Please enter the value of %d Element: "%i))
	NumList.append(value)
	
print("The smallest Element in this List is: ", min(NumList))
print("The largest Element in this list is : ", max(NumList))

#############################################################

print("""
*********************************************
* Example 2 : USING SORT fUNCTION					 	
*********************************************
""")

NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1,Number + 1):
	value = int(input("Please enter the value of %d Element: "%i))
	NumList.append(value)
	
NumList.sort()

print("The smallest Element in this List is: ", NumList[0])
print("The largest Element in this list is : ", NumList[Number - 1])

#############################################################

print("""
*********************************************
* Example 3 : USING FOR LOOP					 	
*********************************************
""")
NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

smallest = largest = NumList[0]

for j in range(1, Number):
	if(smallest > NumList[j]):
		smallest = NumList[j]
	min_Index = j
	if(largest < NumList[j]):
		largest = NumList[j]
	max_Index = j

print("The Smallest Element in this List is : ", smallest)
print("The Index position of Smallest Element in this List is: ", min_Index)
print("The Largest Element in this List is : ", largest)
print("The Index position of Largest Element in this List is: ", max_Index)
