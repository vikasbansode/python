#!/usr/bin/python3

######################################################################
#															         #
# Python Program to Sort Elements in ascending order     			 # 
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

NumList = []

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

NumList.sort()

print("Element After Sorting List in Ascending Order is : ", NumList)

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

for i in range (Number):
    for j in range(i + 1, Number):
        if(NumList[i] > NumList[j]):
            temp = NumList[i]
            NumList[i] = NumList[j]
            NumList[j] = temp

print("Element After Sorting List in Ascending Order is : ", NumList)

######################################################################

print("""
*********************************************
* Example 3 : USING WHILE LOOP					 	
*********************************************
""")

NumList = []

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

i = 0
while(i < Number):
    j = i + 1
    while(j < Number):
        if(NumList[i] > NumList[j]):
            temp = NumList[i]
            NumList[i] = NumList[j]
            NumList[j] = temp
        j = j + 1
    i = i + 1

print("Element After Sorting List in Ascending Order is : ", NumList)

