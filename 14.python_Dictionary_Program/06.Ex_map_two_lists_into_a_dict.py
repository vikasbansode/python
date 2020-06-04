#!/usr/bin/python3

######################################################################
#															         #
# Python Program to MAP two lists into a Dictionary 				 # 
# Special Character											         #
# Created on : 05/03/2020									         #
# Author     : Vikas Bansode								         #
#															         #
######################################################################

print("""
*********************************************
* Example 1 : USING FOR LOOP			 	
*********************************************
""")

keys = ['name','age','job']
values = ['John',25,'Developer']

myDict = {k:v for k, v in zip(keys,values)}
print("Dictionary Items : ", myDict)

######################################################################

print("""
*********************************************
* Example 1 : USING ZIP			 	
*********************************************
""")

keys = ['name', 'age', 'job']
values = ['John', 25, 'Developer']

myDict = dict(zip(keys, values))
print("Dictionary Items  :  ",  myDict)

######################################################################

print("""
*********************************************
* Example 1 : USING FOR LOOP			 	
*********************************************
""")

keys = []
values = []
num = int(input("Please enter the Number of elements for this Dictionary : "))
print("Integer Values for Keys")
for i in range(0, num):
    x = int(input("Enter Key " + str(i + 1) + " = "))
    keys.append(x)
    
print("Integer Values for Values")
for i in range(0, num):
    x = int(input("Enter Value " + str(i + 1) + " = "))
    values.append(x)
    
myDict = dict(zip(keys, values))
print("Dictionary Items  :  ",  myDict)
