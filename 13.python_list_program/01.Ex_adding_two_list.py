#!/usr/bin/python3

#############################################################
#															#
# Python Program to Add two listsn						    # 
# Special Character											#
# Created on : 05/02/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : USING FOR LOOP  					 	
*********************************************
""")

NumList1 = [10,20,30]
NumList2 = [15,25,35]
total = []

for j in range(3):
	total.append(NumList1[j] + NumList2[j])

print("\nThe total Sum of Two Lists = ", total)

#############################################################

print("""
*********************************************
* Example 2 : USING FOR LOOP  					 	
*********************************************
""")


NumList1 = []
NumList2 = []
total = []

Number = int(input("Please enter the Total Number of List Elements: "))
print("Please enter the Items of a First List   ")
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList1.append(value)

print("Please enter the Items of a Second List   ")
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList2.append(value)
    
for j in range(Number):
    total.append( NumList1[j] + NumList2[j])
 
print("\nThe total Sum of Two Lists =  ", total)

#############################################################

print("""
*********************************************
* Example 3 : USING FOR LOOP  					 	
*********************************************
""")

NumList1 = []
NumList2 = []
total = []

Number = int(input("Please enter the Total Number of List Elements: "))
print("Please enter the Items of a First and Second List   ")
for i in range(1, Number + 1):
    List1value = int(input("Please enter the %d Element of List1 : " %i))
    NumList1.append(List1value)

    List2value = int(input("Please enter the %d Element of List2 : " %i))
    NumList2.append(List2value)
    
for j in range(Number):
    total.append( NumList1[j] + NumList2[j])
 
print("\nThe total Sum of Two Lists =  ", total)

#############################################################

print("""
*********************************************
* Example 4 : USING WHILE LOOP  					 	
*********************************************
""")

NumList1 = []
NumList2 = []
total = []
i = 1
j = 0

Number = int(input("Please enter the Total Number of List Elements: "))
print("Please enter the Items of a First and Second List   ")
while(i <= Number):
    List1value = int(input("Please enter the %d Element of List1 : " %i))
    NumList1.append(List1value)

    List2value = int(input("Please enter the %d Element of List2 : " %i))
    NumList2.append(List2value)
    i = i + 1
    
while(j < Number):
    total.append( NumList1[j] + NumList2[j])
    j = j + 1
 
print("\nThe total Sum of Two Lists =  ", total)



