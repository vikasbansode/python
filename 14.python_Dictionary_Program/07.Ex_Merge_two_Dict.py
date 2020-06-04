#!/usr/bin/python3

######################################################################
#															         #
# Python Program to Merge two Dictionary			 				 # 
# Special Character											         #
# Created on : 05/03/2020									         #
# Author     : Vikas Bansode								         #
#															         #
######################################################################

print("""
*********************************************
* Example 1 : 			 	
*********************************************
""")

first_Dict = {1: 'apple', 2: 'Banana' , 3: 'Orange'}
second_Dict = { 4: 'Kiwi', 5: 'Mango'}
print("First Dictionary: ", first_Dict)
print("Second Dictionary: ", second_Dict)

# Concatenate Two Dictionaries in Python
first_Dict.update(second_Dict)
    
print("\nAfter Concatenating two Dictionaries : ")
print(first_Dict)

######################################################################

print("""
*********************************************
* Example 2 : 			 	
*********************************************
""")

first_Dict = {'a': 'apple', 'b': 'Banana' , 'o': 'Orange'}
second_Dict = { 'k': 'Kiwi', 'm': 'Mango'}
print("First Dictionary: ", first_Dict)
print("Second Dictionary: ", second_Dict)

# Concatenate Two Dictionaries in Python
print("\nAfter Concatenating two Dictionaries : ")
print(dict(first_Dict, **second_Dict))

######################################################################

print("""
*********************************************
* Example 2 : USING FUNCTION			 	
*********************************************
""")

def Merge_Dictionaries(first, second):
    result = {**first_Dict, **second_Dict}
    return result

first_Dict = {'a': 'apple', 'b': 'Banana' , 'o': 'Orange'}
second_Dict = { 'k': 'Kiwi', 'm': 'Mango'}
print("First Dictionary: ", first_Dict)
print("Second Dictionary: ", second_Dict)

# Concatenate Two Dictionaries in Python
third_Dict = Merge_Dictionaries(first_Dict, second_Dict)

print("\nAfter Concatenating two Dictionaries : ")
print(third_Dict)