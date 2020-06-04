#!/usr/bin/python3

#############################################################
#															#
# Python Program to Counting occurance of Character in str  # 
# Special Character											#
# Created on : 05/01/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : USING FOR LOOP       					 	
*********************************************
""")

string = input("Please enter your own String: ")
char = input("Please enter your own Character: ")

count = 0
for i in range(len(string)):
	if(string[i] == char):
		count =  count + 1

print("The Total Number of Times",char, " has Occured = ", count)

#############################################################

print("""
*********************************************
* Example 2 : USING WHILE LOOP       					 	
*********************************************
""")

string = input("Please enter your own String: ")
char = input("Please enter your own Character: ")
i = 0
count = 0

while(i < len(string)):
	if(string[i] == char):
		count = count + 1
	i = i + 1
print("The Total number of Times ", char, " has Occured = ", count)


#############################################################

print("""
*********************************************
* Example 3 : USING USER DEFINED FUNCTION       					 	
*********************************************
""")

def count_Occurrence(ch,str1):
	count = 0
	for i in range(len(string)):
		if(string[i] == char):
			count = count + 1
		return count

string = input("Please enter your own string: ")
char = input("Please enter your own character : ")

cnt = count_Occurrence(char,string)
print("The total number of Times", char," has Occured = ", cnt)

