#!/bin/python3

#########################################################
#														#
# Python program for Calender							#
# Created on : 4/28/2020								#
# Author     : Vikas Bansode							#
#														#
#########################################################

# import calender module

import calendar 

# ask of month and year

year = int(input("Please enter the year: "))
month = int(input("Please enter the month: "))

# Display the python calender
print(calendar.month(year,month))
