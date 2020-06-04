#!/usr/bin/python3

#############################################################
#															#
# Python Program to calculate Profit and Loss				#	
# using while loop											#
# Created on : 4/28/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : Using If Statement          					 	
*********************************************
""")

actual_cost = float(input("Please enter the Actual product Price: "))
sale_amount = float(input("Please enter the sales Amount: "))

if(actual_cost > sale_amount):
	amount = actual_cost - sale_amount
	print("Total Loss Amount = {0}".format(amount))
elif(sale_amount > actual_cost):
	amount= sale_amount - actual_cost
	print("Total Profit = {0}".format(amount))
else:
	print("No profit No loss !!!")
	
	
#############################################################

print("""
*********************************************
* Example 2 : Using using minus         					 	
*********************************************
""")
	

actual_cost = float(input("Please enter the Actual product Price: "))
sale_amount = float(input("Please enter the sales Amount: "))

if(actual_cost - sale_amount > 0):
	amount = actual_cost - sale_amount
	print("Total Loss Amount = {0}".format(amount))
elif(sale_amount - actual_cost > 0):
	amount = sale_amount - actual_cost
	print("Total Profit = {0}".format(amount))
else:
	print("No profit No Loss!!!")