#!/usr/bin/python3

#############################################################
#															#
# Python Program to reverse a Number						#
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
Reverse = 0
while(Number > 0):
    Reminder = Number % 10
    Reverse = (Reverse * 10) + Reminder
    Number = Number // 10

print("\n Reverse of entered number is = %d" %Reverse)

#############################################################

print("""
*********************************************
* Example 2 : Using Function          					 	
*********************************************
""")

def Reverse_Integer(Number):
    Reverse = 0
    while(Number > 0):
        Reminder = Number %10
        Reverse = (Reverse *10) + Reminder
        Number = Number //10
    return Reverse

Number = int(input("Please Enter any Number: "))
Reverse = Reverse_Integer(Number)
print("\n Reverse of entered number is = %d" %Reverse)

#############################################################

print("""
*********************************************
* Example 3 : Using Recursion          					 	
*********************************************
""")

Reverse = 0
def Reverse_Integer(Number):
    global Reverse
    if(Number > 0):
        Reminder = Number %10
        Reverse = (Reverse *10) + Reminder
        Reverse_Integer(Number //10)
    return Reverse

Number = int(input("Please Enter any Number: "))
Reverse = Reverse_Integer(Number)
print("\n Reverse of entered number is = %d" %Reverse)



