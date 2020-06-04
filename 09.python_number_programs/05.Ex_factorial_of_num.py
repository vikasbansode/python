#!/usr/bin/python3

#############################################################
#															#
# Python Program to find factorial of Numbers			    #
# Created on : 4/29/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : Using in built math function          					 	
*********************************************
""")

import math 
number = int(input(" Please enter any Number to find factorial : "))

fact = math.factorial(number)
print("The factorial of %d  = %d" %(number, fact))


#############################################################

print("""
*********************************************
* Example 2 : Using for loop          					 	
*********************************************
""")

number = int(input(" Please enter any Number to find factorial : "))
fact = 1

for i in range(1, number + 1):
    fact = fact * i
print("The factorial of %d  = %d" %(number, fact))


#############################################################

print("""
*********************************************
* Example 3 : Using while loop          					 	
*********************************************
""")

number = int(input(" Please enter any Number to find factorial : "))
fact = 1
i = 1

while(i <= number):
    fact = fact * i
    i = i + 1

print("The factorial of %d  = %d" %(number, fact))

#############################################################

print("""
*********************************************
* Example 4 : Using UDF function           					 	
*********************************************
""")

def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    return fact

number = int(input(" Please enter any Number to find factorial : "))

facto = factorial(number)
print("The factorial of %d  = %d" %(number, facto))

def factorial(num):
    if((num == 0) or (num == 1)):
        return 1
    else:
        return num * factorial(num - 1)


#############################################################

print("""
*********************************************
* Example 5 : Using Recursion function           					 	
*********************************************
""")

number = int(input(" Please enter any Number to find factorial : "))

fact = factorial(number)
print("The factorial of %d  = %d" %(number, fact))

