#!/usr/bin/python3

#############################################################
#															#
# Python Program to find first Digit of Numbers			    #
# Created on : 4/29/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : Using while loop          					 	
*********************************************
""")

number = int(input("Please enter any Number: "))

first_digit = number

while(first_digit >= 10):
	first_digit = first_digit // 10
	
print("The first Digit from a given number {0} = {1}".format(number,first_digit))


print("""
*********************************************
* Example 2 : Using built in function          					 	
*********************************************
""")

import math

number = int(input("Please Enter any Number: "))

count = int(math.log10(number))

first_digit = number // math.pow(10,count)

print("Total number of Digit in a given Number {0} = {1}".format(number,count))
print("The first Digit from a given Number {0} = {1}".format(number,first_digit))


print("""
*********************************************
* Example 3 : Using UDF function          					 	
*********************************************
""")

def first_digit(number):
	while(number >= 10):
		number = number // 10
	return number

num = int(input("Please Enter any Number: "))

firstdigit = first_digit(num)

print("The first Digit from a given Number {0} = {1}".format(num,firstdigit))