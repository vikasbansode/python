#!/usr/bin/python3

#########################################################
#														#
# python program to Calculate Cube of a Number			#
# Created on : 4/28/2020								#
# Author     : Vikas Bansode							#
#														#
#########################################################

print("Example 1 :")
number = float(input("Please enter any numeric value : "))

cube = number * number * number

print("The Cube of the given number {0} = {1}".format(number,cube))

print()
print("#########################################################")
print()
print("Example 2 :")


number = float(input(" Please Enter any numeric Value : "))

cube = number ** 3

print("The Cube of a Given Number {0}  = {1}".format(number, cube))

print()
print("#########################################################")
print()
print("Example 3 :")

def cube(num):
    return num * num * num

number = float(input(" Please Enter any numeric Value : "))

cub = cube(number)

print("The Cube of a Given Number {0}  = {1}".format(number, cub))