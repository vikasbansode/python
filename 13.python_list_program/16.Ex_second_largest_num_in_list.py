#!/usr/bin/python3

######################################################################
#															         #
# Python Program to Find the second largest number in the list		 # 
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

NumList= []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
	value = int(input("Please enter the value of %d Element : " %i))
	NumList.append(value)
	
NumList.sort()

print("The Larget Element in this List is: ", NumList[Number - 2])

######################################################################

print("""
*********************************************
* Example 2 : USING WHILE LOOP					 	
*********************************************
""")

NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

NumList.sort()
NumList.reverse()
print("The Largest Element in this List is : ", NumList[1)

######################################################################

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

first = second = NumList[0]
for j in range(1, Number):
    if(NumList[j] > first):
        second = first
        first = NumList[j]
    elif(NumList[j] > second and NumList[j] < first):
        second = NumList[j]
        

print("The Largest Element in this List is : ", first)
print("The Second Largest Element in this List is : ", second)