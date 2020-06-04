#!/usr/bin/python3

#############################################################
#															#
# Python Program to Palindrome								#
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

reverse = 0
temp = number

while(temp > 0):
	Reminder = temp % 10
	reverse = (reverse * 10) + Reminder
	temp = temp // 10

print("Reverse of a given number is = %d" %reverse)

if(number == reverse):
	print("%d is a Palindrome Number" %number)
else:
	print("%d is not a Palindrome Number" %number)
	
#############################################################

print("""
*********************************************
* Example 2 : Using User Defined Function          					 	
*********************************************
""")

reverse = 0
def integer_reverse(number):
    global reverse
    
    if(number > 0):
        Reminder = number % 10
        reverse = (reverse * 10) + Reminder
        integer_reverse(number // 10)
    return reverse


number = int(input("Please Enter any Number: "))

rev = integer_reverse(number)
print("Reverse of a Given number is = %d" %rev)

if(number == rev):
    print("%d is a Palindrome Number" %number)
else:
    print("%d is not a Palindrome Number" %number)
	
#############################################################

print("""
*********************************************
* Example 2 : Using Recursive Function          					 	
*********************************************
""")

maximum = int(input(" Please Enter the Maximum Value : "))

print("Palindrome Numbers between 1 and %d are : " %maximum)
for num in range(1, maximum + 1):
    temp = num
    reverse = 0
    
    while(temp > 0):
        Reminder = temp % 10
        reverse = (reverse * 10) + Reminder
        temp = temp //10

    if(num == reverse):
        print("%d " %num, end = '  ')
		

#############################################################
	
print("""
*********************************************
* Example 3 : Palindrome numbers from 1 to 100          					 	
*********************************************
""")	

maximum = int(input(" Please Enter the Maximum Value : "))

print("Palindrome Numbers between 1 and %d are : " %maximum)
for num in range(1, maximum + 1):
    temp = num
    reverse = 0
    
    while(temp > 0):
        Reminder = temp % 10
        reverse = (reverse * 10) + Reminder
        temp = temp //10

    if(num == reverse):
        print("%d " %num, end = '  ')

#############################################################
	
print("""
*********************************************
* Example 4 : Palindrome numbers using function          					 	
*********************************************
""")

minimum = int(input(" Please Enter the Minimum Value : "))
maximum = int(input(" Please Enter the Maximum Value : "))

print("Palindrome Numbers between %d and %d are : " %(minimum, maximum))
for num in range(minimum, maximum + 1):
    temp = num
    reverse = 0
    
    while(temp > 0):
        Reminder = temp % 10
        reverse = (reverse * 10) + Reminder
        temp = temp //10

    if(num == reverse):
        print("%d " %num, end = '  ')


