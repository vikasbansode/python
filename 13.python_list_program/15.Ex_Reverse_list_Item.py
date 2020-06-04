#!/usr/bin/python3

######################################################################
#															         #
# Python Program to REVERSE LIST ITMES 								 # 
# Special Character											         #
# Created on : 05/03/2020									         #
# Author     : Vikas Bansode								         #
#															         #
######################################################################

print("""
*********************************************
* Example 1 : USING REVERSE FUNCTION					 	
*********************************************
""")

NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1,Number + 1):
	value = int(input("Please enter the value of %d Element: " %i))
	NumList.append(value)

NumList.reverse()
print("\nThe Result of a Reverse List = ", NumList)

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
	
j = Number - 1
i = 0

while(i < j):
    temp = NumList[i]
    NumList[i] = NumList[j]
    NumList[j] = temp
    i = i + 1
    j = j - 1
    
print("\nThe Result of a Reverse List =  ", NumList)


######################################################################

print("""
*********************************************
* Example 3 : USING FUNCTION					 	
*********************************************
""")	

def reverse_list(NumList, num):
    j = Number - 1
    i = 0
    while(i < j):
        temp = NumList[i]
        NumList[i] = NumList[j]
        NumList[j] = temp
        i = i + 1
        j = j - 1
    
NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)
    
reverse_list(NumList, Number)
print("\nThe Result of a Reverse List =  ", NumList)

######################################################################

print("""
*********************************************
* Example 4 : USING RECURSION FUNCTION					 	
*********************************************
""")

def reverse_list(NumList, i, j):
    if(i < j):
        temp = NumList[i]
        NumList[i] = NumList[j]
        NumList[j] = temp
        reverse_list(NumList, i + 1, j-1)
    
NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)
    
reverse_list(NumList, 0, Number - 1)
print("\nThe Result of a Reverse List =  ", NumList)


