#!/usr/bin/python3

######################################################################
#															         #
# Python Program to create Database          				         # 
# Created on : 13/06/2020									         #
# Author     : Vikas Bansode								         #
#															         #
######################################################################

print("""
*********************************************
* Example 1 : Create Database	 	
*********************************************
""")

import os
import sqlite3

db_filename = 'todo.db'

db_is_new = not os.path.exists(db_filename)

conn = sqlite3.connect(db_filename)

if db_is_new:
	print("Need to create schema")
else:
	print("Database exists, assume schema does, too.")
conn.close()
