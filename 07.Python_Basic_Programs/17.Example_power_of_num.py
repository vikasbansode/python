#!/usr/bin/python3

#############################################################
#															#
# Python Program to find power of number				 	#	
# 															#
# Created on : 4/29/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("Example 1 : using for loop ")

number = int(input("please enter any positive Integer : "))
exponent = int(input("Pleae enter Exponent value : "))

power = 1

for i in range(1,exponent + 1):
	power = power * number

print("The result of {0} power {1} = {2}".format(number,exponent,power))

print()
print("#######################################################")
print()
print("example 2 : using while loop")

number = int(input("Please enter any Positive Integer:  "))
exponent = int(input("Please enter exponent value : "))

power = 1
i = 1

while (i <= exponent):
	power = power * number
	i = i + 1

print("The result of {0} power {1} = {2}".format(number,exponent,power))