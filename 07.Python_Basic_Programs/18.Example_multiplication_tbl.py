#!/usr/bin/python3

#############################################################
#															#
# Python Program to print multiplication table			 	#	
# Created on : 4/29/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print()
print("example 1 : using for loop")
print("=====================X=====================")
print()

print("Multiplication table")
print()
for i in range(8,10):
	for j in range(1,11):
		print("{0} * {1} = {2}".format(i,j,i*j))
	print("=====================================")

#############################################################

print()
print("example 2 : using for loop")
print("===================X=======================")
print()

num = int(input("Please enter any positive integer less than 10: "))

print("Multiplication Table")
print()
for i in range(num,10):
	for j in range(1,11):
		print("{0} * {1} = {2}".format(i,j,i*j))
	print("===========================")

#############################################################

print()
print("example 3 : using while loop")
print("===================X=======================")
print()

i = int(input("Please enter any positive integer less than 10: "))

print("Multiplication Talble")
print()

while(i <= 10):
	j = 1
	while(j <= 10):
		print('{0} * {1} = {2}'.format(i,j,i*j))
		j = j + 1
	print('===================')
	i = i + 1