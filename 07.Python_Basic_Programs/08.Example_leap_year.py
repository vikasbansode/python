#!/usr/bin/python3

#############################################################
#															#
# Python Program to check leap year							#
# Created on : 4/28/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print()
print("Example 1 : using if condition ")

year = int(input("Please enter the year Number you wish: "))

if(( year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0 ))):
	print("%d is a leap year " %year)
else:
	print("%d is not a lear year " %year)
	
print()
print("#########################################################")
print()
print("Example 2 : using while loop ")

year = int(input("Please enter the year: "))

if(year % 400 == 0):
	print("%d is a leap year" %year)
elif(year % 100 == 0):
	print("%d is not a leap year" %year)
elif(year % 4 == 0):
	print("%d is a leap year" %year)
else:
	print("%d is not a the leap year" %year)