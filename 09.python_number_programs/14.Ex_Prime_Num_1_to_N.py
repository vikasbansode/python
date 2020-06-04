#!/usr/bin/python3

#############################################################
#															#
# Python Program to print Prime Number 1 to N				#
# Created on : 4/30/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : Using for Loop          					 	
*********************************************
""")

for Number in range (1, 101):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')

#############################################################
		
print("""
*********************************************
* Example 2 : Using While Loop          					 	
*********************************************
""")

Number = 1

while(Number <= 100):
    count = 0
    i = 2
    
    while(i <= Number//2):
        if(Number % i == 0):
            count = count + 1
            break
        i = i + 1

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')
    Number = Number  + 1
	

#############################################################
print("""
*********************************************
* Example 3 : Using Minimum maximum          					 	
*********************************************
""")

minimum = int(input(" Please Enter the Minimum Value: "))
maximum = int(input(" Please Enter the Maximum Value: "))

for Number in range (minimum, maximum + 1):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')

#############################################################
print("""
*********************************************
* Example 4 : Using Minimum maximum          					 	
*********************************************
""")

minimum = int(input(" Please Enter the Minimum Value: "))
maximum = int(input(" Please Enter the Maximum Value: "))

Number = minimum

while(Number <= maximum):
    count = 0
    i = 2
    
    while(i <= Number//2):
        if(Number % i == 0):
            count = count + 1
            break
        i = i + 1

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')
    Number = Number  + 1
	
#############################################################
print("""
*********************************************
* Example 5 : Using SUm of Prime Number          					 	
*********************************************
""")

minimum = int(input(" Please Enter the Minimum Value: "))
maximum = int(input(" Please Enter the Maximum Value: "))
total = 0

for Number in range (minimum, maximum + 1):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')
        total = total + Number

print("\n\nSum of Prime Numbers from %d to %d = %d" %(minimum, maximum, total))

#############################################################
print("""
*********************************************
* Example 6 : Using SUm of Prime Number          					 	
*********************************************
""")

minimum = int(input(" Please Enter the Minimum Value: "))
maximum = int(input(" Please Enter the Maximum Value: "))
total = 0

Number = minimum

while(Number <= maximum):
    count = 0
    i = 2
    
    while(i <= Number//2):
        if(Number % i == 0):
            count = count + 1
            break
        i = i + 1

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')
        total = total + Number
    Number = Number  + 1
        
print("\n\nSum of Prime Numbers from %d to %d = %d" %(minimum, maximum, total))
