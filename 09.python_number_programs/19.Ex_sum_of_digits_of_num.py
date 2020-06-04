#!/usr/bin/python3

#############################################################
#															#
# Python Program to print sum of Digits in a Number			#
# Created on : 4/30/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : Using while Loop          					 	
*********************************************
""")

Number = int(input("Please Enter any Number: "))
Sum = 0

while(Number > 0):
    Reminder = Number % 10
    Sum = Sum + Reminder
    Number = Number //10

print("\n Sum of the digits of Given Number = %d" %Sum)

#############################################################

print("""
*********************************************
* Example 2 : Using Function           					 	
*********************************************
""")

def Sum_Of_Digits(Number):
    Sum = 0
    while(Number > 0):
        Reminder = Number % 10
        Sum = Sum + Reminder
        Number = Number //10
    return Sum

Number = int(input("Please Enter any Number: "))
Sum = Sum_Of_Digits(Number)
print("\n Sum of the digits of Given Number = %d" %Sum)

#############################################################

print("""
*********************************************
* Example 3 : Using Recursion Function           					 	
*********************************************
""")

Sum = 0
def Sum_Of_Digits(Number):
    global Sum
    if(Number > 0):
        Reminder = Number % 10
        Sum = Sum + Reminder
        Sum_Of_Digits(Number //10)
    return Sum

Number = int(input("Please Enter any Number: "))
Sum = Sum_Of_Digits(Number)
print("\n Sum of the digits of Given Number = %d" %Sum)





