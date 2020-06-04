#!/usr/bin/python3

#############################################################
#															#
# Python Program to PRINT ELEMENTS IN A LIST				# 
# Special Character											#
# Created on : 05/02/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : USING PRINT FUNCTION					 	
*********************************************
""")

a = [10, 50, 60, 80, 20, 15]

print("Element in this List are : ")
print(a)

#############################################################

print("""
*********************************************
* Example 2 : USING FOR LOOP					 	
*********************************************
""")

a = [10, 50, 60, 80, 20, 15]

print("Element in this List are : ")
for i in range(len(a)):
    print("Element at Position %d = %d" %(i, a[i]))
	
#############################################################

print("""
*********************************************
* Example 3 : USING STRING LIST					 	
*********************************************
""")	
	
Fruits = ['Apple', 'Orange', 'Grape', 'Banana']

print("Element in this List are : ")
print(Fruits)

#############################################################

print("""
*********************************************
* Example 3 : USING FOR LOOP					 	
*********************************************
""")	

Fruits = ['Apple', 'Orange', 'Grape', 'Banana']

print("Element in this List are : ")
for fruit in Fruits:
    print(fruit)
	
#############################################################

print("""
*********************************************
* Example 4 : USING FOR LOOP					 	
*********************************************
""")

NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

for i in range(Number):
    print("The Element at index position %d = %d " %(i, NumList[i]))