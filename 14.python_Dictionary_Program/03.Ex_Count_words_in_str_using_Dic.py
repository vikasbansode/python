#!/usr/bin/python3

######################################################################
#															         #
# Python Program to Count words in a sring using Dictionary       	 # 
# Special Character											         #
# Created on : 05/03/2020									         #
# Author     : Vikas Bansode								         #
#															         #
######################################################################

print("""
*********************************************
* Example 1 : USING STRING			 	
*********************************************
""")


string = input("please enter any String: ")
words = []

words = string.split()
frequency = [words.count(i) for i in words]

myDict = dict(zip(words, frequency))
print("Dictionary Items : ", myDict)

######################################################################

print("""
*********************************************
* Example 2 : USING FOR LOOP			 	
*********************************************
""")

string = input("Please enter any String : ")
words = []

words = string.split() # or string.lower().split()
myDict = {}
for key in words:
    myDict[key] = words.count(key)

print("Dictionary Items  :  ",  myDict)

