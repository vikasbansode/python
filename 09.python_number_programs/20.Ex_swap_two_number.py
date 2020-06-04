#!/usr/bin/python3

#############################################################
#															#
# Python Program to Swap two numbers						#
# Created on : 4/30/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : Basic          					 	
*********************************************
""")

a = float(input(" Please Enter the First Value a: "))
b = float(input(" Please Enter the Second Value b: "))

print("Before Swapping two Number: a = {0} and b = {1}".format(a, b))

temp = a
a = b
b = temp

print("After Swapping two Number: a = {0} and b = {1}".format(a, b))

#############################################################

print("""
*********************************************
* Example 2 : Using Functions          					 	
*********************************************
""")

def swap_numbers(a, b):
    temp = a
    a = b
    b = temp
    
    print("After Swapping two Number: num1 = {0} and num2 = {1}".format(a, b))
 
num1 = float(input(" Please Enter the First Value : "))
num2 = float(input(" Please Enter the Second Value : "))

print("Before Swapping two Number: num1 = {0} and num2 = {1}".format(num1, num2))
swap_numbers(num1, num2)

#############################################################

print("""
*********************************************
* Example 3 : Using Arithmatic Operator          					 	
*********************************************
""")


a = float(input(" Please Enter the First Value a: "))
b = float(input(" Please Enter the Second Value b: "))

print("Before Swapping two Number: a = {0} and b = {1}".format(a, b))

a = a + b
b = a - b
a = a - b

print("After Swapping two Number: a = {0} and b = {1}".format(a, b))