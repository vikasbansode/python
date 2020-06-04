#!/usr/bin/python3

#############################################################
#															#
# Python Program to find factors of a Numbers			    #
# Created on : 4/29/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################


print("""
*********************************************
* Example 1 : Using while Loop          					 	
*********************************************
""")

number = int(input("Please enter any number : "))
value = 1

print("Factors of a given Number {0} are : ".format(number))

while(value <= number):
	if(number % value == 0 ):
		print("{0}".format(value))
	value = value + 1
	

#############################################################

print("""
*********************************************
* Example 2 : Using for Loop          					 	
*********************************************
""")
	
number = int(input("Please Enter any Number: "))

print("Factors of a Given Number {0} are:".format(number))

for value in range(1, number + 1):
    if(number % value == 0):
        print("{0}".format(value))
		
#############################################################

print("""
*********************************************
* Example 3 : Using function          					 	
*********************************************
""")

def Find_Factors(number):
    for value in range(1, number + 1):
        if(number % value == 0):
            print("{0}".format(value))

num = int(input("Please Enter any Number: "))

print("Factors of a Given Number {0} are:".format(num))
Find_Factors(num)



