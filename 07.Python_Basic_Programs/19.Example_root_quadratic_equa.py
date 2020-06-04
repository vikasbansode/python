#!/usr/bin/python3

#############################################################
#															#
# Python Program to find root quadratic equation		 	#	
# Created on : 4/29/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print()
print("example 1 : using elif")
print("=====================X=====================")
print()

import math

a = int(input("Pleas enter a value of a of Quadratic Equation: "))
b = int(input("Pleas enter a value of b of Quadratic Equation: "))
c = int(input("Pleas enter a value of c of Quadratic Equation: "))

discriminant = (b * b) - (4 * a * c)

if(discriminant > 0):
	root1 = (-b + math.sqrt(discriminant) / (2*a))
	root2 = (-b - math.sqrt(discriminant) / (2*a))
	print("Two Equal and Real roots Exists : root1 = %.2f and root2 = %.2f" %(root1,root2))
elif(discriminant == 0):
    root1 = root2 = -b / (2 * a)
    print("Two Equal and Real Roots Exists: root1 = %.2f and root2 = %.2f" %(root1, root2))
elif(discriminant < 0):
    root1 = root2 = -b / (2 * a)
    imaginary = math.sqrt(-discriminant) / (2 * a)
    print("Two Distinct Complex Roots Exists: root1 = %.2f+%.2f and root2 = %.2f-%.2f" %(root1, imaginary, root2, imaginary))