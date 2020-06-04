#!/usr/bin/python3

#############################################################
#															#
# Python Program to find Prime Number						#
# Created on : 4/30/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : Using For Loop          					 	
*********************************************
""")

# What is Prime Number?
# Any Natural Number that is not divisible by any other number except 1 and itself called prime Number.

Number = int(input("Please Enter any Number: "))
count = 0

for i in range(2,(Number // 2 + 1)):
	if(Number % i == 0):
		count = count + 1
		break
if (count == 0 and Number != 1):
	print("%d is a Prime Number" %Number)
else:
	print("%d is not a Prime Number" %Number)

#############################################################

print("""
*********************************************
* Example 2 : Using While Loop          					 	
*********************************************
""")

Number = int(input(" Please Enter any Number: "))
count = 0
i = 2

while(i <= Number//2):
    if(Number % i == 0):
        count = count + 1
        break
    i = i + 1

if (count == 0 and Number != 1):
    print(" %d is a Prime Number" %Number)
else:
    print(" %d is not a Prime Number" %Number)

#############################################################

print("""
*********************************************
* Example 3 : Using Function          					 	
*********************************************
""")


def finding_factors(Number):
    count = 0

    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
    return count

Num = int(input(" Please Enter any Number: "))

cnt = finding_factors(Num)

if (cnt == 0 and Num != 1):
    print(" %d is a Prime Number" %Num)
else:
    print(" %d is not a Prime Number" %Num)
	

