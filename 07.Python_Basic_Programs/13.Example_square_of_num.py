#!/usr/bin/python3

#############################################################
#															#
# Python Program to calculate square of a number 			#	
# using while loop											#
# Created on : 4/28/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

number = float(input("Please Enter any numeric value : "))
square = number * number
print("The square of a given Number {0} = {1}".format(number,square))

# you can use square ** 2 or
# you can write function as below

def square(num):
	return num * num

num = float(input("Please enter any numeric value: "))
sqre = square(num)

print("The square of a given Number {0} = {1}".format(num,sqre))