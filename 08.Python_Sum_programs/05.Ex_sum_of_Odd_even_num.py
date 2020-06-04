#!/usr/bin/python3

#############################################################
#															#
# Python Program to calculate Even and  Odd numbers		    #
# Created on : 4/29/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : Using for Loop          					 	
*********************************************
""")

maximum = int(input(" Please Enter the Maximum Value : "))
even_total = 0
odd_total = 0
 
for number in range(1, maximum + 1):
    if(number % 2 == 0):
        even_total = even_total + number
    else:
        odd_total = odd_total + number
 
print("The Sum of Even Numbers from 1 to {0} = {1}".format(number, even_total))
print("The Sum of Odd Numbers from 1 to {0} = {1}".format(number, odd_total))

#############################################################

print("""
*********************************************
* Example 2 : Using minimum maximum           					 	
*********************************************
""")

minimum = int(input(" Please Enter the Minimum Value : ")) 
maximum = int(input(" Please Enter the Maximum Value : "))

even_total = 0
odd_total = 0
 
for number in range(minimum, maximum + 1):
    if(number % 2 == 0):
        even_total = even_total + number
    else:
        odd_total = odd_total + number
 
print("The Sum of Even Numbers from 1 to {0} = {1}".format(number, even_total))
print("The Sum of Odd Numbers from 1 to {0} = {1}".format(number, odd_total))