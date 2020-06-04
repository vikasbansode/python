#!/usr/bin/python3

#############################################################
#															#
# Python Program to Remove last Occurance of char in string # 
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

string2 = ''
length = len(string)

for i in range(length):
    if(string[i] == char):
        string2 = string[0:i] + string[i + 1:length]
 
print("Original String :  ", string)
print("Final String :     ", string2)


#############################################################

print("""
*********************************************
* Example 2 : USING WHILE LOOP     					 	
*********************************************
""")

string = input("Please enter your own String : ")
char = input("Please enter your own Character : ")

string2 = ''
length = len(string)
i = 0

while(i < length):
    if(string[i] == char):
        string2 = string[0 : i] + string[i + 1 : length]
    i = i + 1
 
print("Original String :  ", string)
print("Final String :     ", string2)


#############################################################

print("""
*********************************************
* Example 3 : USING FUNCTION      					 	
*********************************************
""")

def removeLastOccur(string, char):
    string2 = ''
    length = len(string)
    i = 0

    while(i < length):
        if(string[i] == char):
            string2 = string[0 : i] + string[i + 1 : length]
        i = i + 1
    return string2
 
str1 = input("Please enter your own String : ")
char = input("Please enter your own Character : ")

print("Original String :  ", str1)
print("Final String :     ", removeLastOccur(str1, char))