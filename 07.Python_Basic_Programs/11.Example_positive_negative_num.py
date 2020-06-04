#!/usr/bin/python3

#############################################################
#															#
# Python Program to print positive or Negative Numbers		#	
# using while loop											#
# Created on : 4/28/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

number = float(input("Please Enter any Numeric Value : "))

if(number > 0):
	print("{0} is a positive number".format(number))
elif(number < 0):
	print("{0} is a negative number".format(number))
else:
	print("You have entered Zero")