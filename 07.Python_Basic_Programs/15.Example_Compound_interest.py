#!/usr/bin/python3

#############################################################
#															#
# Python Program to calculate compound interest		 		#	
# 															#
# Created on : 4/28/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

import math

princ_amount = float(input("Please enter the Principal Amount: "))
rate_of_int = float(input("Please enter the Rate of Interest: "))
time_period = float(input("Please enter time period in Years: "))

ci_future = princ_amount * (math.pow((1 + rate_of_int / 100),time_period))
compound_int = ci_future - princ_amount

print("Future Compound Interest for Principal Amount {0} = {1}".format(princ_amount,ci_future))
print("Compound interest for Principal Amount {0} = {1}".format(princ_amount,compound_int))
