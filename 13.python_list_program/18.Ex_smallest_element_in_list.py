#!/usr/bin/python3

######################################################################
#															         #
# Python Program to Smallest Element in the List         			 # 
# Special Character											         #
# Created on : 05/03/2020									         #
# Author     : Vikas Bansode								         #
#															         #
######################################################################

print("""
*********************************************
* Example 1 : USING LIST					 	
*********************************************
""")

a = [10,50,60,80,20,15]

print("The Smallest Element in this list is : " min(a))

######################################################################

print("""
*********************************************
* Example 2 : USING FOR LOOP					 	
*********************************************
""")

NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

print("The Smallest Element in this List is : ", min(NumList))

a = [10, 50, 60, 80, 20, 15]

######################################################################

print("""
*********************************************
* Example 3 : USING SORT FUNCTION 					 	
*********************************************
""")
a = [10, 50, 60, 80, 20, 15]
a.sort()
print("The Smallest Element in this List is : ", a[0])

######################################################################

print("""
*********************************************
* Example 4 : GETTING USER INPUT  					 	
*********************************************
""")

NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

NumList.sort()
print("The Smallest Element in this List is : ", NumList[0])

######################################################################

print("""
*********************************************
* Example 5 : GETTING USER INPUT  					 	
*********************************************
""")

NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

smallest = NumList[0]    
for j in range(1, Number):
    if(smallest > NumList[j]):
        smallest = NumList[j]
        position = j

print("The Smallest Element in this List is : ", smallest)
print("The Index position of the Smallest Element is : ", position)


