#!/usr/bin/python3

#############################################################
#															#
# Python Program to Arithmatic Operations on List		    # 
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
NumList2 = [5,2,3]
add=[]
sub=[]
multi=[]
div=[]
mod=[]
expo=[]

for j in range(3):
	add.append(NumList1[j] + NumList2[j])
	sub.append(NumList1[j] - NumList2[j])
	multi.append(NumList1[j] * NumList2[j])
	div.append(NumList1[j] / NumList2[j])
	mod.append(NumList1[j] % NumList2[j])
	expo.append(NumList1[j] ** NumList2[j])

print("\nThe List Items after Addition =  ", add)
print("The List Items after Subtraction =  ", sub)
print("The List Items after Multiplication =  ", multi)
print("The List Items after Division =  ", div)
print("The List Items after Modulus =  ", mod)
print("The List Items after Exponent =  ", expo)


#############################################################

print("""
*********************************************
* Example 2 : USING FOR LOOP (GETTING USER INPUT)  					 	
*********************************************
""")

NumList1 = []
NumList2 = []
add = [] 
sub = [] 
multi = []
div = []
mod = []
expo = []

Number = int(input("Please enter the Total Number of List Elements: "))
print("Please enter the Items of a First and Second List   ")
for i in range(1, Number + 1):
    List1value = int(input("Please enter the %d Element of List1 : " %i))
    NumList1.append(List1value)

    List2value = int(input("Please enter the %d Element of List2 : " %i))
    NumList2.append(List2value)
    
for j in range(Number):
    add.append( NumList1[j] + NumList2[j])
    sub.append( NumList1[j] - NumList2[j])
    multi.append( NumList1[j] * NumList2[j])
    div.append( NumList1[j] / NumList2[j])
    mod.append( NumList1[j] % NumList2[j])
    expo.append( NumList1[j] ** NumList2[j])
 
print("\nThe List Items after Addition =  ", add)
print("The List Items after Subtraction =  ", sub)
print("The List Items after Multiplication =  ", multi)
print("The List Items after Division =  ", div)
print("The List Items after Modulus =  ", mod)
print("The List Items after Exponent =  ", expo)

#############################################################

print("""
*********************************************
* Example 2 : USING WHILE LOOP (GETTING USER INPUT)  					 	
*********************************************
""")

NumList1 = []; NumList2 = []
add = [] ; sub = [] ; multi = []
div = []; mod = [] ; expo = []
i = 0
j = 0
Number = int(input("Please enter the Total Number of List Elements: "))
print("Please enter the Items of a First and Second List   ")
while(i < Number):
    List1value = int(input("Please enter the %d Element of List1 : " %i))
    NumList1.append(List1value)

    List2value = int(input("Please enter the %d Element of List2 : " %i))
    NumList2.append(List2value)
    i = i + 1
    
while(j < Number):
    add.append( NumList1[j] + NumList2[j])
    sub.append( NumList1[j] - NumList2[j])
    multi.append( NumList1[j] * NumList2[j])
    div.append( NumList1[j] / NumList2[j])
    mod.append( NumList1[j] % NumList2[j])
    expo.append( NumList1[j] ** NumList2[j])
    j = j + 1
 
print("\nThe List Items after Addition =  ", add)
print("The List Items after Subtraction =  ", sub)
print("The List Items after Multiplication =  ", multi)
print("The List Items after Division =  ", div)
print("The List Items after Modulus =  ", mod)
print("The List Items after Exponent =  ", expo)