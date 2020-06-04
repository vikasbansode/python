#!/usr/bin/python3

#############################################################
#															#
# Python Program to Count total number of words in str      # 
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

str1 = input("Please Enter your Own String : ")
total = 1

for i in range(len(str1)):
    if(str1[i] == ' ' or str1 == '\n' or str1 == '\t'):
        total = total + 1

print("Total Number of Words in this String = ", total)

#############################################################

print("""
*********************************************
* Example 2 : USING WHILE LOOP       					 	
*********************************************
""")

str1 = input("Please Enter your Own String : ")
total = 1
i = 0

while(i < len(str1)):
    if(str1[i] == ' ' or str1 == '\n' or str1 == '\t'):
        total = total + 1
    i = i + 1

print("Total Number of Words in this String = ", total)


#############################################################

print("""
*********************************************
* Example 2 : USING UDF      					 	
*********************************************
""")

def Count_Total_Words(str1):
    total = 1
    for i in range(len(str1)):
        if(str1[i] == ' ' or str1 == '\n' or str1 == '\t'):
            total = total + 1
    return total


string = input("Please Enter your Own String : ")
leng = Count_Total_Words(string)
print("Total Number of Words in this String = ", leng)

