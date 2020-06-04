#!/usr/bin/python3

#############################################################
#															#
# Python Program to calculate Sum and Average of Natural 	#	
# numbers												 	#
# using while loop											#
# Created on : 4/28/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print()
print("Example 1 : using for loop ")

number = int(input("Please enter any number: "))
total=0
for value in range(1,number + 1):
	total = total + value
average = total/number

print("The Sum of Natural Numbers from 1 to {0} =  {1}".format(number, total))
print("Average of Natural Numbers from 1 to {0} =  {1}".format(number, average))

print()
print("#########################################################")
print()
print("Example 2 : using while loop ")

number = int(input("Please enter any number: "))

total = 0
value = 1

while (value <= number):
	total = total + value
	value = value + 1
average = total / number

print("The sum of Natural Numbers from 1 to {0} = {1}".format(number,total))
print("Average of Natural Numbers from 1 to {0}  = {1}".format(number,average))

print()
print("#########################################################")
print()
print("Example 2 : using Recursive function ")

def sum_and_average_of_natural_numbers(num):
	if(num == 0):
		return num
	else:
		return (num + sum_and_average_of_natural_numbers(num - 1))

number = int(input("Please enter any number: "))
total = sum_and_average_of_natural_numbers(number)
average = total / number

print("The Sum of Natural Numbers from 1 to {0} =  {1}".format(number, total))
print("Average of Natural Numbers from 1 to {0} =  {1}".format(number, average))


