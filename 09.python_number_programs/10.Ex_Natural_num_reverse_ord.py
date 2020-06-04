#!/usr/bin/python3

#############################################################
#															#
# Python Program to print Natural Numbers in Reverse order  #
# Created on : 4/30/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : Using While Loop          					 	
*********************************************
""")

number = int(input("Please enter any Number: "))

i = number

print("List of Natural Numbers from {0} to 1 in Reverse order: ".format(number))

while(i >= 1):
	print(i,end=' ')
	i = i - 1
	
print("""
*********************************************
* Example 2 : Using Min max number          					 	
*********************************************
""")

maximum = int(input("Please Enter the Maximum integer Value : "))
minimum = int(input("Please Enter the Minimum integer Value : "))

print("List of Natural Numbers from {0} to {1} : ".format(maximum, minimum)) 

while ( maximum >= minimum):
    print (maximum, end = '  ')
    maximum = maximum - 1
