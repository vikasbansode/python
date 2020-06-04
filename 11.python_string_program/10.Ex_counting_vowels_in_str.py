#!/usr/bin/python3

#############################################################
#															#
# Python Program to Count Vowel in a string                 # 
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


str1 = input("Please Enter Your Own String : ")
vowels = 0
 
for i in str1:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A'
       or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
 
print("Total Number of Vowels in this String = ", vowels)


#############################################################

print("""
*********************************************
* Example 2 : USING FOR LOOP       					 	
*********************************************
""")

str1 = input("Please Enter Your Own String : ")

vowels = 0
str1.lower()

for i in str1:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        vowels = vowels + 1
 
print("Total Number of Vowels in this String = ", vowels)


#############################################################

print("""
*********************************************
* Example 3 : USING FOR LOOP       					 	
*********************************************
""")

str1 = input("Please Enter Your Own String : ")
vowels = 0

for i in str1:
    if(ord(i) == 65 or ord(i) == 69 or ord(i) == 73
       or ord(i) == 79 or ord(i) == 85
       or ord(i) == 97 or ord(i) == 101 or ord(i) == 105
       or ord(i) == 111 or ord(i) == 117):
        vowels = vowels + 1
 
print("Total Number of Vowels in this String = ", vowels)