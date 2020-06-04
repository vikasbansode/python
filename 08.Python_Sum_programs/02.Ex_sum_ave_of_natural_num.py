#!/usr/bin/python3

#############################################################
#															#
# Python Program to to find sum of average of Natural       #
# numbers		 											#	
# 															#
# Created on : 4/29/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : Using for Loop          					 	
*********************************************
""")

number = int(input("Please enter any number: "))

total = 0

for value in range(1,number + 1):
	total = total + value

average = total / number

print("The sum of Natural Numbers from 1 to {0} = {1}".format(number,total))
print("Average of Natural Numbers from 1 to {0} = {1}".format(number,average))

#############################################################

print("""
*********************************************
* Example 2 : Using while Loop          					 	
*********************************************
""")

number = int(input("Please enter any number: "))

total = 0
value = 1

while (value <= number):
    total = total + value
    value = value + 1

average = total / number

print("The Sum of Natural Numbers from 1 to {0} =  {1}".format(number, total))
print("Average of Natural Numbers from 1 to {0} =  {1}".format(number, average))


#############################################################

print("""
*********************************************
* Example 3 : Using function & if statement          					 	
*********************************************
""")

def sum_and_avg_of_natural_numbers(num):
    if(num == 0):
        return num
    else:
        return (num * (num + 1) / 2)
    
number = int(input("Please Enter any Number: "))

total = sum_and_avg_of_natural_numbers(number)
average = total / number

print("The Sum of Natural Numbers from 1 to {0} =  {1}".format(number, total))
print("Average of Natural Numbers from 1 to {0} =  {1}".format(number, average))

#############################################################

print("""
*********************************************
* Example 4 : Using recurssion function           					 	
*********************************************
""")

# Python Program to find Sum and Average of N Natural Numbers

def sum_and_avg_of_natural_numbers(num):
    if(num == 0):
        return num
    else:
        return (num + sum_and_avg_of_natural_numbers(num - 1))
    
number = int(input("Please Enter any Number: "))

total = sum_and_avg_of_natural_numbers(number)
average = total / number

print("The Sum of Natural Numbers from 1 to {0} =  {1}".format(number, total))
print("Average of Natural Numbers from 1 to {0} =  {1}".format(number, average))