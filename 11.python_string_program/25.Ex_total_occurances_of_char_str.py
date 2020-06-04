#!/usr/bin/python3

#############################################################
#															#
# Python Program to String Length    					    # 
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

str1 = input("Please enter your own String : ")
ch = input("Please enter your own Character : ")

for i in range(len(str1)):
    if(str1[i] == ch ):
        print(ch, " is Found at Position " , i + 1)

#############################################################

print("""
*********************************************
* Example 2 : USING WHILE LOOP  					 	
*********************************************
""")		


str1 = input("Please enter your own String : ")
ch = input("Please enter your own Character : ")
i = 0

while(i < len(str1)):
    if(str1[i] == ch ):
        print(ch, " is Found at Position " , i + 1)
    i = i + 1
	
#############################################################

print("""
*********************************************
* Example 3 : USING FUNCTION  					 	
*********************************************
""")	

def all_Occurrence(ch, str1):
    for i in range(len(str1)):
        if(str1[i] == ch ):
            print(ch, " is Found at Position " , i + 1)

string = input("Please enter your own String : ")
char = input("Please enter your own Character : ")
all_Occurrence(char, string)