#!/usr/bin/python3

#############################################################
#															#
# Python Program to Count Positive and Negative num in list # 
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
Positive_count = 0
Negative_count = 0

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1,Number + 1):
	value = int(input("Please enter the value of %d Element : " %i))
	NumList.append(value)

for j in range(Number):
	if(NumList[j] >= 0):
		Positive_count = Positive_count + 1
		
	else:
		Negative_count = Negative_count + 1

print("\nTotal Number of Positive Numbers in this List = ",Positive_count)
print("Total Number of Negative Numbers in this list = ", Negative_count)

#############################################################

print("""
*********************************************
* Example 2 : USING WHILE LOOP  					 	
*********************************************
""")

NumList = []
Positive_count = 0
Negative_count = 0
j = 0

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1,Number + 1):
	value = int(input("Please enter the value of %d Element : " %i))
	NumList.append(value)
	
while(j < Number):
	if(NumList[j] >= 0):
		Positive_count = Positive_count + 1
	else:
		Negative_count = Negative_count + 1
	j = j + 1

print("\nTotal Number of Positive Numbers in this List = ",Positive_count)
print("Total Number of Negative Numbers in this list = ", Negative_count)


#############################################################

print("""
*********************************************
* Example 3 : USING FUNCTION  					 	
*********************************************
""")

def count_Positive(NumList):
	Positive_count = 0
	for j in range(Number):
		if(NumList[j] >= 0):
			Positive_count = Positive_count + 1
	return Positive_count

def count_Negative(NumList):
	Negative_count = 0
	for j in range(Number):
		if(NumList[j] % 2 !=0):
			Negative_count = Negative_count + 1
	return Negative_count
	
NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1,Number + 1):
	value = int(input("Please enter the value of %d Element: " %i))
	NumList.append(value)
	
Positive_cnt = count_Positive(NumList)
Negative_cnt = count_Negative(NumList)

print("\nTotal Number of Positive Numbers in this List = ", Positive_cnt)
print("Total Number of Negative Numbers in this List = ", Negative_cnt)


