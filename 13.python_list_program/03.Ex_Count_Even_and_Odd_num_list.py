#!/usr/bin/python3

#############################################################
#															#
# Python Program to Count Even and Odd number in list       # 
# Special Character											#
# Created on : 05/02/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : USING FOR LOOP  					 	
*********************************************
""")

NumList = []
Even_count = 0
Odd_count = 0

Number = int(input("Please enter the Total Number Of List Elements: "))
for i in range(1,Number + 1):
	value = int(input("Please enter the value of %d Element : " %i))
	NumList.append(value)
	
for j in range(Number):
	if(NumList[j] % 2 == 0):
		Even_count = Even_count + 1
	else:
		Odd_count = Odd_count + 1

print("\nTotal Number of Even Numbers in this List = ", Even_count)
print("Total Number of Odd Numbers in this List = ", Odd_count)

#############################################################

print("""
*********************************************
* Example 2 : USING WHILE LOOP  					 	
*********************************************
""")

NumList = []
Even_count = 0
Odd_count = 0
j = 0

Number = int(input("Please enter the Total Number Of List Elements: "))
for i in range(1,Number + 1):
	value = int(input("Please enter the value of %d Element : " %i))
	NumList.append(value)
	
while(j < Number):
	if(NumList[j] % 2 == 0):
		Even_count = Even_count + 1
	else:
		Odd_count = Odd_count + 1
	j = j + 1

print("\nTotal Number of Even Numbers in this List = ", Even_count)
print("Total Number of Odd Numbers in this list = ", Odd_count)

#############################################################

print("""
*********************************************
* Example 3 : USING FUNCTION  					 	
*********************************************
""")

def count_even(NumList):
	Even_count=0
	for j in range(Number):
		if(NumList[j] % 2 == 0):
			Even_count = Even_count + 1
	return Even_count
	
def count_odd(NumList):
	Odd_count = 0
	for j in range(Number):
		if(NumList[j] % 2 != 0):
			Odd_count = Odd_count + 1
	return Odd_count

NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1,Number + 1):
	value = int(input("Please enter the value of %d Element: " %i))
	NumList.append(value)

even_cnt = count_even(NumList)
odd_cnt = count_odd(NumList)

print("\nTotal Number of Even Numbers in this List = ", even_cnt)
print("Total Number of Odd Numbers in this List = ", odd_cnt)


	


