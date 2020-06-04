#!/usr/bin/python3

#############################################################
#															#
# Python Program to Strong Number   						#
# Created on : 4/30/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : Using while Loop          					 	
*********************************************
""")

# What is strong Number?
# Strong number is a Special number whose sum of factorial of digits is equal to the original number.
# e.g 145 is strong number since, 1! + 4! + 5! = 145

Number = int(input(" Please Enter any Number: "))
Sum = 0
Temp = Number

while(Temp > 0):
    Factorial = 1
    i = 1
    Reminder = Temp % 10

    while(i <= Reminder):
        Factorial = Factorial * i
        i = i + 1

    print("\n Factorial of %d = %d" %(Reminder, Factorial))
    Sum = Sum + Factorial
    Temp = Temp // 10

print("\n Sum of Factorials of a Given Number %d = %d" %(Number, Sum))
    
if (Sum == Number):
    print(" %d is a Strong Number" %Number)
else:
    print(" %d is not a Strong Number" %Number)
	
#############################################################

print("""
*********************************************
* Example 2 : Using for Loop          					 	
*********************************************
""")

Number = int(input(" Please Enter any Number: "))
Sum = 0
Temp = Number

while(Temp > 0):
    Factorial = 1
    Reminder = Temp % 10

    for i in range(1, Reminder + 1):
        Factorial = Factorial * i

    print("Factorial of %d = %d" %(Reminder, Factorial))
    Sum = Sum + Factorial
    Temp = Temp // 10

print("\n Sum of Factorials of a Given Number %d = %d" %(Number, Sum))
    
if (Sum == Number):
    print(" %d is a Strong Number" %Number)
else:
    print(" %d is not a Strong Number" %Number)
	
#############################################################

print("""
*********************************************
* Example 2 : Using factorial function         					 	
*********************************************
""")


import math 
Number = int(input(" Please Enter any Number: "))
Sum = 0
Temp = Number

while(Temp > 0):
    Reminder = Temp % 10
    Factorial = math.factorial(Reminder)

    print("Factorial of %d = %d" %(Reminder, Factorial))
    Sum = Sum + Factorial
    Temp = Temp // 10

print("\n Sum of Factorials of a Given Number %d = %d" %(Number, Sum))
    
if (Sum == Number):
    print(" %d is a Strong Number" %Number)
else:
    print(" %d is not a Strong Number" %Number)
	
