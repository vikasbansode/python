#!/usr/bin/python3

#############################################################
#															#
# Python Program to  last occurance of character in str     # 
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

flag = -1
for i in range(len(string)):
    if(string[i] == char):
        flag = i

if(flag == -1):
    print("Sorry! We haven't found the Search Character in this string ")
else:
    print("The Last Occurrence of ", char, " is Found at Position " , flag + 1)

#############################################################

print("""
*********************************************
* Example 2 : USING WHILE LOOP       					 	
*********************************************
""")

string = input("Please enter your own String : ")
char = input("Please enter your own Character : ")
i = 0
flag = -1

while(i < len(string)):
    if(string[i] == char):
        flag = i
    i = i + 1

if(flag == -1):
    print("Sorry! We haven't found the Search Character in this string ")
else:
    print("The Last Occurrence of ", char, " is Found at Position " , flag + 1)
	

#############################################################

print("""
*********************************************
* Example 3 : USING FUNCTION       					 	
*********************************************
""")


def last_Occurrence(char, string):
    index = -1
    for i in range(len(string)):
        if(string[i] == char):
            index = i
    return index

str1 = input("Please enter your own String : ")
ch = input("Please enter your own Character : ")

flag = last_Occurrence(ch, str1)

if(flag == -1):
    print("Sorry! We haven't found the Search Character in this string ")
else:
    print("The Last Occurrence of ", ch, " is Found at Position " , flag + 1)