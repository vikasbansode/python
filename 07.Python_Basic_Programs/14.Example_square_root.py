#!/usr/bin/python3

#############################################################
#															#
# Python Program to calculate square root of a number 		#	
# using while loop											#
# Created on : 4/28/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("Example 1")
import math
number = int(input("Please enter any number value : "))
squareRoot = math.sqrt(number)
print("The square root of a given Number {0} = {1}".format(number,squareRoot))


#############################################################
print("Example 2")

import math
number = float(input("Please Enter any numeric Value : "))
squareRoot = math.pow(number, 0.5)
print("The Square Root of a Given Number {0}  = {1}".format(number, squareRoot))