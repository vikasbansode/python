#!/usr/bin/python3

######################################################################
#															         #
# Python Program to Find sum of Elements in a List         			 # 
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

NumList = []

Number = int(input("Please enter the Total Number of List Elements : "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

total = sum(NumList)

print("\n The Sum of All Element in this List is : ", total)

######################################################################

print("""
*********************************************
* Example 2 : USING FOR LOOP					 	
*********************************************
""")

NumList = []
total = 0

Number = int(input("Please enter the Total Number of List Elements : "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

for j in range(Number):
    total = total + NumList[j]

print("\n The Sum of All Element in this List is : ", total)

######################################################################

print("""
*********************************************
* Example 3 : USING FOR LOOP					 	
*********************************************
""")

NumList = []
total = 0
j = 0

Number = int(input("Please enter the Total Number of List Elements : "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

while(j < Number):
    total = total + NumList[j]
    j = j + 1
print("\n The Sum of All Element in this List is : ", total)


######################################################################

print("""
*********************************************
* Example 4 : USING WHILE LOOP					 	
*********************************************
""")

NumList = []
total = 0
j = 0

Number = int(input("Please enter the Total Number of List Elements : "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

while(j < Number):
    total = total + NumList[j]
    j = j + 1
print("\n The Sum of All Element in this List is : ", total)

######################################################################

print("""
*********************************************
* Example 5 : USING FUNCTION 					 	
*********************************************
""")

def sum_of_list(NumList):
    total = 0
    for j in range(Number):
        total = total + NumList[j]
    return total


NumList = []
Number = int(input("Please enter the Total Number of List Elements : "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

total = sum_of_list(NumList)
print("\n The Sum of All Element in this List is : ", total)


