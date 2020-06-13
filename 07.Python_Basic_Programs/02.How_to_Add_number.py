#!/bin/python3

#########################################################
#														#
# Python program to perform Arithmatic Operations		#
# Created on : 4/28/2020								#
# Author     : Vikas Bansode							#
#														#
#########################################################

print("Example 1")
print()

number1 = int(input("Please enter the first Number: "))
number2 = int(input("please Enter the second number: "))

# Using arithmetic + operater to add two numbers

sum = float(number1) + float(number2)
print('The sume of {0} and {1} is {2}'.format(number1,number2,sum))

print()
print("#########################################################")
print()
print("Example 2 :")

number1 = float(input("Please Enter the first Number: "))
number2 = float(input("Please Enter the second Number: "))

# Using Arithmetic + operator to add two numbers

sum = number1 +	number2
print('The sum of {0} and {1} is {2}'.format(number1,number2,sum))

print()
print("#########################################################")
print()

print("Example 3 :")

num1 = float(input("Please enter the First value number 1 : "))
num2 = float(input("pleaes Enter the first value number 2: "))

# Add two numbers

add = num1 + num2

# substracting num2 from num1
sub = num1 - num2

# Multiply num1 with num2
multi = num1 * num2

# Divide num1 by num2
div = num1 / num2

# Modulus of num1 and num2
mod = num1 % num2

# Exponent of num1 and num2
expo = num1 ** num2

print("The Sum of {0} and {1} = {2}".format(num1, num2, add))
print("The Subtraction of {0} from {1} = {2}".format(num2, num1, sub))
print("The Multiplication of {0} and {1} = {2}".format(num1, num2, multi))
print("The Division of {0} and {1} = {2}".format(num1, num2, div))
print("The Modulus of {0} and {1} = {2}".format(num1, num2, mod))
print("The Exponent Value of {0} and {1} = {2}".format(num1, num2, expo))

================================== Basic calculater=========
#!/bin/usr/python3

x = input("Eter your first number: ")
y = input("Enter your Second number: ")
z = input("please insert any add,minus,multiply,divide? (+,-,x,+): ")

y = int(y)
x = int(x)

if z != "":
	if z == "+":
		print("The sum of x and y",x + y)

	if z == "-":
		print("The substraction of x and y",x - y)

	if z == "x":
		print("The multiplication of x and y",x * y)

	if z == "/":
		print("The division of x and y",x / y)
else:
	print("use x,-,/,or + next time!")

