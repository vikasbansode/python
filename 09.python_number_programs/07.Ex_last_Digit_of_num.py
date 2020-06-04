#!/usr/bin/python3

#############################################################
#															#
# Python Program to find Last Digit in Number			    #
# Created on : 4/30/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : Basic          					 	
*********************************************
""")

number = int(input("Please enter any Number: "))

last_digit = number % 10

print("The last Digit in a given Number %d = %d" %(number,last_digit))

#############################################################

print("""
*********************************************
* Example 2 : Using User Defined Function          					 	
*********************************************
""")

def lastDigit(num):
	return num % 10

number = int(input("Please enter any number: "))

last_digit = lastDigit(number)

print("The last Digit in a given Number %d = %d" %(number, last_digit))