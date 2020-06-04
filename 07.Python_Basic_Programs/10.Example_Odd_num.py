#!/usr/bin/python3

#############################################################
#															#
# Python Program to print odd number from 1 to N 			#	
# using for loop											#
# Created on : 4/28/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print()
print("Example 1 : using for loop ")
print()
maximum = int(input("Please enter the value: "))

for number in range(1,maximum + 1):
	if(number % 2 != 0):
		print("{0}".format(number))
		
print()
print("#########################################################")
print()
print("Example 2 : using while loop ")

maximum = int(input("Please Enter the Maximum value : "))

number = 1

while(number <= maximum):
	if(number % 2 != 0):
		print("{0}".format(number))
	number = number + 1
	
print()
print("#########################################################")
print()
print("Example 3 : using for loop ")

minimum = int(input("Please enter your value : "))
maximum = int(input("please enter your value : "))

for number in range(minimum,maximum + 1):
	if(number % 2 != 0):
		print("{0}".format(number))
