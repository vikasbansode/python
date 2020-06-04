#!/usr/bin/python3

#############################################################
#															#
# Python Program to Strong Number 1 to N					#
# Created on : 4/30/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : Using while Loop          					 	
*********************************************
""")

import math

maximum = int(input(" Please Enter the Maximum Value: "))

for Number in range(1, maximum):
    Temp = Number
    Sum = 0
    while(Temp > 0):
        Reminder = Temp % 10
        Factorial = math.factorial(Reminder)
        Sum = Sum + Factorial
        Temp = Temp // 10
    
    if (Sum == Number):
        print(" %d is a Strong Number" %Number)
		
		
#############################################################

print("""
*********************************************
* Example 1 : Using factorial function          					 	
*********************************************
""")

import math

minimum = int(input(" Please Enter the Minimum Value: "))
maximum = int(input(" Please Enter the Maximum Value: "))

for Number in range(minimum, maximum):
    Temp = Number
    Sum = 0
    while(Temp > 0):
        Reminder = Temp % 10
        Factorial = math.factorial(Reminder)
        Sum = Sum + Factorial
        Temp = Temp // 10
    
    if (Sum == Number):
        print(" %d is a Strong Number" %Number)
