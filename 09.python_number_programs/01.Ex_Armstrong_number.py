#!/usr/bin/python3

#############################################################
#															#
# Python Program for Armstrong Number					    #
# Created on : 4/29/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

# A number is called Armstrong if it is equal to the sum of the cubes of its own digits.

print("""
*********************************************
* Example 1 : Using While Loop          					 	
*********************************************
""")

num = int(input("Enter a number: "))
sum = 0
temp = num

while temp > 0 :
	digit = temp % 10
	sum += digit ** 3
	temp //=10

if num == sum:
	print(num," is an Armstrong number")
else:
	print(num," is not an Armstrong number")

#############################################################

print("""
*********************************************
* Example 1 : Using While Loop          					 	
*********************************************
""")


Number = int(input("\nPlease Enter the Number to Check for Armstrong: "))

# Initializing Sum and Number of Digits
Sum = 0
Times = 0
           
# Calculating Number of individual digits
Temp = Number
while Temp > 0:
           Times = Times + 1
           Temp = Temp // 10

# Finding Armstrong Number
Temp = Number
while Temp > 0:
           Reminder = Temp % 10
           Sum = Sum + (Reminder ** Times)
           Temp //= 10
if Number == Sum:
           print("\n %d is Armstrong Number.\n" %Number)
else:
           print("\n %d is Not a Armstrong Number.\n" %Number)
		   
#############################################################

print("""
*********************************************
* Example 2 : Using for Loop          					 	
*********************************************
""")

Number = int(input("\nPlease Enter the Number to Check for Armstrong: "))

# Initializing Sum and Number of Digits
Sum = 0
Times = 0
           
# Calculating Number of individual digits
Temp = Number
while Temp > 0:
           Times = Times + 1
           Temp = Temp // 10

# Finding Armstrong Number
Temp = Number
for n in range(1, Temp + 1):
           Reminder = Temp % 10
           Sum = Sum + (Reminder ** Times)
           Temp //= 10

if Number == Sum:
           print("\n %d is Armstrong Number.\n" %Number)
else:
           print("\n %d is Not a Armstrong Number.\n" %Number)

#############################################################

print("""
*********************************************
* Example 3 : Using function           					 	
*********************************************
""")

def Armstrong_Number(Number):
           # Initializing Sum and Number of Digits
           Sum = 0
           Times = 0

           # Calculating Number of individual digits
           Temp = Number
           while Temp > 0:
                      Times = Times + 1
                      Temp = Temp // 10

           # Finding Armstrong Number
           Temp = Number
           for n in range(1, Temp + 1):
                      Reminder = Temp % 10
                      Sum = Sum + (Reminder ** Times)
                      Temp //= 10
           return Sum
#End of Function

#User Input
Number = int(input("\nPlease Enter the Number to Check for Armstrong: "))

if (Number == Armstrong_Number(Number)):
    print("\n %d is Armstrong Number.\n" %Number)
else:
    print("\n %d is Not a Armstrong Number.\n" %Number)
	
#############################################################

print("""
*********************************************
* Example 3 : Using recursion Function           					 	
*********************************************
""")

# Initializing Number of Digits
Sum = 0
Times = 0

# Calculating Number of individual digits
def Count_Of_Digits(Number):
           global Times
           if(Number > 0):
                      Times = Times + 1
                      Count_Of_Digits(Number // 10)
           return Times
#End of Count Of Digits Function

# Finding Armstrong Number
def Armstrong_Number(Number, Times):
           global Sum
           if(Number > 0):
                      Reminder = Number % 10
                      Sum = Sum + (Reminder ** Times)
                      Armstrong_Number(Number //10, Times)
           return Sum
#End of Armstrong Function

#User Input
Number = int(input("\nPlease Enter the Number to Check for Armstrong: "))

Times = Count_Of_Digits(Number)
Sum = Armstrong_Number(Number, Times)
if (Number == Sum):
    print("\n %d is Armstrong Number.\n" %Number)
else:
    print("\n %d is Not a Armstrong Number.\n" %Number)
	

#############################################################

print("""
*********************************************
* Example 4 : Using minimum maximum            					 	
*********************************************
""")

Minimum = int(input("Please Enter the Minimum Value: "))
Maximum = int(input("\nPlease Enter the Maximum Value: "))

for Number in range(Minimum, Maximum + 1):
           # Initializing Sum and Number of Digits
           Sum = 0
           Times = 0
           
           # Calculating Number of individual digits
           Temp = Number
           while Temp > 0:
                      Times = Times + 1
                      Temp = Temp // 10

           # Finding Armstrong Number
           Temp = Number
           while Temp > 0:
                      Reminder = Temp % 10
                      Sum = Sum + (Reminder ** Times)
                      Temp //= 10
           if Number == Sum:
                      print(Number)
	
#############################################################

print("""
*********************************************
* Example 5 : Using minimum maximum            					 	
*********************************************
""")


num = int(input("Please enter your value: "))

order = len(str(num))

sum = 0
temp = num

while temp > 0:
	digit = temp % 10
	sum += digit ** order
	temp //= 10

if num == sum:
	print(num,"is an Armstrong number")
else:
	print(num,"is not an Armstrong number")

	
