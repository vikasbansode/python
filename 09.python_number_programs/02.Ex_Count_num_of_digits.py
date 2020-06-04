#!/usr/bin/python3

#############################################################
#															#
# Python Program to count number of Digits in Number	    #
# Created on : 4/29/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : Using while Loop          					 	
*********************************************
""")

Number = int(input("Please Enter any Number: "))
Count = 0
while(Number > 0):
    Number = Number // 10
    Count = Count + 1

print("\n Number of Digits in a Given Number = %d" %Count)

#############################################################

print("""
*********************************************
* Example 2 : Using function           					 	
*********************************************
""")

def Counting(Number):
    Count = 0
    while(Number > 0):
        Number = Number // 10
        Count = Count + 1
    print("\n Number of Digits in a Given Number = %d" %Count)

Counting(1234)

#############################################################

print("""
*********************************************
* Example 3 : Using function     OR      					 	
*********************************************
""")


def Counting(Number):
    Count = 0
    while(Number > 0):
        Number = Number // 10
        Count = Count + 1
    return Count

Number = int(input("Please Enter any Number: "))
Count = Counting(Number)
print("\n Number of Digits in a Given Number = %d" %Count)


#############################################################

print("""
*********************************************
* Example 3 : Using Recursion function           					 	
*********************************************
""")

Count = 0
def Counting(Number):
    global Count
    if(Number > 0):
        Count = Count + 1
        Counting(Number//10)
    return Count

Number = int(input("Please Enter any Number: "))
Count = Counting(Number)
print("\n Number of Digits in a Given Number = %d" %Count)