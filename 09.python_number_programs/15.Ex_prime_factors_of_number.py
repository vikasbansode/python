#!/usr/bin/python3

#############################################################
#															#
# Python Program to print Prime factors Number 1 to N		#
# Created on : 4/30/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : Using for Loop          					 	
*********************************************
""")

Number = int(input(" Please Enter any Number: "))

for i in range(2, Number + 1):
    if(Number % i == 0):
        isprime = 1
        for j in range(2, (i //2 + 1)):
            if(i % j == 0):
                isprime = 0
                break
            
        if (isprime == 1):
            print(" %d is a Prime Factor of a Given Number %d" %(i, Number))
			
#############################################################

print("""
*********************************************
* Example 2 : Using while Loop          					 	
*********************************************
""")

Number = int(input(" Please Enter any Number: "))
i = 1

while(i <= Number):
    count = 0
    if(Number % i == 0):
        j = 1
        while(j <= i):
            if(i % j == 0):
                count = count + 1
            j = j + 1
            
        if (count == 2):
            print(" %d is a Prime Factor of a Given Number %d" %(i, Number))
    i = i + 1


