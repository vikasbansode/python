#!/usr/bin/python3

#############################################################
#															#
# Python Program to Count Alphabets,Digits adn Special Char # 
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

string = input("Please enter your own String :")
alphabets = digits = special = 0

for i in range(len(string)):
	if(string[i].isalpha()):
		alphabets = alphabets + 1
	elif(string[i].isdigit()):
		digits = digits + 1
	else:
		special = special + 1

print("\nTotal Number of Alphabets in this String : ", alphabets)
print("Total Number of Digits in this String: ", digits)
print("Total Number of Special Characters in this String: ",special)


#############################################################

print("""
*********************************************
* Example 2 : USING WHILE LOOP       					 	
*********************************************
""")

str1 = input("Please Enter your Own String : ")
alphabets = digits = special = 0

for i in range(len(str1)):
    if((str1[i] >= 'a' and str1[i] <= 'z') or (str1[i] >= 'A' and str1[i] <= 'Z')): 
        alphabets = alphabets + 1 
    elif(str1[i] >= '0' and str1[i] <= '9'):
        digits = digits + 1
    else:
        special = special + 1
        
print("\nTotal Number of Alphabets in this String :  ", alphabets)
print("Total Number of Digits in this String :  ", digits)
print("Total Number of Special Characters in this String :  ", special)

#############################################################

print("""
*********************************************
* Example 3 : USING STRING FUNCTION       					 	
*********************************************
""")

str1 = input("Please Enter your Own String : ")
alphabets = digits = special = 0

for i in range(len(str1)):
    if(ord(str1[i]) >= 48 and ord(str1[i]) <= 57): 
       digits = digits + 1 
    elif((ord(str1[i]) >= 65 and ord(str1[i]) <= 90) or (ord(str1[i]) >= 97 and ord(str1[i]) <= 122)):
        alphabets = alphabets + 1
    else:
        special = special + 1
        
print("\nTotal Number of Alphabets in this String :  ", alphabets)
print("Total Number of Digits in this String :  ", digits)
print("Total Number of Special Characters in this String :  ", special)



