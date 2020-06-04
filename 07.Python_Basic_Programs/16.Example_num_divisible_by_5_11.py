#!/usr/bin/python3

#############################################################
#															#
# Python Program to check if number is divisible by 5 & 11 	#	
# 															#
# Created on : 4/28/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

number = int(input("Please enter any positive Integer: "))

if ((number % 5 == 0) and (number % 11 == 0)):
	print("Given number {0} is Divisible by 5 and 11".format(number))
else:
	print("Given Number {0} is Not Divisible by 5 and 11".format(number))
