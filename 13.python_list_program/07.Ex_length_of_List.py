#!/usr/bin/python3

#############################################################
#															#
# Python Program to Length of a List						# 
# Special Character											#
# Created on : 05/02/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

print("""
*********************************************
* Example 1 : USING EMPTY LIST					 	
*********************************************
""")

emptyList = []
print("Length of a List =", len(emptyList))


#############################################################

print("""
*********************************************
* Example 2 : USING INTEGER LIST					 	
*********************************************
""")

integerList = [12,22,33,44,55,66,77]
print("\n Original List = ", integerList)

print("Length of an Integer List = ", len(integerList))


#############################################################

print("""
*********************************************
* Example 3 : USING STRING LIST					 	
*********************************************
""")

stringList = ['Krishna', 'John', 'Yung', 'Ram', 'Steve']
print("\n Original List = ", stringList)
      
print("Length of a String List = ", len(stringList))

#############################################################

print("""
*********************************************
* Example 4 : USING MIXED LIST					 	
*********************************************
""")

mixedList = ['Krishna', 20, 'John', 40.5, 'Yung', 11.98, 'Ram', 22]
print("\n Original List = ", mixedList)
      
print("Length of a Mixed List = ", len(mixedList))


#############################################################

print("""
*********************************************
* Example 5 : USING MIXED LIST					 	
*********************************************
""")

mixedList = ['Krishna', 20, 'John', (40, 50, 65), 'Yung', 11.98, 'Ram']
print("\n Original List = ", mixedList)
      
print("Length of a Mixed List = ", len(mixedList))

#############################################################

print("""
*********************************************
* Example 6 : USING NESTED LIST					 	
*********************************************
""")

nestedList = ['Krishna', 20, 'John', [20, 40, 50, 65, 22], 'Yung', 11.98]
print("\n Original List = ", nestedList)
      
print("Length of a Nested List = ", len(nestedList[3]))

#############################################################

print("""
*********************************************
* Example 7 : USING DYNAMIC LIST					 	
*********************************************
""")

intList = []
Number = int(input("Please enter the Total Number of Items in a List : "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    intList.append(value)
    
print("\n Original List = ", intList)
      
print("Length of a Dynamic List = ", len(intList))
