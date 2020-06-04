#!/usr/bin/python3

#############################################################
#															#
# Python Program to check if number is Odd or even			#
# Created on : 4/28/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

number = int(input("Please enter the number : "))

if(number % 2 == 0):
	print("{0} is an Even number".format(number))
else:
	print("{0} is an Odd number".format(number))