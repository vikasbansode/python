#!/usr/bin/python3

#############################################################
#															#
# Python Program to Perfect Number							#
# Created on : 4/30/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

# what is perfect Number?
# Perfect number is a positive integer that is equal to the sum of its proper divisors.
# e.g 6 -> is divisible by 1,2,3 & 6.  = 1+2+3+6 = 12 it is double of n hence it is perfect number.

print("""
*********************************************
* Example 1 : Using For Loop          					 	
*********************************************
""")

Number = int(input("Please Enter any Number: "))
sum = 0

for i in range(1,Number):
	if(Number % i == 0):
		sum = sum + i
if (sum == Number):
	print("%d is a Perfect Number" %Number)
else:
	print("%d is not a Perfect Number" %Number)
		
#############################################################
print("""
*********************************************
* Example 2 : Using while Loop          					 	
*********************************************
""")

Number = int(input(" Please Enter any Number: "))
i = 1
Sum = 0
while(i < Number):
    if(Number % i == 0):
        Sum = Sum + i
    i = i + 1
if (Sum == Number):
    print(" %d is a Perfect Number" %Number)
else:
    print(" %d is not the Perfect Number" %Number)

#############################################################
print("""
*********************************************
* Example 3 : Using Function          					 	
*********************************************
""")

def Perfect_Number(Number):
    Sum = 0
    for i in range(1, Number):
        if(Number % i == 0):
            Sum = Sum + i
    return Sum        

# Taking input from the user
Number = int(input("Please Enter any number: "))
if (Number == Perfect_Number(Number)):
    print("\n %d is a Perfect Number" %Number)
else:
    print("\n %d is not a Perfect Number" %Number)

#############################################################
print("""
*********************************************
* Example 4 : Pefect number between 1 to 1000          					 	
*********************************************
""")

Minimum = int(input("Please Enter any Minimum Value: "))
Maximum = int(input("Please Enter any Maximum Value: "))

# initialise sum


# Checking the Perfect Number
for Number in range(Minimum, Maximum - 1):
    Sum = 0
    for n in range(1, Number - 1):
        if(Number % n == 0):
            Sum = Sum + n       
    # display the result
    if(Sum == Number):
        print(" %d " %Number)
		
