#!/usr/bin/python3

#############################################################
#															#
# Python Program to first occurance of character in str     # 
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

string = input("Please enter your own String : ")
char = input("Please enter your own Character : ")

flag = 0
for i in range(len(string)):
    if(string[i] == char):
        flag = 1
        break

if(flag == 0):
    print("Sorry! We haven't found the Search Character in this string ")
else:
    print("The first Occurrence of ",char,"is Found at Position " , i + 1)
	
#############################################################

print("""
*********************************************
* Example 2 : USING WHILE LOOP       					 	
*********************************************
""")

string = input("Please enter your own String : ")
char = input("Please enter your own Character : ")
i = 0
flag = 0

while(i < len(string)):
    if(string[i] == char):
        flag = 1
        break
    i = i + 1

if(flag == 0):
    print("Sorry! We haven't found the Search Character in this string ")
else:
    print("The first Occurrence of ", char, " is Found at Position " , i + 1)
	

#############################################################

print("""
*********************************************
* Example 3 : USING FUNCTION       					 	
*********************************************
""")

def first_Occurrence(char, string):
    for i in range(len(string)):
        if(string[i] == char):
            return i
    return -1

str1 = input("Please enter your own String : ")
ch = input("Please enter your own Character : ")

flag =  first_Occurrence(ch, str1)
if(flag == -1):
    print("Sorry! We haven't found the Search Character in this string ")
else:
    print("The first Occurrence of ", ch, " is Found at Position " , flag + 1)