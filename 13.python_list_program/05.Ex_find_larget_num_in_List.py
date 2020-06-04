#!/usr/bin/python3

#############################################################
#															#
# Python Program to Find Larget Number in a List			# 
# Special Character											#
# Created on : 05/02/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : USING MAX in bulit function  					 	
*********************************************
""")

a = [10,50,60,20,15]

print("The Larget Element in this List is : ", max(a))


#############################################################

print("""
*********************************************
* Example 2 : USING FOR LOOP (getting input)  					 	
*********************************************
""")

NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))

for i in range(1,Number + 1):
	value = int(input("Please enter the Value of %d Element: " %i))
	NumList.append(value)

print("The Larget Element in this list is: ", max(NumList))

#############################################################

print("""
*********************************************
* Example 3 : USING SORT FUNCTION  					 	
*********************************************
""")

a = [10,50,60,80,20,15]
a.sort()

print("The Larget Element in this List is : ", a[5])

#############################################################

print("""
*********************************************
* Example 4 : USING  FOR LOOP AND SORT FUNCTION  					 	
*********************************************
""")

NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))

for i in range(1,Number + 1):
	value = int(input("please enter the Value of %d Element: " %i))
	NumList.append(value)

NumList.sort()

print("The Larget Element in this List is : ", NumList[Number - 1])

#############################################################

print("""
*********************************************
* Example 5 : USING  FOR LOOP AND SORT,Reverse
*********************************************
""")

NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1,Number + 1):
	value = int(input("Please enter the value of %d Element: " %i))
	NumList.append(value)

NumList.sort()
NumList.reverse()

print("The Larget Element in this List is: ", NumList[0])

#############################################################

print("""
*********************************************
* Example 6 : USING  FOR LOOP AND SORT,Reverse
*********************************************
""")


NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

largest = NumList[0]    
for j in range(1, Number):
    if(largest < NumList[j]):
        largest = NumList[j]
        position = j

print("The Largest Element in this List is : ", largest)
print("The Index position of the Largest Element is : ", position)

