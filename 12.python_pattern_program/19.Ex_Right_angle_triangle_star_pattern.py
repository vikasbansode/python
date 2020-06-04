#!/usr/bin/python3

######################################################################
#															         #
# Python Program to print Square number Pattern           		 	 # 
# 															         #
# Created on : 05/04/2020									         #
# Author     : Vikas Bansode								         #
#															         #
######################################################################

print("""
*********************************************
* Example 1 : USING FOR LOOP	 	
*********************************************
""")

num = int(input("Please enter number of rows: "))
print()
for i in range(1,num + 1):
	for j in range(1,i + 1):
		print("*",end="")
	print()

######################################################################

print("""
*********************************************
* Example 2 : USING WHILE LOOP	 	
*********************************************
""")

num = int(input("Please enter the number of rows: "))

i=0
while(i < num):
	j = i + 1
	while(j > 0):
		print("*",end="")
		j =  j - 1
	i=i+1
	print()


######################################################################

print("""
*********************************************
* Example 3 : USING FUNCTION (FOR LOOP) 	 	
*********************************************
""")
	
def star_triangle(num):
	for i in range(1,num + 1):
		for j in range(1, i + 1):
			print("*",end="")
		print()
		
num = int(input("Please enter the number of rows: "))
print()
star_triangle(num)



######################################################################

print("""
*********************************************
* Example 4 : USING FUNCTION (WHILELOOP) 	 	
*********************************************
""")
 
def while_triangle(num):
	i=0
	while(i < num):
		j=i + 1
		while(j > 0):
			print("*",end="")
			j = j - 1
		i=i+1
		print()
		
num=int(input("Please enter total number of rows : "))
print()
while_triangle(num)