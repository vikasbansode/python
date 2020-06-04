#!/usr/bin/python3

#############################################################
#															#
# Python Program to Calculate Total Average and percentage 	#	
# 															#
# Created on : 4/29/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print()
print("example 1: using elif statement ")
print("=====================X=====================")
print()


english = float(input("Please enter English Marks: "))
math = float(input("Please enter Math score: "))
computers = float(input("Please enter Computer Marks: "))
physics = float(input("Please enter Physics Marks: "))
chemistry = float(input("Please enter Chemistry Marks: "))

total = english + math + computers + physics + chemistry
average = total / 5
percentage = (total / 500) * 100

print("\nTotal Marks = %.2f"  %total)
print("Average Marks = %.2f"  %average)
print("Marks Percentage = %.2f"  %percentage)