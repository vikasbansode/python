#!/usr/bin/python3

#############################################################
#															#
# Python Program to calculate sum of Odd numbers		    #
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
Oddtotal = 0

for number in range(1, maximum+1):
    if(number % 2 != 0):
        print("{0}".format(number))
        Oddtotal = Oddtotal + number

print("The Sum of Odd Numbers from 1 to {0} = {1}".format(number, Oddtotal))

#############################################################

print("""
*********************************************
* Example 2 : Using for Loop but without if         					 	
*********************************************
""")

# Python Program to Calculate Sum of Odd Numbers from 1 to N
 
maximum = int(input(" Please Enter the Maximum Value : "))
Oddtotal = 0

for number in range(1, maximum+1, 2):
    print("{0}".format(number))
    Oddtotal = Oddtotal + number

print("The Sum of Odd Numbers from 1 to {0} = {1}".format(number, Oddtotal))


#############################################################

print("""
*********************************************
* Example 3 : Using while loop        					 	
*********************************************
""")

maximum = int(input(" Please Enter the Maximum Value : "))
Oddtotal = 0
number = 1
 
while number <= maximum:
    if(number % 2 != 0):
        print("{0}".format(number))
        Oddtotal = Oddtotal + number
    number = number + 1

print("The Sum of Odd Numbers from 1 to {0} = {1}".format(maximum, Oddtotal))

#############################################################

print("""
*********************************************
* Example 4 : Using minimum maximum        					 	
*********************************************
""")

minimum = int(input(" Please Enter the Minimum Value : ")) 
maximum = int(input(" Please Enter the Maximum Value : "))
Oddtotal = 0

for number in range(minimum, maximum+1):
    if(number % 2 != 0):
        print("{0}".format(number))
        Oddtotal = Oddtotal + number

print("The Sum of Odd Numbers from {0} to {1} = {2}".format(minimum, maximum, Oddtotal))