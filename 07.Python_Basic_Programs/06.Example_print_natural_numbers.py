#!/usr/bin/python3

#########################################################
#														#
# Python Program to Print Natural Numbers from 1 to N 	#
# using for loop 										#
# nested if statement									#
# Created on : 4/28/2020								#
# Author     : Vikas Bansode							#
#														#
#########################################################


print()
print("Example 1 : using for loop ")
number = int(input("Please Enter any number: "))

print("The list of Natural numbers from 1 to {0} are".format(number))

for i in range(1,number + 1):
	print(i,end=' ')
	
	
print()

# below code print natural numbers vertically
for i in range(1,number + 1):
	print(i)
	
	
print()
print("#########################################################")
print()
print("Example 2 : using while loop ")

number = int(input("Please enter any number : "))

i = 1

print("The list of natural numbers from 1 to {0} are".format(number))

while (i <= number):
	print(i,end =' ')
	i = i + 1
	
print()
print("#########################################################")
print()
print("Example 3 : within Range")

minimum = int(input("Please enter the minimum value: "))
maximum = int(input("Please enter the maximum value: "))

print("The list of natural numbers from {0} and {1} are".format(minimum,maximum))

for i in (range(minimum,maximum + 1)):
	print(i,end=' ')


print()
print("#########################################################")
print()
print("Example 3 : Natural Number Reverse Order")

number = int(input("Please enter the value: "))

i = number

print("The list of Natural numbers from {0} to 1 in reverse order : ".format(number))

while(i >= 1):
	print(i,end = ' ')
	i = i - 1
	
	
print()
print("#########################################################")
print()
print("Example 3 : Natural Number within Range")


maximum = int(input("Please enter the value : "))
minimum = int(input("Please enter the value : "))

print("The list of natural numbers from {0} to {1} are :".format(maximum,minimum))

while(maximum >=  minimum):
	print(maximum, end = ' ')
	maximum =  maximum - 1
	