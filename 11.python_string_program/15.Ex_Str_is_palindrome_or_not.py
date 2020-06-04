#!/usr/bin/python3

#############################################################
#															#
# Python Program to check given string Palindrome or not    # 
# Special Character											#
# Created on : 05/01/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : USING If Else statement      					 	
*********************************************
""")

string = input("Please enter your own String : ")

if(string == string[:: - 1]):
   print("This is a Palindrome String")
else:
   print("This is Not a Palindrome String")
   
  
#############################################################

print("""
*********************************************
* Example 2 : USING FOR LOOP      					 	
*********************************************
""")

string = input("Please enter your own String : ")
str1 = ""

for i in string:
    str1 = i + str1  
print("String in reverse Order :  ", str1)

if(string == str1):
   print("This is a Palindrome String")
else:
   print("This is Not a Palindrome String")
   
   
#############################################################

print("""
*********************************************
* Example 3 : USING FUNCTION    					 	
*********************************************
""")

def reverse(str1):
    if(len(str1) == 0):
        return str1
    else:
        return reverse(str1[1 : ]) + str1[0]
    
string = input("Please enter your own String : ")
str1 = reverse(string)
print("String in reverse Order :  ", str1)

if(string == str1):
   print("This is a Palindrome String")
else:
   print("This is Not a Palindrome String")


#############################################################

print("""
*********************************************
* Example 4 : USING FOR LOOP    					 	
*********************************************
""")

string = input("Please enter your own String : ")
flag = 0

length = len(string)
for i in range(length):
    if(string[i] != string[length - i - 1]):
        flag = 1
        break

if(flag == 0):
   print("This is a Palindrome String")
else:
   print("This is Not a Palindrome String")