#!/usr/bin/python3

#############################################################
#															#
# Python Program to to find sum of natural numbers		 	#	
# 															#
# Created on : 4/29/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

# what is Natural Numbers?
# Natural numbers are a part of the number system which includes all the positive integers from 1 till infinity.
# It is an integer which is always greater than zero(0).

print("""
*********************************************
*	Example 1 : Using for Loop          					 	
*********************************************
""")

number = int(input("Please enter any Number: "))

total = 0
for value in range(1,number + 1):
	total = total + value

print("The sum of Natural Numbers from 1 to {0} = {1}".format(number,total))

#############################################################

print("""
*********************************************
*	Example 1 : Using while Loop        					 	
*********************************************
""")

number = int(input("Please enter any number: "))
total = 0
value = 1

while(value <= number):
	total = total + value
	value = value + 1
print("The sum of Natural Numbers from 1 to {0} = {1}".format(number,total))



#############################################################

print("""
*********************************************
*	Example 1 : Using function 	    					 	
*********************************************
""")


def sum_of_n_natural_numbers(num):
    if(num == 0):
        return num
    else:
        return (num + sum_of_n_natural_numbers(num - 1))
    
number = int(input("Please Enter any Number: "))

total_value = sum_of_n_natural_numbers(number)

print("Sum of Natural Numbers from 1 to {0} =  {1}".format(number, total_value))

