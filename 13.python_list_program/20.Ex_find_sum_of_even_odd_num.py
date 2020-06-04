#!/usr/bin/python3

######################################################################
#															         #
# Python Program to Find sum of Even and Odd Numbers in a List		 # 
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
Even_Sum = 0
Odd_Sum = 0

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

for j in range(Number):
    if(NumList[j] % 2 == 0):
        Even_Sum = Even_Sum + NumList[j]
    else:
        Odd_Sum = Odd_Sum + NumList[j]

print("\nThe Sum of Even Numbers in this List =  ", Even_Sum)
print("The Sum of Odd Numbers in this List =  ", Odd_Sum)

######################################################################

print("""
*********************************************
* Example 2 : USING WHILE LOOP					 	
*********************************************
""")

NumList = []
Even_Sum = 0
Odd_Sum = 0
j = 0

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

while(j < Number):
    if(NumList[j] % 2 == 0):
        Even_Sum = Even_Sum + NumList[j]
    else:
        Odd_Sum = Odd_Sum + NumList[j]
    j = j+ 1

print("\nThe Sum of Even Numbers in this List =  ", Even_Sum)
print("The Sum of Odd Numbers in this List =  ", Odd_Sum)

######################################################################

print("""
*********************************************
* Example 3 : USING FUNCTION LOOP					 	
*********************************************
""")

def even_sum(NumList):
    Even_Sum = 0
    for j in range(Number):
        if(NumList[j] % 2 == 0):
            Even_Sum = Even_Sum + NumList[j]
    return Even_Sum

def odd_sum(NumList):
    Odd_Sum = 0
    for j in range(Number):
        if(NumList[j] % 2 != 0):
            Odd_Sum = Odd_Sum + NumList[j]
    return Odd_Sum

NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

Even_Sum = even_sum(NumList)
Odd_Sum = odd_sum(NumList)
print("\nThe Sum of Even Numbers in this List =  ", Even_Sum)
print("The Sum of Odd Numbers in this List =  ", Odd_Sum)

