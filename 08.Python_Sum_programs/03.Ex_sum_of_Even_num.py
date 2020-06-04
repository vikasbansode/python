#!/usr/bin/python3

#############################################################
#															#
# Python Program to calculate sum of Even numbers		    #
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
total = 0

for number in range(1, maximum+1):
    if(number % 2 == 0):
        print("{0}".format(number))
        total = total + number

print("The Sum of Even Numbers from 1 to {0} = {1}".format(number, total))

#############################################################

print("""
*********************************************
* Example 2 : Using without if          					 	
*********************************************
""")

# Python Program to Calculate Sum of Even Numbers from 1 to N
 
maximum = int(input(" Please Enter the Maximum Value : "))
total = 0

for number in range(2, maximum + 1, 2):
    print("{0}".format(number))
    total = total + number

print("The Sum of Even Numbers from 1 to {0} = {1}".format(number, total))


#############################################################

print("""
*********************************************
* Example 3 : Using while loop          					 	
*********************************************
""")

maximum = int(input(" Please Enter the Maximum Value : "))
total = 0
number = 1
 
while number <= maximum:
    if(number % 2 == 0):
        print("{0}".format(number))
        total = total + number
    number = number + 1

print("The Sum of Even Numbers from 1 to N = {0}".format(total))


#############################################################

print("""
*********************************************
* Example 4 : Using minimum and Maximum          					 	
*********************************************
""")

minimum = int(input(" Please Enter the Minimum Value : "))
maximum = int(input(" Please Enter the Maximum Value : "))
total = 0

for number in range(minimum, maximum+1):
    if(number % 2 == 0):
        print("{0}".format(number))
        total = total + number

print("The Sum of Even Numbers from {0} to {1} = {2}".format(minimum, number, total))


