#!/usr/bin/python3

#############################################################
#															#
# Python Program fibonacci Series 						    #
# Created on : 4/29/2020									#
# Author     : Vikas Bansode								#
#															#
#############################################################

# What is Fibonacci Sequence?
# The Fibonacci sequence specifies a series of numbers where the next number is found by adding up the two
# numbers just before it.

print("""
*********************************************
* Example 1 : Using While Loop          					 	
*********************************************
""")

num = int(input("Please enter any number: "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci series: ",end= " ")
while(count <= n):
    print(sum,end=" ")
    count = count + 1
    a = b
    b = sum
    sum = a + b

print("""
*********************************************
* Example 1 : Using while Loop          					 	
*********************************************
""")

# Fibonacci series will start at 0 and travel upto below number
Number = int(input("\nPlease Enter the Range Number: "))

# Initializing First and Second Values of a Series
i = 0
First_Value = 0
Second_Value = 1
           
# Find & Displaying Fibonacci series
while(i < Number):
           if(i <= 1):
                      Next = i
           else:
                      Next = First_Value + Second_Value
                      First_Value = Second_Value
                      Second_Value = Next
           print(Next)
           i = i + 1
#############################################################

print("""
*********************************************
* Example 2 : Using for Loop          					 	
*********************************************
""")

# Fibonacci series will start at 0 and travel upto below number
Number = int(input("\nPlease Enter the Range Number: "))

# Initializing First and Second Values of a Series
First_Value = 0
Second_Value = 1
           
# Find & Displaying Fibonacci series
for Num in range(0, Number):
           if(Num <= 1):
                      Next = Num
           else:
                      Next = First_Value + Second_Value
                      First_Value = Second_Value
                      Second_Value = Next
           print(Next)

#############################################################

print("""
*********************************************
* Example 3 : Using Recursion function          					 	
*********************************************
""")

def Fibonacci_series(Number):
           if(Number == 0):
                      return 0
           elif(Number == 1):
                      return 1
           else:
                      return (Fibonacci_series(Number - 2)+ Fibonacci_series(Number - 1))

# End of the Function

# Fibonacci series will start at 0 and travel upto below number
Number = int(input("\nPlease Enter the Range Number: "))

# Find & Displaying Fibonacci series
for Num in range(0, Number):
           print(Fibonacci_series(Num))


