#!/usr/bin/python3

######################################################################
#															         #
# Python Program to PUT Positive and Negative Numbers in seperat list# 
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
Positive = []
Negative = []

Number = int(input("Please enter the Total Number of List Elements : "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

for j in range(Number):
    if(NumList[j] >= 0):
        Positive.append(NumList[j])
    else:
        Negative.append(NumList[j])

print("Element in Positive List is : ", Positive)
print("Element in Negative List is : ", Negative)

######################################################################

print("""
*********************************************
* Example 2 : USING WHILE LOOP					 	
*********************************************
""")

NumList = []
Positive = []
Negative = []
j = 0

Number = int(input("Please enter the Total Number of List Elements : "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

while(j < Number):
    if(NumList[j] >= 0):
        Positive.append(NumList[j])
    else:
        Negative.append(NumList[j])
    j = j + 1

print("Element in Positive List is : ", Positive)
print("Element in Negative List is : ", Negative)

######################################################################

print("""
*********************************************
* Example 3 : USING FUNCTION LOOP					 	
*********************************************
""")

def positive_numbers(NumList):
    Positive = []
    for j in range(Number):
        if(NumList[j] >= 0):
            Positive.append(NumList[j])
    print("Element in Positive List is : ", Positive)

def negative_numbers(NumList):
    Negative = []
    for j in range(Number):
        if(NumList[j] < 0):
            Negative.append(NumList[j])
    print("Element in Negative List is : ", Negative)
    
NumList = []
Positive = []
Negative = []
j = 0
Number = int(input("Please enter the Total Number of List Elements : "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

positive_numbers(NumList)
negative_numbers(NumList)





